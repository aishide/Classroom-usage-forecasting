"""
app.py
Interactive Streamlit dashboard using Plotly
Features:
- Forecast horizon slider
- Peak usage alert
- Confidence intervals
- Download forecast CSV
"""

import streamlit as st
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import plotly.graph_objects as go

# -------------------- Page Setup --------------------
st.set_page_config(page_title="Classroom Electricity Forecast", layout="wide")
st.title("🏫 Classroom Electricity Usage Forecasting ")

st.markdown(
    """
    <small>
    Aishi De
    </small>
    """,
    unsafe_allow_html=True
)

# -------------------- Load Data --------------------
df = pd.read_csv("data/electricity_usage.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df.set_index("timestamp", inplace=True)

# -------------------- Historical Usage --------------------
st.subheader("📊 Historical Electricity Usage")

hist_fig = go.Figure()
hist_fig.add_trace(go.Scatter(
    x=df.index,
    y=df["electricity_kW"],
    mode="lines",
    name="Actual Usage"
))
hist_fig.update_layout(
    xaxis_title="Time",
    yaxis_title="Electricity Usage (kW)",
    hovermode="x unified"
)
st.plotly_chart(hist_fig, use_container_width=True)

# -------------------- Forecast Controls --------------------
st.subheader("⚙️ Forecast Settings")
forecast_minutes = st.slider(
    "Forecast next (minutes)",
    min_value=30,
    max_value=180,
    value=60,
    step=5
)
forecast_steps = forecast_minutes // 5

# -------------------- ARIMA Forecast --------------------
model = ARIMA(df["electricity_kW"], order=(1,1,1))
model_fit = model.fit()

forecast = model_fit.get_forecast(steps=forecast_steps)
forecast_values = forecast.predicted_mean
conf_int = forecast.conf_int()

forecast_index = pd.date_range(
    df.index[-1] + pd.Timedelta(minutes=5),
    periods=forecast_steps,
    freq="5T"
)

# -------------------- Peak Usage --------------------
peak_load = forecast_values.max()
st.markdown(
    f"### ⚡ Predicted peak load in next {forecast_minutes} minutes: **{peak_load:.2f} kW**"
)

if peak_load > 8:
    st.warning("⚠️ High electricity load expected. Energy optimization recommended.")

# -------------------- Forecast Plot (Plotly) --------------------
st.subheader("🔮 Electricity Usage Forecast")

forecast_fig = go.Figure()

# Actual data
forecast_fig.add_trace(go.Scatter(
    x=df.index,
    y=df["electricity_kW"],
    mode="lines",
    name="Actual Usage"
))

# Forecast line
forecast_fig.add_trace(go.Scatter(
    x=forecast_index,
    y=forecast_values,
    mode="lines",
    name="Forecast",
    line=dict(color="red")
))

# Confidence interval
forecast_fig.add_trace(go.Scatter(
    x=list(forecast_index) + list(forecast_index[::-1]),
    y=list(conf_int.iloc[:, 1]) + list(conf_int.iloc[:, 0][::-1]),
    fill="toself",
    fillcolor="rgba(255,0,0,0.2)",
    line=dict(color="rgba(255,255,255,0)"),
    hoverinfo="skip",
    name="Confidence Interval"
))

forecast_fig.update_layout(
    xaxis_title="Time",
    yaxis_title="Electricity Usage (kW)",
    hovermode="x unified"
)

st.plotly_chart(forecast_fig, use_container_width=True)

# -------------------- Forecast Table --------------------
st.subheader("📄 Forecast Data")

forecast_table = pd.DataFrame({
    "Time": forecast_index,
    "Forecast (kW)": forecast_values,
    "Lower CI": conf_int.iloc[:, 0],
    "Upper CI": conf_int.iloc[:, 1]
})

st.dataframe(forecast_table, use_container_width=True)

# -------------------- Download Button --------------------
csv = forecast_table.to_csv(index=False)
st.download_button(
    "⬇️ Download Forecast CSV",
    data=csv,
    file_name="electricity_forecast.csv",
    mime="text/csv"
)
