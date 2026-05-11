import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load('stroke_model.pkl')
scaler = joblib.load('scaler.pkl')

# Page config
st.set_page_config(page_title="Stroke Risk Predictor", page_icon="🧠")

# Title
st.title("🧠 Stroke Risk Prediction App")
st.markdown("This app predicts the likelihood of a stroke based on clinical and demographic information.")
st.markdown("---")

# Input form
st.subheader("Enter Patient Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=100, value=45)
    hypertension = st.selectbox("Hypertension", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    heart_disease = st.selectbox("Heart Disease", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    ever_married = st.selectbox("Ever Married", options=[1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
    residence_type = st.selectbox("Residence Type", options=[1, 0], format_func=lambda x: "Urban" if x == 1 else "Rural")

with col2:
    avg_glucose_level = st.number_input("Average Glucose Level", min_value=50.0, max_value=300.0, value=100.0)
    bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
    gender = st.selectbox("Gender", options=[1, 0], format_func=lambda x: "Male" if x == 1 else "Female")
    work_type = st.selectbox("Work Type", options=["Private", "Self-employed", "Govt_job", "children", "Never_worked"])
    smoking_status = st.selectbox("Smoking Status", options=["formerly smoked", "never smoked", "smokes", "Unknown"])

st.markdown("---")

# Encode work_type
work_type_Never_worked = 1 if work_type == "Never_worked" else 0
work_type_Private = 1 if work_type == "Private" else 0
work_type_Self_employed = 1 if work_type == "Self-employed" else 0
work_type_children = 1 if work_type == "children" else 0

# Encode smoking_status
smoking_formerly = 1 if smoking_status == "formerly smoked" else 0
smoking_never = 1 if smoking_status == "never smoked" else 0
smoking_smokes = 1 if smoking_status == "smokes" else 0

# Build input array
input_data = np.array([[
    gender, age, hypertension, heart_disease, ever_married,
    residence_type, avg_glucose_level, bmi,
    work_type_Never_worked, work_type_Private,
    work_type_Self_employed, work_type_children,
    smoking_formerly, smoking_never, smoking_smokes
]])

# Scale input
input_scaled = scaler.transform(input_data)

# Predict button
if st.button("Predict Stroke Risk"):
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    st.markdown("---")
    st.subheader("Prediction Result")

    if prediction == 1:
        st.error(f"⚠️ High Stroke Risk Detected — Probability: {probability:.1%}")
        st.markdown("Please consult a medical professional immediately.")
    else:
        st.success(f"✅ Low Stroke Risk — Probability: {probability:.1%}")
        st.markdown("Continue maintaining a healthy lifestyle.")

    st.info("⚠️ This tool is for educational purposes only and is not a substitute for professional medical advice.")