import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

# Parameters
n_samples = 1000

# Generate synthetic data
data = {
    'transaction_id': [fake.uuid4() for _ in range(n_samples)],
    'transaction_date': [fake.date_between(start_date='-2y', end_date='today') for _ in range(n_samples)],
    'transaction_amount': [round(random.uniform(-500, 5000), 2) for _ in range(n_samples)],
    'balance': [round(random.uniform(0, 20000), 2) for _ in range(n_samples)],
    'transaction_type': [random.choice(['debit', 'credit']) for _ in range(n_samples)],
    'credit_risk': [random.choice([0, 1]) for _ in range(n_samples)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Sort by transaction date
df = df.sort_values(by='transaction_date').reset_index(drop=True)

# Display first few rows
print(df.head())

# Save to CSV
df.to_csv('synthetic_bank_statements.csv', index=False)
