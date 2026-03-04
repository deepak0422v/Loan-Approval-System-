import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from preprocess import preprocess_data

df = pd.read_csv("data/train.csv")

df = preprocess_data(df)

X = df.drop("Loan_Status_Y", axis=1)
y = df["Loan_Status_Y"]
joblib.dump(X.columns, "models/model_columns.pkl")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    max_depth=10,
    min_samples_leaf=2,
    min_samples_split=5,
    random_state=42
)

model.fit(X_train, y_train)

joblib.dump(model, "models/loan_model.pkl")

print("Model trained and saved.")