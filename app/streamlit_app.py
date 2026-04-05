import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import time
from src.detector import AnomalyDetector
from src.stream_simulator import generate_stream

st.title("📊 Real-Time Anomaly Detection")

detector = AnomalyDetector(window_size=10, threshold=2.5)
stream = generate_stream()

data = []
chart_placeholder = st.empty()   # placeholder for chart
status_placeholder = st.empty()  # placeholder for status

# Run limited iterations to avoid infinite loop in Streamlit
for _ in range(50):
    value = next(stream) 

    result = detector.update(value)
    
    data.append(value)
    
    chart_placeholder.line_chart(data)  

    if result["status"] == "anomaly":
        status_placeholder.error(f"🚨 Anomaly Detected: {result}")
    else:
        status_placeholder.success(f"✅ Normal: {value}")

    time.sleep(0.3)
