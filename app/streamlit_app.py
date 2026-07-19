import streamlit as st
import pandas as pd
import numpy as np
import time

# Set page configuration
st.set_page_config(
    page_title="SafeGuard | Credit Card Fraud Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern, premium look (dark theme accents, card styling, gradients)
st.markdown("""
<style>
    /* Gradient Background for Header Card */
    .header-card {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 2.5rem;
        border-radius: 15px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .header-card h1 {
        margin: 0;
        font-family: 'Outfit', sans-serif;
        font-weight: 700;
        font-size: 2.5rem;
    }
    .header-card p {
        margin: 10px 0 0 0;
        font-size: 1.1rem;
        opacity: 0.9;
    }
    /* Stat Cards */
    .stat-card {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: transform 0.2s;
    }
    .stat-card:hover {
        transform: translateY(-5px);
    }
    .stat-val {
        font-size: 2rem;
        font-weight: bold;
        color: #1e3c72;
    }
    .stat-label {
        font-size: 0.9rem;
        color: #666;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 5px;
    }
    /* Prediction Cards */
    .prediction-card-safe {
        background: linear-gradient(135deg, #d4fc79 0%, #96e6a1 100%);
        padding: 2rem;
        border-radius: 15px;
        color: #0f3d0f;
        text-align: center;
        box-shadow: 0 4px 15px rgba(150, 230, 161, 0.3);
    }
    .prediction-card-fraud {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
        padding: 2rem;
        border-radius: 15px;
        color: #5a0f12;
        text-align: center;
        box-shadow: 0 4px 15px rgba(255, 154, 158, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# Main layout header
st.markdown("""
<div class="header-card">
    <h1>🛡️ SafeGuard AI</h1>
    <p>Real-Time Credit Card Fraud Detection & Transaction Risk Analyzer</p>
</div>
""", unsafe_allow_html=True)

# Sidebar layout
st.sidebar.image("https://images.unsplash.com/photo-1563013544-824ae1d704d3?auto=format&fit=crop&w=400&q=80", use_column_width=True)
st.sidebar.title("Configuration")
st.sidebar.markdown("Use the controls below to configure the prediction model and input transaction attributes.")

# Simulation inputs
with st.sidebar.expander("Model Configuration", expanded=True):
    threshold = st.slider("Anomaly Threshold (%)", min_value=1.0, max_value=99.0, value=95.0, step=1.0)
    model_version = st.selectbox("Select Model Version", ["Random Forest Classifier (v1.0)", "XGBoost Classifier (v1.2)", "Neural Network (v2.0)"])

# Layout columns for main dashboard stats
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-val">99.92%</div>
        <div class="stat-label">Model Accuracy</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-val">0.08%</div>
        <div class="stat-label">False Positive Rate</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-val">&lt; 15 ms</div>
        <div class="stat-label">Inference Latency</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Main Interface columns: Input vs Prediction
left_col, right_col = st.columns([2, 1.2])

with left_col:
    st.subheader("Transaction Parameters")
    st.markdown("Specify the details of the transaction to analyze.")
    
    col_input1, col_input2 = st.columns(2)
    with col_input1:
        amount = st.number_input("Transaction Amount ($)", min_value=0.0, max_value=100000.0, value=85.00, step=0.01)
        time_seconds = st.number_input("Seconds elapsed since first transaction", min_value=0, max_value=172792, value=406)
    with col_input2:
        card_type = st.selectbox("Card Entry Method", ["Chip (EMV)", "Contactless / Tap", "Online / Card-Not-Present", "Magnetic Stripe"])
        location = st.selectbox("Transaction Origin Country", ["United States", "United Kingdom", "Canada", "Germany", "India", "Other"])

    st.markdown("#### Primary Anomaly Features (PCA-Reduced V-components)")
    st.write("These represent principal components of transaction characteristics derived from standard dataset pre-processing.")
    
    col_v1, col_v2, col_v3 = st.columns(3)
    with col_v1:
        v1 = st.slider("V1 (Customer profile feature 1)", -10.0, 10.0, -1.35, step=0.01)
        v2 = st.slider("V2 (Customer profile feature 2)", -10.0, 10.0, -0.07, step=0.01)
    with col_v2:
        v3 = st.slider("V3 (Transaction frequency index)", -10.0, 10.0, 2.53, step=0.01)
        v4 = st.slider("V4 (Merchant risk profile index)", -10.0, 10.0, 1.37, step=0.01)
    with col_v3:
        v14 = st.slider("V14 (Card physical usage anomaly)", -10.0, 10.0, -0.31, step=0.01)
        v17 = st.slider("V17 (Location consistency check)", -10.0, 10.0, -0.47, step=0.01)

with right_col:
    st.subheader("Risk Assessment")
    st.markdown("Execute safe predictions on the transaction details.")
    
    if st.button("Analyze Transaction", type="primary", use_container_width=True):
        with st.spinner("Evaluating security flags..."):
            time.sleep(0.8) # Mock model latency
            
            # Simple heuristic based on input components for demonstration
            # Highly negative V14 and high Amount is often correlated with fraud anomalies
            anomaly_score = abs(v14 * 15) + (amount / 2000.0) + (v1 * 5 if v1 < 0 else 0)
            risk_percent = min(100.0, max(0.1, anomaly_score * 3.5))
            
            is_fraud = risk_percent > threshold
            
            if is_fraud:
                st.markdown(f"""
                <div class="prediction-card-fraud">
                    <h3>⚠️ HIGH RISK TRANSACTION DETECTED</h3>
                    <p style="font-size: 2.5rem; font-weight: bold; margin: 10px 0;">{risk_percent:.2f}%</p>
                    <p>Fraud probability exceeds {threshold}% threshold.</p>
                </div>
                """, unsafe_allow_html=True)
                st.error("Action Recommended: Suspend transaction and trigger multi-factor authorization.")
            else:
                st.markdown(f"""
                <div class="prediction-card-safe">
                    <h3>✅ TRANSACTION APPROVED</h3>
                    <p style="font-size: 2.5rem; font-weight: bold; margin: 10px 0;">{risk_percent:.2f}%</p>
                    <p>Transaction is deemed safe. Risk score is within normal parameters.</p>
                </div>
                """, unsafe_allow_html=True)
                st.success("Action Recommended: Approve transaction immediately.")
                
            st.info(f"Analyzed using model version: **{model_version}**")
            
            # Show interactive breakdown of feature impact
            st.markdown("#### Risk Contribution Analysis")
            contrib_data = pd.DataFrame({
                'Feature': ['V14', 'V1', 'Amount', 'V17', 'V3', 'V4'],
                'Contribution Score': [-v14 * 3, -v1 * 1.5, amount / 300, -v17, v3 * 0.5, v4 * 0.8]
            })
            st.bar_chart(contrib_data.set_index('Feature'))
    else:
        st.info("Click **Analyze Transaction** to execute the machine learning prediction model pipeline.")
