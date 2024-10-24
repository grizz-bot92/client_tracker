import pandas as pd
import psycopg2

db_params = {
    'dbname':'massage_clients',
    'user':'postgres',
    'password':'password',
    'port':'5432'
}

connection = psycopg2.connect(**db_params)

sql_query = """
SELECT * FROM "massage_clients"; """

df = pd.read_sql_query(sql_query, connection)

connection.close()

print(df.head())