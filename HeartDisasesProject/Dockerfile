FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY streamlit_app.py .
COPY heart_disease_model.pkl .
COPY heart_disease_columns.pkl .
COPY heart.csv .

# Create .streamlit directory and config
RUN mkdir -p ~/.streamlit

# Configure Streamlit
RUN echo "\
[server]\n\
port = 8501\n\
headless = true\n\
\n\
[client]\n\
showErrorDetails = true\n\
" > ~/.streamlit/config.toml

# Expose port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Run Streamlit app
CMD ["streamlit", "run", "streamlit_app.py"]
