import pandas as pd

df1 = pd.read_csv('csv_files/massage_clients.csv')
df2 = pd.read_csv('csv_files/massage_clients2.csv')

merged_df = pd.concat([df1, df2], ignore_index=True)

merged_df.to_csv('merged_massage_clients.csv', index=False)

#Cleaned up data removing timestamp

df = pd.read_csv('merged_massage_clients.csv')
df['Appointment On'] = pd.to_datetime(df['Appointment On']).dt.date
df['Customer Name'] = df['Customer Name'].str.replace('*', '', regex=False)
df['Status'] = df['Status'].str.replace('/Complete', '', regex=False).str.strip()
df.to_csv('updated_merged_massage_clients.csv', index=False)