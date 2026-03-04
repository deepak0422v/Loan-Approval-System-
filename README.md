Machine Learning | Python | Streamlit | Scikit-Learn

# Loan Approval Prediction System

An end-to-end Machine Learning application that predicts whether a loan application will be approved based on applicant financial and demographic details.

---

# Project Overview

This project builds a complete machine learning pipeline for loan approval prediction using historical applicant data.

The system includes:

- Data preprocessing
- Feature engineering
- Model training and evaluation
- Hyperparameter tuning
- Model persistence
- Prediction pipeline
- Interactive web interface using Streamlit

Users can input applicant details and receive a real-time loan approval prediction.

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Matplotlib
- Seaborn
- Joblib

---

# Machine Learning Pipeline

The project follows a structured ML workflow:

1. Data Cleaning  
2. Handling Missing Values  
3. Feature Engineering  
4. Categorical Encoding  
5. Train-Test Split  
6. Model Training  
7. Model Comparison  
8. Hyperparameter Tuning  
9. Model Evaluation  
10. Model Deployment

---

# Feature Engineering

New features created:

- **Total_Income**
  
  ```
  Total_Income = ApplicantIncome + CoapplicantIncome
  ```

- **Income_Loan_Ratio**
  
  ```
  Income_Loan_Ratio = Total_Income / LoanAmount
  ```

These engineered features improved model performance.

---

# Models Implemented

The following models were trained and compared:

- Logistic Regression
- Random Forest Classifier

Hyperparameter tuning was performed using **GridSearchCV** to optimize the Random Forest model.

---

# Model Evaluation Metrics

Model performance was evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

Feature importance analysis was also performed to identify the most influential variables affecting loan approval.

---

# Project Structure

```
Loan Approval ML
│
├── data
│   └── train.csv
│
├── models
│   ├── loan_model.pkl
│   └── model_columns.pkl
│
├── notebooks
│   └── eda.ipynb
│
├── src
│   ├── train.py
│   ├── preprocess.py
│   └── predict.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

# Features

- Automated preprocessing pipeline
- Feature engineering
- Model comparison
- Hyperparameter tuning
- Feature importance visualization
- Model persistence using Joblib
- Interactive Streamlit UI
- Real-time loan approval prediction

---

# How to Run the Project

### 1 Install dependencies

```
pip install -r requirements.txt
```

### 2 Train the model

```
python src/train.py
```

### 3 Run the application

```
streamlit run app.py
```

---

# Example Prediction Interface

Users can enter:

- Gender
- Marital Status
- Income
- Loan Amount
- Credit History
- Property Area

The system predicts whether the loan will be **Approved or Rejected**.

---

# Future Improvements

- Deploy the model as a REST API using FastAPI
- Cloud deployment (Streamlit Cloud / AWS)
- Add model monitoring for data drift
- Improve UI with advanced visualizations

---

# Author

**Parasa Deepak Kumar**  
B.Tech CSE (AIML)  
Mohan Babu University