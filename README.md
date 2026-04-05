# 📊 Real-Time Anomaly Detection System

## 🚀 Overview

This project implements a **real-time anomaly detection system** for streaming data using statistical techniques.
It processes incoming data points, maintains a sliding window of recent values, and detects anomalies based on deviation from normal behavior.

---

## ✨ Features

* 🔄 Real-time data stream simulation
* 🧠 Sliding window based statistical analysis
* 🚨 Z-score based anomaly detection
* ⚡ Cold-start handling to avoid unstable detection
* 📊 Live visualization using Streamlit
* 🧹 Prevention of anomaly contamination in baseline

---

## 🏗️ Project Structure

```bash
anomaly-detection/
│
├── src/
│   ├── detector.py              # Core anomaly detection logic
│   ├── stream_simulator.py      # Generates real-time data stream
│
├── app/
│   └── streamlit_app.py         # Streamlit dashboard
│
├── main.py                      # CLI runner
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/mouktikzz/Real-Time-Anomaly-Detection
cd anomaly-detection
pip install -r requirements.txt
```

---

## ▶️ Usage

### 🖥️ Run CLI (Terminal Monitoring)

```bash
python main.py
```

### 📊 Run Streamlit Dashboard

```bash
streamlit run app/streamlit_app.py
```

---

## 🧠 How It Works

1. **Sliding Window**

   * Maintains a fixed-size window of recent values
   * Continuously updates as new data arrives

2. **Cold Start Phase**

   * Builds initial baseline
   * Performs cautious anomaly detection with limited data

3. **Z-Score Detection**

   * Computes mean and standard deviation from window
   * Flags values that deviate beyond a threshold

4. **Anomaly Handling**

   * Detected anomalies are **not added to the window**
   * Prevents contamination of statistical baseline

---

## 📊 Example

```text
📥 Collecting: 11
📥 Collecting: 10
🚨 Anomaly: 50 | z=3.20
✅ Normal: 12
🚨 Anomaly: 55 | z=3.80
```

---

## 🛠️ Tech Stack

* Python
* NumPy
* Streamlit

---

## 💡 Key Concepts

* Sliding Window Processing
* Real-Time Data Streams
* Statistical Anomaly Detection (Z-score)
* Cold Start Problem Handling
* Data Pipeline Design

---

## 📈 Future Improvements

* IQR-based anomaly detection (robust to outliers)
* Hybrid detection (Z-score + IQR)
* Kafka-based streaming pipeline
* Advanced visualization (highlight anomalies on graph)
* Deployment on cloud

---

## 👨‍💻 Author

Mouktik Dasari
