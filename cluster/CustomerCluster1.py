import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.cluster import KMeans
from connector import MySQLConnector


# Kết nối MySQL
def getConnect():
    connector = MySQLConnector()
    return connector.connect()


# Hàm truy vấn MySQL
def queryDataset(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    df = pd.DataFrame(cursor.fetchall(), columns=[i[0] for i in cursor.description])
    return df


# Lấy dữ liệu từ MySQL
conn = getConnect()
sql = "SELECT * FROM customer"
df = queryDataset(conn, sql)

sql2 = """
    SELECT DISTINCT customer.CustomerId, Age, Annual_Income, Spending_Score 
    FROM customer 
    JOIN customer_spend_score ON customer.CustomerId = customer_spend_score.CustomerID
"""
df2 = queryDataset(conn, sql2)
df2.columns = ['CustomerId', 'Age', 'Annual Income', 'Spending Score']


# Hàm vẽ biểu đồ histogram
def showHistogram(df, columns):
    plt.figure(figsize=(7, 8))
    for i, column in enumerate(columns, 1):
        plt.subplot(len(columns), 1, i)
        sns.histplot(df[column], bins=32, kde=True)
        plt.title(f'Histogram of {column}')
    plt.show()


showHistogram(df2, df2.columns[1:])


# Hàm Elbow Method
def elbowMethod(df, columnsForElbow):
    X = df[columnsForElbow].values
    inertia = []
    for n in range(1, 11):
        model = KMeans(n_clusters=n, init='k-means++', max_iter=500, random_state=42)
        model.fit(X)
        inertia.append(model.inertia_)

    plt.figure(figsize=(15, 6))
    plt.plot(range(1, 11), inertia, 'o-')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Cluster Sum of Squared Distances')
    plt.title('Elbow Method')
    plt.show()


elbowMethod(df2, ['Age', 'Spending Score'])


# Hàm K-Means clustering
def runKMeans(X, cluster):
    model = KMeans(n_clusters=cluster, init='k-means++', max_iter=500, random_state=42)
    model.fit(X)
    return model.labels_, model.cluster_centers_


X = df2[['Age', 'Spending Score']].values
df2["cluster"], centroids = runKMeans(X, 4)


# Hàm vẽ scatter plot
def visualizeKMeans(X, y_kmeans, cluster, title, xlabel, ylabel):
    plt.figure(figsize=(10, 10))
    colors = ["red", "green", "blue", "purple", "black"]

    for i in range(cluster):
        plt.scatter(X[y_kmeans == i, 0], X[y_kmeans == i, 1], s=100, c=colors[i], label=f'Cluster {i + 1}')

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()


visualizeKMeans(X, df2["cluster"].values, 4, "Clusters of Customers", "Age", "Spending Score")

# Hàm hiển thị danh sách khách hàng theo cụm
def print_cluster_details(conn, df2):
    unique_clusters = df2["cluster"].unique()

    for cluster in unique_clusters:
        customer_ids = df2[df2["cluster"] == cluster]["CustomerId"].tolist()
        sql = f"SELECT * FROM customer WHERE CustomerId IN ({','.join(map(str, customer_ids))})"
        df_customers = queryDataset(conn, sql)
        print(f"### Customers in Cluster {cluster} ###")
        print(df_customers)
        print("\n" + "=" * 50 + "\n")


print_cluster_details(conn, df2)
