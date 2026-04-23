import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("loan_model.pkl")

# Title and header\st.title("🏦 Smart Loan Approval Predictor")
st.markdown("""
<style>
.big-font {
    font-size:25px !important;
    color: #2E8B57;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Enter applicant details to predict loan approval:</p>', unsafe_allow_html=True)

# User Inputs
age = st.number_input("Age of Applicant", min_value=18, max_value=100, value=30)
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Marital Status", ["Yes", "No"])
dependent = st.selectbox("Number of Dependents", [0, 1, 2, 3])
education = st.selectbox("Education Level", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self-Employed", ["Yes", "No"])
income = st.number_input("Annual Income (in Lakhs)", value=5.0)
loan_amount = st.number_input("Loan Amount Required (in Lakhs)", value=10.0)
loan_term = st.number_input("Loan Term (in Years)", value=20)
credit_score = st.slider("Credit Score", min_value=300, max_value=900, value=650)

# Encode inputs same as model training
# Label Encoding used: Male=1, Female=0; Yes=1, No=0; Graduate=1, Not Graduate=0
gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
education = 1 if education == "Graduate" else 0
self_employed = 1 if self_employed == "Yes" else 0

# Prepare data for prediction
input_data = np.array([[age, gender, married, dependent, education,
                        self_employed, income, loan_amount, loan_term, credit_score]])

# Predict button
if st.button("🔢 Predict Loan Approval"):
    prediction = model.predict(input_data)[0]
    result = "✅ Approved" if prediction == 1 else "❌ Rejected"
    st.subheader(f"Loan Status: {result}")

    if prediction == 1:
        st.success("Congratulations! The applicant is likely to get loan approval.")
    else:
        st.error("Sorry, the applicant might not get the loan approved.")

# Footer
st.markdown("---")
st.markdown("Developed by Prince Joshi | Streamlit App Demo", unsafe_allow_html=True)