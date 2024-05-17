import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load synthetic data
data = pd.read_csv('synthetic_bank_statements.csv')

# Transaction amount distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['transaction_amount'], bins=50, kde=True)
plt.title('Distribution of Transaction Amounts')
plt.xlabel('Transaction Amount')
plt.ylabel('Frequency')
plt.show()

# Correlation matrix
corr_matrix = data.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

# Feature engineering example: Monthly transaction count
data['transaction_month'] = pd.to_datetime(data['transaction_date']).dt.to_period('M')
monthly_transaction_counts = data.groupby('transaction_month')['transaction_id'].count().reset_index()
monthly_transaction_counts.rename(columns={'transaction_id': 'monthly_transaction_count'}, inplace=True)
print(monthly_transaction_counts.head())
