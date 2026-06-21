# Heart Disease Prediction Application

A Streamlit web application for predicting heart disease risk using machine learning.

## 📋 Features

- **Interactive Prediction Interface**: User-friendly form to input patient health metrics
- **Real-time Predictions**: Instant heart disease risk assessment
- **Visual Analytics**: Probability gauges and risk indicators
- **Feature Documentation**: Detailed explanation of all clinical features
- **Responsive Design**: Works on desktop and mobile devices
- **Model Performance**: 98.54% accuracy on test data

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Verify Required Files
Ensure these files are in the same directory:
- `streamlit_app.py` (main application)
- `heart_disease_model.pkl` (trained model)
- `heart_disease_columns.pkl` (feature columns)
- `heart.csv` (optional, for data info tab)

### Step 3: Run the Application
```bash
streamlit run streamlit_app.py
```

The application will open in your default browser at `http://localhost:8501`

## 📖 Usage Guide

### 1. **Prediction Tab** 🔮
- Enter patient information (age, sex, measurements)
- Click "Predict" button
- View probability scores and risk assessment

### 2. **Data Info Tab** 📊
- Learn about each feature
- View dataset statistics
- Explore sample data

### 3. **About Tab** ℹ️
- Application information
- Model details
- Disclaimer and usage guidelines

## 🔬 Model Details

| Aspect | Details |
|--------|---------|
| **Algorithm** | Random Forest Classifier |
| **Accuracy** | 98.54% |
| **Features** | 13 clinical indicators |
| **Training Data** | 1,025 patient records |
| **Classes** | Binary (Disease/No Disease) |

## 📊 Input Features

### Demographic
- **Age**: 29-77 years
- **Sex**: Female (0) or Male (1)

### Cardiac Measurements
- **Chest Pain Type**: 0-3 (4 types)
- **Resting Blood Pressure**: 94-200 mmHg
- **Serum Cholesterol**: 126-564 mg/dl
- **Maximum Heart Rate**: 71-202 bpm
- **ST Depression**: 0-6.2

### Test Results
- **Fasting Blood Sugar**: Yes/No
- **Resting ECG**: 0-2 (3 types)
- **Exercise Induced Angina**: Yes/No
- **ST Segment Slope**: 0-2 (3 types)
- **Major Vessels**: 0-4
- **Thalassemia**: 0-3 (4 types)

## ⚠️ Disclaimer

**IMPORTANT:** This application is:
- For **educational purposes only**
- **NOT** a substitute for professional medical diagnosis
- Should **NOT** be used for clinical decision-making
- Must be validated with qualified healthcare professionals

Always consult with a licensed physician for medical advice.

## 🔧 Troubleshooting

### Model file not found
```
Error: FileNotFoundError: heart_disease_model.pkl
```
**Solution**: Ensure model files are in the same directory as the script.

### Dependencies missing
```
Error: ModuleNotFoundError: No module named 'streamlit'
```
**Solution**: Run `pip install -r requirements.txt`

### Port already in use
```
Error: Address already in use
```
**Solution**: Run on different port:
```bash
streamlit run streamlit_app.py --server.port 8502
```

## 📁 Project Structure

```
HeartDiseasesProject/
├── streamlit_app.py              # Main application
├── heart_disease_model.pkl       # Trained model
├── heart_disease_columns.pkl     # Feature columns
├── heart.csv                     # Dataset (optional)
├── heart_Disease.ipynb           # Analysis notebook
├── requirements.txt              # Dependencies
└── README.md                     # This file
```

## 🎯 Next Steps

To deploy this application:

### **Option 1: Streamlit Cloud** (Recommended)
1. Push code to GitHub
2. Go to https://streamlit.io/cloud
3. Deploy in one click

### **Option 2: Docker**
```bash
docker build -t heart-disease-app .
docker run -p 8501:8501 heart-disease-app
```

### **Option 3: Heroku**
```bash
git push heroku main
```

## 📚 References

- Dataset: [UCI Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/Heart+Disease)
- Streamlit Docs: https://docs.streamlit.io/
- Scikit-learn: https://scikit-learn.org/

## 📝 License

This project is provided as-is for educational purposes.

## 👨‍💻 Author

Created for Heart Disease ML Project 2024

---

**Questions or Issues?** Feel free to modify and customize the application for your needs!
