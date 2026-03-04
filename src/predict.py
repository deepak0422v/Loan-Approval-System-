import joblib
import pandas as pd
from src.preprocess import preprocess_data

model = joblib.load("models/loan_model.pkl")
model_columns = joblib.load("models/model_columns.pkl")

def predict(data):

    df = pd.DataFrame([data])

    # Apply preprocessing
    df = preprocess_data(df)

    # Match training columns exactly
    df = df.reindex(columns=model_columns, fill_value=0)

    prediction = model.predict(df)

    return prediction[0]