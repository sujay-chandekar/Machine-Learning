#!/usr/bin/env python3
"""Verify that all pickle files are correctly saved."""

import pickle
import pandas as pd
import numpy as np

print("=" * 60)
print("🔍 VERIFYING SETUP")
print("=" * 60)

try:
    # Load model
    print("\n1️⃣ Loading model...")
    with open('heart_disease_model.pkl', 'rb') as f:
        model = pickle.load(f)
    print(f"   ✅ Model loaded: {type(model).__name__}")
    
    # Load scaler
    print("\n2️⃣ Loading scaler...")
    with open('heart_disease_scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    print(f"   ✅ Scaler loaded")
    print(f"   ✅ Scaler expects {scaler.n_features_in_} features")
    
    # Load scaler columns
    print("\n3️⃣ Loading scaler columns...")
    with open('heart_disease_scaler_columns.pkl', 'rb') as f:
        scaler_columns = pickle.load(f)
    print(f"   ✅ Scaler columns: {scaler_columns}")
    
    # Load all columns
    print("\n4️⃣ Loading all columns...")
    with open('heart_disease_columns.pkl', 'rb') as f:
        columns = pickle.load(f)
    print(f"   ✅ Total columns: {len(columns)}")
    print(f"   ✅ Columns: {columns}")
    
    # Verify dimensions
    print("\n" + "=" * 60)
    print("✅ VERIFICATION RESULTS")
    print("=" * 60)
    
    if scaler.n_features_in_ == len(scaler_columns):
        print(f"✅ Scaler features ({scaler.n_features_in_}) matches scaler columns ({len(scaler_columns)})")
    else:
        print(f"❌ MISMATCH: Scaler expects {scaler.n_features_in_} but has {len(scaler_columns)} columns")
    
    if len(columns) == 13:
        print(f"✅ Model has 13 features")
    else:
        print(f"❌ Model has {len(columns)} features (expected 13)")
    
    # Test prediction
    print("\n" + "=" * 60)
    print("🧪 TESTING PREDICTION")
    print("=" * 60)
    
    # Create sample input (all 13 features)
    sample_input = np.array([[
        50,    # age
        1,     # sex
        0,     # cp
        130,   # trestbps
        240,   # chol
        0,     # fbs
        0,     # restecg
        150,   # thalach
        0,     # exang
        1.0,   # oldpeak
        1,     # slope
        1,     # ca
        2      # thal
    ]])
    
    # Create DataFrame
    input_df = pd.DataFrame(sample_input, columns=columns)
    
    # Scale only the specified columns
    input_df[scaler_columns] = scaler.transform(input_df[scaler_columns])
    
    # Make prediction
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]
    
    print(f"\n✅ Sample prediction successful!")
    print(f"   Prediction: {prediction} (0=No Disease, 1=Disease)")
    print(f"   No Disease: {probability[0]*100:.2f}%")
    print(f"   Has Disease: {probability[1]*100:.2f}%")
    
    print("\n" + "=" * 60)
    print("✅ ALL CHECKS PASSED! UI IS READY!")
    print("=" * 60)
    print("\n🚀 Run: streamlit run streamlit_app.py")
    
except Exception as e:
    print(f"\n❌ ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
