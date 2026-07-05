import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# -----------------------------
# Load Model and Feature Columns
# -----------------------------
model = joblib.load("churn_project_model.pkl")
FEATURE_COLUMNS = joblib.load("feature_columns.pkl")

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📉",
    layout="wide"
)

# -----------------------------
# Page Header
# -----------------------------
st.title("📉 Customer Churn Prediction App")
st.write("Enter customer details to predict whether the customer is likely to churn.")

# -----------------------------
# User Inputs
# -----------------------------

with st.expander("👤 Customer Information", expanded=True):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=18, max_value=100, value=35)
        dependents = st.number_input("Number of Dependents", min_value=0, max_value=10, value=0)
        referrals = st.number_input("Number of Referrals", min_value=0, max_value=20, value=0)

    with col2:
        gender = st.selectbox("Gender", ["Female", "Male"])
        married = st.selectbox("Married", ["No", "Yes"])
        tenure = st.number_input("Tenure in Months", min_value=0, max_value=100, value=12)

with st.expander("💳 Billing Information", expanded=True):
    col1, col2 = st.columns(2)

    with col1:
        monthly_charge = st.number_input("Monthly Charge", min_value=0.0, value=70.0)
        total_charges = st.number_input("Total Charges", min_value=0.0, value=800.0)
        contract = st.selectbox("Contract", ["Month-to-Month", "One Year", "Two Year"])

    with col2:
        paperless_billing = st.selectbox("Paperless Billing", ["No", "Yes"])
        payment_method = st.selectbox(
            "Payment Method",
            ["Bank Withdrawal", "Credit Card", "Mailed Check"]
        )
        offer = st.selectbox(
            "Offer",
            ["No Offer", "Offer A", "Offer B", "Offer C", "Offer D", "Offer E"]
        )

with st.expander("🌐 Internet & Services", expanded=True):
    col1, col2 = st.columns(2)

    with col1:
        internet_type = st.selectbox(
            "Internet Type",
            ["No Internet Service", "DSL", "Fiber Optic"]
        )
        multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes"])
        security_services = st.slider(
            "Security Services Count",
            0,
            4,
            0,
            help="""
Number of security-related services subscribed by the customer.

Includes:
• Online Security
• Online Backup
• Device Protection Plan
• Premium Tech Support

Range:
0 = None
4 = All four services
"""
        )

    with col2:
        if internet_type == "No Internet Service":
            avg_gb = 0
            streaming_tv = "No Internet Service"
            streaming_movies = "No Internet Service"
            streaming_music = "No Internet Service"
            unlimited_data = "No Internet Service"

            st.info("Internet-related services and average monthly GB download are set automatically because there is no internet service.")
        else:
            avg_gb = st.number_input(
                "Average Monthly GB Download",
                min_value=0.0,
                value=20.0,
                step=1.0
            )
            streaming_tv = st.selectbox("Streaming TV", ["No", "Yes"])
            streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes"])
            streaming_music = st.selectbox("Streaming Music", ["No", "Yes"])
            unlimited_data = st.selectbox("Unlimited Data", ["No", "Yes"])

# -----------------------------
# Create Input Data
# -----------------------------
input_data = {
    'Age': age,
    'Number of Dependents': dependents,
    'Number of Referrals': referrals,
    'Tenure in Months': tenure,
    'Avg Monthly GB Download': avg_gb,
    'Monthly Charge': monthly_charge,
    'Total Charges': total_charges,
    'Security Services': security_services,

    'Gender_Male': 1 if gender == "Male" else 0,
    'Married_Yes': 1 if married == "Yes" else 0,

    'Offer_Offer A': 1 if offer == "Offer A" else 0,
    'Offer_Offer B': 1 if offer == "Offer B" else 0,
    'Offer_Offer C': 1 if offer == "Offer C" else 0,
    'Offer_Offer D': 1 if offer == "Offer D" else 0,
    'Offer_Offer E': 1 if offer == "Offer E" else 0,

    'Multiple Lines_Yes': 1 if multiple_lines == "Yes" else 0,

    'Internet Type_DSL': 1 if internet_type == "DSL" else 0,
    'Internet Type_Fiber Optic': 1 if internet_type == "Fiber Optic" else 0,
    'Internet Type_No Internet Service': 1 if internet_type == "No Internet Service" else 0,

    'Streaming TV_No Internet Service': 1 if streaming_tv == "No Internet Service" else 0,
    'Streaming TV_Yes': 1 if streaming_tv == "Yes" else 0,

    'Streaming Movies_No Internet Service': 1 if streaming_movies == "No Internet Service" else 0,
    'Streaming Movies_Yes': 1 if streaming_movies == "Yes" else 0,

    'Streaming Music_No Internet Service': 1 if streaming_music == "No Internet Service" else 0,
    'Streaming Music_Yes': 1 if streaming_music == "Yes" else 0,

    'Unlimited Data_No Internet Service': 1 if unlimited_data == "No Internet Service" else 0,
    'Unlimited Data_Yes': 1 if unlimited_data == "Yes" else 0,

    'Contract_One Year': 1 if contract == "One Year" else 0,
    'Contract_Two Year': 1 if contract == "Two Year" else 0,

    'Paperless Billing_Yes': 1 if paperless_billing == "Yes" else 0,

    'Payment Method_Credit Card': 1 if payment_method == "Credit Card" else 0,
    'Payment Method_Mailed Check': 1 if payment_method == "Mailed Check" else 0
}

input_df = pd.DataFrame([input_data])
input_df = input_df[FEATURE_COLUMNS]

# -----------------------------
# Prediction Button
# -----------------------------
st.markdown("---")

predict_button = st.button("🚀 Predict Churn", use_container_width=True)

# -----------------------------
# Prediction Result
# -----------------------------
if predict_button:
    prediction = model.predict(input_df, validate_features=False)[0]
    probability = model.predict_proba(input_df, validate_features=False)[0][1]

    st.subheader("📊 Prediction Result")

    result_col1, result_col2 = st.columns([1, 1])

    with result_col1:
        st.metric("Churn Probability", f"{probability:.2%}")

        if prediction == 1:
            st.error("⚠️ The customer is likely to churn.")
        else:
            st.success("✅ The customer is not likely to churn.")

        if probability < 0.30:
            st.info("Risk Level: Low")
        elif probability < 0.60:
            st.warning("Risk Level: Medium")
        else:
            st.error("Risk Level: High")

    with result_col2:
        pie_data = pd.DataFrame({
            "Status": ["Churn", "No Churn"],
            "Probability": [probability, 1 - probability]
        })

        fig = px.pie(
            pie_data,
            names="Status",
            values="Probability",
            color="Status",
            color_discrete_map={
                "Churn": "red",
                "No Churn": "green"
            },
            title="Churn Probability",
            hole=0.55
        )

        fig.update_traces(
            textinfo="label+percent",
            textfont_size=15
        )

        fig.update_layout(
            title={
                "text": "Churn Probability",
                "x": 0.5,
                "xanchor": "center",
                "font": dict(size=24, color="darkblue")
            },
            showlegend=False,
            font=dict(size=15),
            margin=dict(t=70, b=20, l=20, r=20)
        )

        st.plotly_chart(fig, use_container_width=True)

    with st.expander("🔍 Model Input Preview"):
        st.dataframe(input_df, use_container_width=True)
