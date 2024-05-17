# Credit Risk Management Project

## Project Overview
This project aims to create a simulated credit risk management system using synthetic bank statement data. The project demonstrates capabilities in data collection, preparation, analysis, modeling, and policy refinement.

## Table of Contents
1. [Project Scope and Requirements](#project-scope-and-requirements)
2. [Data Generation](#data-generation)
3. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
4. [Machine Learning Models](#machine-learning-models)
5. [ETL Pipeline](#etl-pipeline)
6. [Policy Refinement](#policy-refinement)
7. [Monitoring and Iteration](#monitoring-and-iteration)
8. [Conclusion](#conclusion)

## Project Scope and Requirements
**Objective:** Create a simulated credit risk management system using synthetic bank statement data. Demonstrate capabilities in data collection, preparation, analysis, modeling, and policy refinement.

## Data Generation
1. **File:** `generate_synthetic_data.py`
2. **Libraries Used:** `pandas`, `numpy`, `faker`, `random`
3. **Description:** Generates 1000 samples of synthetic bank statement data with features including `transaction_id`, `transaction_date`, `transaction_amount`, `balance`, `transaction_type`, and `credit_risk`.
4. **Run Command:**
    ```sh
    python generate_synthetic_data.py
    ```

## Exploratory Data Analysis (EDA)
1. **File:** `eda_and_feature_engineering.py`
2. **Libraries Used:** `pandas`, `matplotlib`, `seaborn`
3. **Description:** Performs EDA on the synthetic data, including plotting the distribution of transaction amounts and generating a correlation matrix. Also includes feature engineering to calculate monthly transaction counts.
4. **Run Command:**
    ```sh
    python eda_and_feature_engineering.py
    ```

## Machine Learning Models
1. **File:** `model_training_and_evaluation.py`
2. **Libraries Used:** `pandas`, `scikit-learn`
3. **Description:** Trains a Random Forest classifier to predict credit risk using `transaction_amount` and `balance` as features. Evaluates the model using classification report and ROC-AUC score.
4. **Run Command:**
    ```sh
    python model_training_and_evaluation.py
    ```

## ETL Pipeline
1. **File:** `etl_pipeline.py`
2. **Description:** Cleans and preprocesses the raw synthetic data, removing duplicates and handling missing values, and saves the cleaned data to a CSV file.
3. **Run Command:**
    ```sh
    python etl_pipeline.py
    ```

## Policy Refinement
**Description:** Based on the model's predictions, insights and proposed policy changes are documented. This step involves analyzing the model's output to refine credit risk policies.

## Monitoring and Iteration
1. **File:** `monitor_model_performance.py`
2. **Description:** Monitors the performance of the trained model on new synthetic data, providing updated classification reports and ROC-AUC scores.
3. **Run Command:**
    ```sh
    python monitor_model_performance.py
    ```

## Conclusion
This project demonstrates a comprehensive approach to credit risk management using synthetic data. By following the steps outlined, we have generated synthetic data, performed exploratory data analysis, built and evaluated a machine learning model, set up an ETL pipeline, refined policies, and implemented a monitoring system. 

## How to Run the Project
1. Clone the repository.
2. Install the required libraries:
    ```sh
    pip install pandas numpy faker matplotlib seaborn scikit-learn
    ```
3. Run each script in the following order:
    ```sh
    python generate_synthetic_data.py
    python eda_and_feature_engineering.py
    python model_training_and_evaluation.py
    python etl_pipeline.py
    python monitor_model_performance.py
    ```

## Repository Structure
```sh
    |-- generate_synthetic_data.py

    |-- eda_and_feature_engineering.py

    |-- model_training_and_evaluation.py

    |-- etl_pipeline.py

    |-- monitor_model_performance.py

    |-- synthetic_bank_statements.csv

    |-- cleaned_bank_statements.csv

    |-- README.md
```

## Acknowledgements
Special thanks to the contributors and the community for their support and resources.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

