import pandas as pd

def preprocess_data(df):

    # Drop Loan_ID if present
    if "Loan_ID" in df.columns:
        df = df.drop("Loan_ID", axis=1)

    # Feature engineering
    df["Total_Income"] = df["ApplicantIncome"] + df["CoapplicantIncome"]

    df["Income_Loan_Ratio"] = df["Total_Income"] / df["LoanAmount"]

    # One-hot encoding
    df = pd.get_dummies(df, drop_first=True)

    return df