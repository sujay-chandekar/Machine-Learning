@echo off
echo Installing dependencies...
pip install -q streamlit scikit-learn pandas numpy plotly

echo.
echo ✓ Dependencies installed!
echo.
echo Starting Streamlit app...
echo.
streamlit run streamlit_app.py
