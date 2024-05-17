import pandas as pd
from sklearn.metrics import classification_report, roc_auc_score

# Function to monitor model performance
def monitor_model_performance(model):
    # Load new synthetic data
    new_data = pd.read_csv('synthetic_bank_statements.csv')

    # Preprocess data
    new_data['transaction_date'] = pd.to_datetime(new_data['transaction_date'], format='%Y-%m-%d')

    # Predict using trained model
    X_new = new_data[['transaction_amount', 'balance']]
    y_new = new_data['credit_risk']
    y_pred_new = model.predict(X_new)

    # Evaluate performance
    print(classification_report(y_new, y_pred_new))
    print("ROC-AUC Score:", roc_auc_score(y_new, y_pred_new))

# Load the trained model from previous steps (assumes the model is saved or retrain here)
from model_training_and_evaluation import model

# Run the monitoring
monitor_model_performance(model)
