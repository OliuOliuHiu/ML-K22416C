from flask import Flask, render_template_string
import pandas as pd
from connector import MySQLConnector
from CustomerCluster1 import queryDataset, df2

app = Flask(__name__)


# Kết nối database
def getConnect():
    connector = MySQLConnector()
    return connector.connect()


conn = getConnect()


@app.route('/clusters')
def show_clusters():
    unique_clusters = df2["cluster"].unique()
    cluster_data = {}

    for cluster in unique_clusters:
        customer_ids = df2[df2["cluster"] == cluster]["CustomerId"].tolist()
        sql = f"SELECT * FROM customer WHERE CustomerId IN ({','.join(map(str, customer_ids))})"
        df_customers = queryDataset(conn, sql)
        cluster_data[cluster] = df_customers.to_html(index=False)

    html_template = """
    <html>
        <head>
            <title>Customer Clusters</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                table { border-collapse: collapse; width: 100%; margin-bottom: 20px; }
                th, td { border: 1px solid black; padding: 8px; text-align: left; }
                th { background-color: #f2f2f2; }
            </style>
        </head>
        <body>
            <h1>Customer Clusters</h1>
            {% for cluster, table in cluster_data.items() %}
                <h2>Cluster {{ cluster }}</h2>
                {{ table | safe }}
            {% endfor %}
        </body>
    </html>
    """

    return render_template_string(html_template, cluster_data=cluster_data)


if __name__ == '__main__':
    app.run(debug=True)
