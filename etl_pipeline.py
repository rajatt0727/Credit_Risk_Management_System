import pandas as pd

def etl_pipeline():
    # Load raw data
    raw_data = pd.read_csv('synthetic_bank_statements.csv')

    # Data cleaning steps
    raw_data.drop_duplicates(inplace=True)
    raw_data.ffill(inplace=True)  # Replace fillna with ffill directly
    #raw_data.fillna(method='ffill', inplace=True)
    raw_data['transaction_date'] = pd.to_datetime(raw_data['transaction_date'], format='%Y-%m-%d')

    # Save cleaned data
    raw_data.to_csv('cleaned_bank_statements.csv', index=False)

# Run the pipeline
etl_pipeline()
