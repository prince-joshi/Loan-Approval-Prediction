# Loan Approval Prediction

A machine learning project that predicts whether a loan application will be approved or rejected based on applicant details like income, credit score, education, and more.

---

## About the Project

This project builds a binary classification model to predict loan approval status. Two models were trained and compared — Logistic Regression and Decision Tree — to find the better performing one. The final model is deployed as an interactive Streamlit web app.

---

## Dataset

- **File:** `loan_approval_data.csv`
- **Features:**
  - Age, Gender, Marital Status, Dependents
  - Education Level, Self-Employed
  - Annual Income, Loan Amount, Loan Term
  - Credit Score
- **Target:** `Loan_Status` (1 = Approved, 0 = Rejected)

---

## Workflow

1. Loaded and explored the dataset
2. Performed EDA — loan status distribution, education vs loan status, gender vs loan status, income and credit score boxplots
3. Label encoded categorical columns
4. Applied StandardScaler for feature scaling
5. Split data into 80% train and 20% test
6. Trained and compared two models — Logistic Regression and Decision Tree
7. Evaluated using Accuracy, Confusion Matrix, Classification Report, and ROC Curve
8. Saved the final model and scaler using joblib
9. Built a Streamlit app for real-time loan approval prediction

---

## Tech Stack

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Streamlit
- Joblib

---

## Results

### Logistic Regression (Final Model)
| Metric | Value |
|--------|-------|
| Accuracy | 70% |
| Precision (Approved) | 0.67 |
| Recall (Approved) | 0.57 |
| F1-Score (Approved) | 0.62 |

### Decision Tree
| Metric | Value |
|--------|-------|
| Accuracy | 65% |
| Precision (Approved) | 0.60 |
| Recall (Approved) | 0.50 |
| F1-Score (Approved) | 0.55 |

**Logistic Regression outperformed Decision Tree and was selected as the final model.**

---

## Files

| File | Description |
|------|-------------|
| `loan_approval_code.ipynb` | Main notebook — EDA, model training, evaluation |
| `loan_approval_data.csv` | Dataset |
| `loan_model.pkl` | Saved Logistic Regression model |
| `scaler.pkl` | Saved StandardScaler |
| `loan_prediction_app.py` | Streamlit web app for real-time prediction |

---

*Developed by Prince Joshi | Aspiring Data Analyst*
