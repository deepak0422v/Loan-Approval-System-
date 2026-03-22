Machine Learning | Python | Streamlit | Scikit-Learn

# Loan Approval System
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Machine Learning](https://img.shields.io/badge/MachineLearning-Project-green)

An end-to-end Machine Learning application that predicts whether a loan application will be approved or rejected based on applicant financial and demographic information.

The project demonstrates a complete ML pipeline, including data preprocessing, feature engineering, model training, hyperparameter tuning, evaluation, and deployment using an interactive Streamlit web application.

## Live Demo

Try the application here:
https://loan-approval-predictor-ml.streamlit.app

## Application Preview
![Loan Approval System Page](https://github.com/user-attachments/assets/5dcd7d5d-fd4f-41a7-b740-545f3424a47c)

## Demo
![Loan Approval System Demo](https://github.com/user-attachments/assets/7d66c119-e1e7-459d-ad95-0cdac0a3740c)


An end-to-end Machine Learning application that predicts whether a loan application will be approved based on applicant financial and demographic details.

---

# Project Overview

Financial institutions evaluate multiple factors before approving a loan application. This project builds a machine learning system that automates this decision-making process using historical loan applicant data.

The system:

Processes applicant information
Applies a trained machine learning model
Predicts loan approval status in real time

This project demonstrates the implementation of an end-to-end machine learning workflow, from data analysis to production deployment.

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

# System Architecture
```
User Input (Applicant Details)
        │
        ▼
Streamlit Web Interface
        │
        ▼
Feature Preprocessing Pipeline
        │
        ▼
Trained Machine Learning Model
(Random Forest Classifier)
        │
        ▼
Loan Approval Prediction
(Approved / Rejected)

```
---

## Tech Stack

Programming Language
- Python
Data Processing
- Pandas
- NumPy
Machine Learning
- Scikit-Learn
- Logistic Regression
- Random Forest Classifier
- GridSearchCV (Hyperparameter tuning)
Visualization
- Matplotlib
- Seaborn
Model Persistence
- Joblib
Deployment
- Streamlit
- Streamlit Cloud
---

## Machine Learning Model

Two machine learning models were trained and evaluated:
- Logistic Regression
- Random Forest Classifier
Random Forest achieved better performance and was selected as the final model.
Hyperparameter tuning was performed using **GridSearchCV** to optimize model performance.

# Machine Learning Pipeline

The project follows a structured ML workflow:

1. Data Cleaning  
2. Handling Missing Values  
3. Feature Engineering  
4. Categorical Encoding  
5. Train-Test Split  
6. Model Training  
7. Model Comparison  
8. Hyperparameter Tuning using GridSearchCV
9. Model Evaluation  
10. Model Deployment

---

# Feature Engineering

New features created to improve predictive performance:

- **Total_Income**
  
  ```
  Total_Income = ApplicantIncome + CoapplicantIncome
  ```

- **Income_Loan_Ratio**
  
  ```
  Income_Loan_Ratio = Total_Income / LoanAmount
  ```

These engineered features help capture financial capacity relative to loan amount, improving model accuracy.

---

# Model Evaluation Metrics

Model performance was evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

Feature importance analysis was also conducted to identify the most influential factors affecting loan approval decisions.
Key influential features include:

- Credit History
- Total Income
- Loan Amount
- Income-Loan Ratio
---

## Project Structure

```
Loan-Approval-System-
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
│   ├── preprocess.py
│   ├── train.py
│   └── predict.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```
This modular structure separates:

data
model training
preprocessing
prediction pipeline
application interface

making the project easier to maintain and extend.

---

## Features

- Data preprocessing pipeline
- Feature engineering
- Model training and evaluation
- Logistic Regression and Random Forest comparison
- Hyperparameter tuning using GridSearchCV
- Feature importance analysis
- Model persistence using Joblib
- Modular prediction pipeline
- Interactive Streamlit web application
- Cloud deployment using Streamlit Cloud

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

### 3 Launch the web application

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

## Deployment

The application is deployed using **Streamlit Cloud**.

Users can enter applicant details through the web interface and receive real-time predictions for loan approval.

## Future Improvements

- Building a REST API using FastAPI
- Implementing model monitoring and drift detection
- Adding automated model retraining pipelines
- Containerizing the application using Docker
- Deploying on cloud platforms such as AWS or GCP
---

# Author

**Parasa Deepak Kumar**  
B.Tech CSE (AIML)  
Mohan Babu University
