import streamlit as st
import numpy as np
import pickle

# --- Load your trained model (example: Random Forest) ---
with open("rf_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# --- Define the features you want the user to input ---
features = [
    'Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9',
    'V10', 'V11', 'V12', 'V14', 'V16', 'V17', 'V18', 'V19', 'V20',
    'V21', 'V24', 'V27', 'V28','Amount'
]

st.title("💳 Credit Card Fraud Detection")

st.write("Enter the transaction details below to check if it's fraud or not:")

# --- Collect user inputs ---
user_inputs = []
for feat in features:
    val = st.number_input(f"{feat}", value=0.0, format="%.4f")
    user_inputs.append(val)

# Scale with SAME scaler
input_array = np.array(user_inputs).reshape(1, -1)
features_scaled = scaler.transform(input_array)

# --- Prediction button ---
if st.button("Predict"):
    input_array = np.array(features_scaled).reshape(1, -1)  # reshape to (1, n_features)
    prediction = model.predict(input_array)[0]

    if prediction == 1:
        st.error("🚨 This transaction is predicted to be **Fraudulent**!")
    else:
        st.success("✅ This transaction is predicted to be **Legit**.")
