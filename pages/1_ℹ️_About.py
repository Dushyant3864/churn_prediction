import streamlit as st

st.set_page_config(page_title="About", page_icon="ℹ️", layout="wide")

st.title("ℹ️ About This Project")

st.markdown(
    """
    ## Customer Churn Prediction Dashboard

    This project predicts whether a telecom customer is likely to churn based on customer profile,
    service usage, billing information, contract details, and internet-related services.

    The goal is to help a business identify high-risk customers early so that retention strategies
    can be applied before the customer leaves.
    """
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 Project Objectives")
    st.markdown(
        """
        - Predict customer churn using machine learning.
        - Analyze customer behavior through EDA.
        - Compare multiple classification models.
        - Deploy the final model using Streamlit.
        - Build a complete, easy-to-use ML web application.
        """
    )

with col2:
    st.subheader("🧠 Final Model")
    st.markdown(
        """
        - **Algorithm**: Tuned XGBoost Classifier
        - **Problem Type**: Binary Classification
        - **Target**: Churn / No Churn
        - **Important Metrics**: F1 Score, Recall, ROC-AUC
        """
    )

st.divider()

st.subheader("🗂️ Dataset Information")
st.markdown(
    """
    The dataset contains telecom customer information such as:

    - Demographic details like age, gender, and marital status
    - Account information like tenure, contract type, and payment method
    - Service details like internet type, streaming services, and unlimited data
    - Billing details like monthly charges and total charges
    - Customer churn status
    """
)

st.divider()

st.subheader("⚙️ Machine Learning Workflow")

workflow = [
    "Data Collection",
    "Data Cleaning",
    "Exploratory Data Analysis",
    "Feature Engineering",
    "Train-Test Split",
    "Model Training",
    "Model Evaluation",
    "Hyperparameter Tuning",
    "Model Saving",
    "Streamlit Deployment",
]

for i, step in enumerate(workflow, start=1):
    st.markdown(f"**{i}. {step}**")

st.divider()

st.subheader("🛠️ Technologies Used")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        """
        **Programming**
        - Python
        - Pandas
        - NumPy
        """
    )

with c2:
    st.markdown(
        """
        **Machine Learning**
        - Scikit-learn
        - XGBoost
        - SMOTE
        - Joblib / Pickle
        """
    )

with c3:
    st.markdown(
        """
        **App & Visualization**
        - Streamlit
        - Plotly
        - Matplotlib / Seaborn
        """
    )

st.divider()

st.subheader("📁 Recommended Project Structure")

st.code(
    """
Customer_Churn_Prediction/
│
├── app.py
├── Telecom_Customer_Churn.csv
├── churn_project_model.pkl
├── feature_columns.pkl
├── requirements.txt
├── README.md
│
└── pages/
    └── 1_ℹ️_About.py
    """,
    language="text",
)

st.divider()

st.subheader("🚀 Future Improvements")
st.markdown(
    """
    - Add batch prediction using uploaded CSV files.
    - Add customer-level retention recommendations.
    - Add SHAP explainability for individual predictions.
    - Deploy the app publicly using Streamlit Community Cloud.
    """
)

st.divider()

st.subheader("👨‍💻 Author")
st.markdown(
    """
    **Dushyant Silot**  
    Electronics and Communication Engineering  (Dual Degree)
    Machine Learning Project: Customer Churn Prediction
    """
)

col1, col2 = st.columns(2)
with col1:
    st.link_button("GitHub", "https://github.com/Dushyant3864")
with col2:
    st.link_button("LinkedIn", "https://www.linkedin.com/in/dushyantsilot")
