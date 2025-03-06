import pandas as pd
import numpy as np
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from connector import MySQLConnector

# Kết nối MySQL
def getConnect():
    connector = MySQLConnector(server="localhost", port=3306, database="sakila",
                               username="root", password="123456")
    return connector.connect()

# Hàm truy vấn dữ liệu
def queryDataset(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    df = pd.DataFrame(cursor.fetchall(), columns=[i[0] for i in cursor.description])
    return df

# Truy vấn dữ liệu từ MySQL
conn = getConnect()
sql = """
SELECT c.customer_id, 
       c.first_name, 
       c.last_name, 
       COUNT(r.rental_id) AS total_rentals,
       COUNT(DISTINCT f.film_id) AS unique_films_rented,
       COUNT(DISTINCT fc.category_id) AS unique_categories
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN film_category fc ON f.film_id = fc.film_id
GROUP BY c.customer_id, c.first_name, c.last_name;
"""
df = queryDataset(conn, sql)

# Chọn các cột số để phân cụm
df_cluster = df[['total_rentals', 'unique_films_rented', 'unique_categories']]

# Áp dụng Elbow Method để tìm số cụm tối ưu
def elbowMethod(df):
    X = df.values
    inertia = []
    for n in range(1, 11):
        model = KMeans(n_clusters=n, init='k-means++', max_iter=500, random_state=42)
        model.fit(X)
        inertia.append(model.inertia_)

    plt.figure(figsize=(10, 5))
    plt.plot(range(1, 11), inertia, 'o-')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Cluster Inertia')
    plt.title('Elbow Method')
    plt.show()

elbowMethod(df_cluster)

# Chọn số cụm và áp dụng K-Means
def runKMeans(X, clusters):
    model = KMeans(n_clusters=clusters, init='k-means++', max_iter=500, random_state=42)
    return model.fit_predict(X)

df['cluster'] = runKMeans(df_cluster, 4)  # Số cụm tối ưu sau Elbow Method

# Hiển thị kết quả phân cụm
print(df.head())

# Vẽ biểu đồ scatter plot phân cụm
def visualizeClusters(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='total_rentals', y='unique_films_rented', hue='cluster', palette='viridis')
    plt.xlabel("Total Rentals")
    plt.ylabel("Unique Films Rented")
    plt.title("Customer Clusters Based on Film Interest")
    plt.legend(title="Cluster")
    plt.show()

visualizeClusters(df)
