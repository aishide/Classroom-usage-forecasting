# 🏫 Classroom Usage Forecasting  

### Electricity Demand Prediction using Wi-Fi Occupancy & ARIMA

This project predicts **short-term classroom electricity usage** using **Wi-Fi occupancy data** (connected devices) and a **time-series forecasting model (ARIMA)**.  
It includes an **interactive dashboard** to visualize historical usage, forecasts, and confidence intervals.

---

## 📌 Table of Contents

1. [Problem Statement](#-problem-statement)  
2. [Approach & Methodology](#-approach--methodology)  
3. [Tech Stack](#-tech-stack)  
4. [Project Structure](#-project-structure)  
5. [How to Run the Project](#-how-to-run-the-project)  
6. [Dashboard Features](#-dashboard-features)  
7. [Key Concepts](#-key-concepts-used)  
8. [Note on Data](#-note-on-data)  
9. [Authors](#-authors)  

---

## 📌 Problem Statement
Educational institutions often lack real-time insights into classroom electricity consumption.  
Wi-Fi access logs can act as a **proxy for room occupancy**.

This project demonstrates how **sensor-like data** (Wi-Fi device counts) can be used to:
- Estimate electricity consumption
- Forecast next-hour power usage
- Identify potential peak load periods

---

## 🧠 Approach & Methodology

1. **Wi-Fi Occupancy Simulation**
   - Simulated connected devices at 5-minute intervals
   - Higher occupancy during class hours, lower during off hours

2. **Electricity Usage Estimation**
   - Base load (always-on devices)
   - Additional load per connected device

3. **Time Series Forecasting**
   - ARIMA model trained on historical electricity usage
   - Forecasts next 30–180 minutes
   - Includes confidence intervals

4. **Interactive Dashboard**
   - Built using Streamlit & Plotly
   - Adjustable forecast horizon
   - Peak load alerts
   - Downloadable forecast data

---

## 🛠️ Tech Stack

- **Python**  
- **Pandas & NumPy** – Data handling  
- **Statsmodels** – ARIMA time-series model  
- **Matplotlib** – Exploratory plots  
- **Streamlit** – Interactive dashboard  
- **Plotly** – Dynamic visualizations  

---

## 📂 Project Structure
```
classroom_usage_forecasting/
│
├── app.py # Streamlit dashboard
├── model.py # Electricity calculation & ARIMA forecasting
├── generate_data.py # Wi-Fi occupancy data simulation
├── requirements.txt # Project dependencies
├── .gitignore
└── data/
├── wifi_occupancy.csv # Simulated sensor data
└── electricity_usage.csv # Derived electricity usage
```

---

## 🚀 How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
python generate_data.py
python model.py
streamlit run app.py
```
---

## 📊 Dashboard Features

- 📈 **Historical electricity usage** – View the classroom electricity consumption over time.  
- 🔮 **Short-term electricity forecasting** – Forecast the next 30–180 minutes of electricity usage using ARIMA.  
- 📉 **Confidence intervals** – See the expected range of forecasts to understand uncertainty.  
- ⚠️ **Peak usage alerts** – Get notified when predicted usage exceeds critical thresholds.  
- ⬇️ **Downloadable forecast CSV** – Export forecast data for further analysis or reporting.

---

## 🔍 Key Concepts Used

- **Sensor data & proxy variables** – Using Wi-Fi connected devices to approximate classroom occupancy.  
- **Time series forecasting** – Predicting future values based on historical trends.  
- **ARIMA (AutoRegressive Integrated Moving Average)** – Statistical model for short-term forecasts.  
- **Energy analytics** – Estimating and analyzing electricity usage patterns.  
- **Data-driven decision support** – Helping schools optimize electricity consumption based on predictions.

---

## ⚠️ Note on Data

This project uses **synthetic Wi-Fi occupancy data** generated for demonstration purposes.  
> In a real-world deployment, we would use Wi-Fi access point logs, network telemetry, or IoT sensor data to measure actual occupancy and electricity usage.

---

## 👥 Authors

- **Aishi De**

---

