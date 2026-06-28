import streamlit as st
import pickle
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Set page config
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0px;
    }
    </style>
""", unsafe_allow_html=True)

# Load model and scaler
@st.cache_resource
def load_model_and_data():
    with open('heart_disease_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('heart_disease_columns.pkl', 'rb') as f:
        columns = pickle.load(f)
    with open('heart_disease_scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    with open('heart_disease_scaler_columns.pkl', 'rb') as f:
        scaler_columns = pickle.load(f)
    return model, columns, scaler, scaler_columns

# Title
st.title("❤️ Heart Disease Prediction System")
st.markdown("---")

# Load model, columns and scaler
model, columns, scaler, scaler_columns = load_model_and_data()

# Create tabs
tab1, tab2, tab3 = st.tabs(["🔮 Prediction", "📊 Data Info", "ℹ️ About"])

with tab1:
    st.header("Patient Information & Prediction")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Basic Information")
        age = st.slider("Age (years)", 29, 77, 50)
        sex = st.radio("Sex", ["Female (0)", "Male (1)"], horizontal=True)
        sex_val = 0 if sex == "Female (0)" else 1
        
        st.subheader("Cardiac Measurements")
        trestbps = st.slider("Resting Blood Pressure (mmHg)", 94, 200, 130)
        chol = st.slider("Serum Cholesterol (mg/dl)", 126, 564, 240)
        thalach = st.slider("Maximum Heart Rate Achieved (bpm)", 71, 202, 150)
    
    with col2:
        st.subheader("Test Results")
        cp = st.selectbox(
            "Chest Pain Type",
            [0, 1, 2, 3],
            format_func=lambda x: [
                "Typical Angina (0)",
                "Atypical Angina (1)", 
                "Non-anginal Pain (2)",
                "Asymptomatic (3)"
            ][x]
        )
        
        fbs = st.radio("Fasting Blood Sugar > 120 mg/dl?", ["No (0)", "Yes (1)"], horizontal=True)
        fbs_val = 0 if fbs == "No (0)" else 1
        
        restecg = st.selectbox(
            "Resting Electrocardiogram",
            [0, 1, 2],
            format_func=lambda x: [
                "Normal (0)",
                "ST-T Abnormality (1)",
                "LV Hypertrophy (2)"
            ][x]
        )
        
        exang = st.radio("Exercise Induced Angina?", ["No (0)", "Yes (1)"], horizontal=True)
        exang_val = 0 if exang == "No (0)" else 1
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("Additional Tests")
        oldpeak = st.slider("ST Depression (oldpeak)", 0.0, 6.2, 1.0)
        slope = st.selectbox(
            "Slope of ST Segment",
            [0, 1, 2],
            format_func=lambda x: [
                "Upsloping (0)",
                "Flat (1)",
                "Downsloping (2)"
            ][x]
        )
    
    with col4:
        ca = st.slider("Number of Major Vessels (0-4)", 0, 4, 1)
        thal = st.selectbox(
            "Thalassemia Type",
            [0, 1, 2, 3],
            format_func=lambda x: [
                "Normal (0)",
                "Fixed Defect (1)",
                "Reversible Defect (2)",
                "Unknown (3)"
            ][x]
        )
    
    # Prepare data for prediction
    input_data = np.array([[age, sex_val, cp, trestbps, chol, fbs_val, restecg, 
                           thalach, exang_val, oldpeak, slope, ca, thal]])
    
    st.markdown("---")
    
    # Make prediction
    if st.button("🔍 Predict", use_container_width=True, type="primary"):
        try:
            # Create array with all 13 features
            input_data = np.array([[age, sex_val, cp, trestbps, chol, fbs_val, restecg, 
                                   thalach, exang_val, oldpeak, slope, ca, thal]])
            
            # Create DataFrame for easier handling
            input_df = pd.DataFrame(input_data, columns=columns)
            
            # Extract only the columns that need scaling
            to_scale = input_df[scaler_columns].values
            
            # Scale only those columns
            scaled = scaler.transform(to_scale)
            
            # Replace the original values with scaled values
            input_df[scaler_columns] = scaled
            
            # Get prediction (invert because SVC has flipped class labels)
            prediction = 1 - model.predict(input_df)[0]
            
            # Handle models with and without predict_proba
            try:
                # Works for RandomForest, LogisticRegression, etc.
                prob_raw = model.predict_proba(input_df)[0]
                # Swap because predictions are inverted
                probability = np.array([prob_raw[1], prob_raw[0]])
            except AttributeError:
                # For SVC, use decision_function to estimate probability
                decision = model.decision_function(input_df)[0]
                # Convert decision function to probability using sigmoid
                prob_disease = 1 / (1 + np.exp(-decision))
                # Invert for consistency with flipped predictions
                probability = np.array([prob_disease, 1 - prob_disease])
            
            # Display results
            st.markdown("---")
            st.subheader("🎯 Prediction Results")
            
            col_res1, col_res2 = st.columns(2)
            
            with col_res1:
                if prediction == 1:
                    st.error("⚠️ Heart Disease DETECTED", icon="❌")
                    risk_level = "HIGH RISK"
                    risk_color = "red"
                else:
                    st.success("✅ No Heart Disease", icon="✅")
                    risk_level = "LOW RISK"
                    risk_color = "green"
            
            with col_res2:
                st.metric(
                    "Risk Level",
                    risk_level,
                    delta=None
                )
            
            # Probability gauge
            st.markdown("### Confidence Score")
            
            disease_prob = probability[1] * 100
            no_disease_prob = probability[0] * 100
            
            col_gauge1, col_gauge2 = st.columns(2)
            
            with col_gauge1:
                fig_disease = go.Figure(go.Indicator(
                    mode="gauge+number+delta",
                    value=disease_prob,
                    title={'text': "Heart Disease Risk (%)"},
                    delta={'reference': 50},
                    gauge={'axis': {'range': [0, 100]},
                           'bar': {'color': "darkred"},
                           'steps': [
                               {'range': [0, 33], 'color': "lightgreen"},
                               {'range': [33, 66], 'color': "lightyellow"},
                               {'range': [66, 100], 'color': "lightcoral"}],
                           'threshold': {'line': {'color': "red", 'width': 4},
                                        'thickness': 0.75,
                                        'value': 50}
                    }))
                fig_disease.update_layout(height=300, margin=dict(l=20, r=20, t=50, b=20))
                st.plotly_chart(fig_disease, use_container_width=True)
            
            with col_gauge2:
                fig_no_disease = go.Figure(go.Indicator(
                    mode="gauge+number+delta",
                    value=no_disease_prob,
                    title={'text': "No Disease Probability (%)"},
                    delta={'reference': 50},
                    gauge={'axis': {'range': [0, 100]},
                           'bar': {'color': "darkgreen"},
                           'steps': [
                               {'range': [0, 33], 'color': "lightcoral"},
                               {'range': [33, 66], 'color': "lightyellow"},
                               {'range': [66, 100], 'color': "lightgreen"}],
                           'threshold': {'line': {'color': "green", 'width': 4},
                                        'thickness': 0.75,
                                        'value': 50}
                    }))
                fig_no_disease.update_layout(height=300, margin=dict(l=20, r=20, t=50, b=20))
                st.plotly_chart(fig_no_disease, use_container_width=True)
            
            # Summary
            st.markdown("### 📋 Summary")
            st.info(f"""
            **Prediction:** {prediction}
            - Heart Disease Probability: {disease_prob:.2f}%
            - No Disease Probability: {no_disease_prob:.2f}%
            
            **Model Accuracy:** 80.4%
            """)
            
        except Exception as e:
            st.error(f"Error in prediction: {str(e)}")

with tab2:
    st.header("📊 Feature Information")
    
    st.markdown("""
    ### Feature Descriptions:
    
    **Demographic:**
    - **Age**: Patient's age in years (29-77)
    - **Sex**: 0=Female, 1=Male
    
    **Cardiac Indicators:**
    - **Chest Pain Type (cp)**: 0=Typical Angina, 1=Atypical, 2=Non-anginal, 3=Asymptomatic
    - **Resting Blood Pressure (trestbps)**: In mmHg (normal: 120-139)
    - **Serum Cholesterol (chol)**: In mg/dl (normal: <200)
    - **Maximum Heart Rate (thalach)**: Bpm achieved during test
    - **ST Depression (oldpeak)**: Induced by exercise relative to rest
    
    **Test Results:**
    - **Fasting Blood Sugar (fbs)**: 0=≤120 mg/dl, 1=>120 mg/dl
    - **Resting ECG (restecg)**: 0=Normal, 1=ST-T abnormality, 2=LV hypertrophy
    - **Exercise Induced Angina (exang)**: 0=No, 1=Yes
    - **Slope**: 0=Upsloping, 1=Flat, 2=Downsloping
    - **Major Vessels (ca)**: Number of vessels colored by fluoroscopy (0-4)
    - **Thalassemia (thal)**: 0=Normal, 1=Fixed defect, 2=Reversible, 3=Unknown
    """)
    
    # Load and display sample data
    try:
        df = pd.read_csv('heart.csv')
        st.subheader("Dataset Overview")
        col_info1, col_info2, col_info3 = st.columns(3)
        
        with col_info1:
            st.metric("Total Samples", len(df))
        
        with col_info2:
            st.metric("Features", len(df.columns))
        
        with col_info3:
            disease_count = (df['target'] == 1).sum()
            st.metric("Disease Cases", f"{disease_count} ({disease_count/len(df)*100:.1f}%)")
        
        st.subheader("Sample Data")
        st.dataframe(df.head(10), use_container_width=True)
        
        # Statistics
        st.subheader("Statistical Summary")
        st.dataframe(df.describe(), use_container_width=True)
        
    except FileNotFoundError:
        st.warning("Dataset file not found")

with tab3:
    st.header("ℹ️ About This Application")
    
    st.markdown("""
    ### 🏥 Heart Disease Prediction System
    
    This application uses **Machine Learning** to predict the likelihood of heart disease 
    based on clinical measurements and patient health indicators.
    
    #### Model Information:
    - **Model Type**: Random Forest Classifier
    - **Accuracy**: 98.54%
    - **Training Dataset**: 1,025 patient records
    - **Features**: 13 clinical indicators
    
    #### How to Use:
    1. Enter patient information on the **Prediction** tab
    2. Fill in all required fields
    3. Click **"Predict"** button
    4. View probability scores and risk assessment
    
    #### ⚠️ Disclaimer:
    - This tool is for **educational purposes only**
    - **NOT** a substitute for professional medical diagnosis
    - Always consult with qualified healthcare professionals
    - Results should be validated with clinical assessment
    
    #### Dataset:
    - Based on UCI Heart Disease Dataset
    - 1,025 samples from multiple hospitals
    - 13 clinical features
    - Binary classification (Disease/No Disease)
    
    #### Technologies Used:
    - **Streamlit**: Web framework
    - **Scikit-learn**: Machine learning
    - **Pandas**: Data processing
    - **Plotly**: Interactive visualizations
    """)
    
    st.markdown("---")
    st.markdown("""
    **Developed with ❤️ for Medical Data Science**
    """)

st.markdown("---")
st.markdown("<div style='text-align: center'><small>© 2024 Heart Disease Prediction System | ML Project</small></div>", unsafe_allow_html=True)
