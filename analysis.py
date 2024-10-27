import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"updated_merged_massage_clients.csv")

# Monthly trends:

df['Appointment On'] = pd.to_datetime(df['Appointment On'], format='%Y-%m-%d', errors='coerce')

df['Year'] = df['Appointment On'].dt.year
df['Month'] = df['Appointment On'].dt.month
monthly_count = df.groupby(['Year', 'Month']).size().unstack(fill_value=0)

plt.figure(figsize=(10, 6))
sns.heatmap(monthly_count.T, cmap="YlGnBu", annot=True, fmt="d")
plt.title('Appointment Per Month')
plt.xlabel('Year')
plt.ylabel('Number of Appointments')
plt.xticks(rotation=45)
plt.tight_layout()
# plt.savefig('appt_per_month_heatmap.png', bbox_inches='tight')
plt.show()

# Revenue comparison:
revenue_by_year = df.groupby('Year')['Price'].sum()

plt.figure(figsize=(8, 8))


def total(pct, allvalues):
    absolute = int(pct / 100. * sum(allvalues))
    return f'${absolute}'


plt.pie(revenue_by_year, labels=revenue_by_year.index.astype(str), autopct=lambda pct:
total(pct, revenue_by_year.values), startangle=140, colors=['blue', 'orange'])
plt.title('Revenue Comparison (2022 vs. 2023)')
plt.axis('equal')
# plt.savefig('revenue_by_year.png', bbox_inches='tight')
plt.show()

# Most popular appointment
treatment_counts = df['Treatment Name'].value_counts()

most_popular_treatment = treatment_counts.idxmax()
most_popular_count = treatment_counts.max()

plt.figure(figsize=(10, 6))
treatment_counts.plot(kind='bar', color='skyblue')
plt.title('Count of Each Treatment')
plt.xlabel('Treatment Name')
plt.ylabel('Number of Appointments')
plt.xticks(rotation=45, fontsize=8)
plt.tight_layout()
# plt.savefig('treatment_counts.png', bbox_inches='tight')
plt.show()

#Status by month
df['Status'] = df['Status'].replace({'No Show': 'No Show/Cancelled', 'Cancelled': 'No Show/Cancelled'})


not_attended = df[df['Status'] == 'No Show/Cancelled']
monthly_cancellations = not_attended.groupby(['Year', 'Month']).size().reset_index(name='Count')
pivot_df = monthly_cancellations.pivot(index='Month', columns='Year', values='Count').fillna(0)

pivot_df.plot(kind='line', marker='o')
plt.title('Monthly Appointment Trend for No Show/Cancelled')
plt.xlabel('Month')
plt.ylabel('Count')
plt.xticks(range(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend(title='Year')
plt.grid(True)
plt.tight_layout()
# plt.savefig('cancellations_by_year.png', bbox_inches='tight')
plt.show()
