# Real-Time Anomaly Detection System

## 📌 Overview
This project detects anomalies in streaming data using statistical methods like Z-score and sliding window analysis.

## 🚀 Features
- Real-time data stream simulation
- Sliding window anomaly detection
- Z-score based outlier detection
- Streamlit dashboard visualization

## 🧠 Tech Stack
- Python
- NumPy
- Streamlit

## ⚙️ How It Works
1. Maintains a sliding window of recent data
2. Computes mean and standard deviation
3. Calculates Z-score for new data point
4. Flags anomalies if threshold exceeded

## ▶️ Run

### CLI
```bash
pip install requirements.txt
cd app
streamlit run streamlit_app.py
