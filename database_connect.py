import pandas as pd
import psycopg2

# Database connection parameters
db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'password',
    'host': 'localhost',
    'port': '5432'
}

connection = None

try:
    connection = psycopg2.connect(**db_params)
    print("Database connected successfully")

    # Create a cursor object
    cursor = connection.cursor()

    # Sample query to fetch data
    query = "SELECT * FROM massage_clients;"  
    cursor.execute(query)

    # Fetch all results
    records = cursor.fetchall()

    # Convert to DataFrame
    df = pd.DataFrame(records, columns=[desc[0] for desc in cursor.description])

    # Print the DataFrame
    print(df)

except Exception as e:
    print("An error occurred while connecting to the database:", e)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Database connection closed")
