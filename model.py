"""
model.py
Calculate electricity usage from Wi-Fi occupancy.
Plot historical usage and forecast next hour using ARIMA.
"""

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# -------------------- Load Data --------------------
df = pd.read_csv("data/wifi_occupancy.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df.set_index("timestamp", inplace=True)

# -------------------- Electricity Calculation --------------------
BASE_LOAD = 2.0          # kW
POWER_PER_DEVICE = 0.15  # kW per connected device

df["electricity_kW"] = BASE_LOAD + (df["connected_devices"] * POWER_PER_DEVICE)

# Save electricity usage CSV
df.to_csv("data/electricity_usage.csv", index=True)
print("Electricity usage data saved as 'electricity_usage.csv'.")

# -------------------- Plot Historical Usage --------------------
plt.figure()
plt.plot(df.index, df["electricity_kW"], label="Electricity Usage (kW)")
plt.xlabel("Time")
plt.ylabel("Electricity Usage")
plt.title("Classroom Electricity Usage Over Time")
plt.legend()
plt.show()

# -------------------- ARIMA Forecast --------------------
# Train ARIMA model (p,d,q) = (1,1,1)
model = ARIMA(df["electricity_kW"], order=(1,1,1))
model_fit = model.fit()

# Forecast next 1 hour (12 points at 5-min intervals)
forecast = model_fit.get_forecast(steps=12)
forecast_values = forecast.predicted_mean
conf_int = forecast.conf_int()

# Print forecast
print("\nNext 1 hour forecast (kW):")
print(forecast_values)
print("\nConfidence Intervals:")
print(conf_int)

# Plot forecast with confidence interval
plt.figure()
plt.plot(df.index, df["electricity_kW"], label="Actual")
forecast_index = pd.date_range(df.index[-1] + pd.Timedelta(minutes=5),
                               periods=12, freq='5T')
plt.plot(forecast_index, forecast_values, color='red', label="Forecast")
plt.fill_between(forecast_index, conf_int.iloc[:,0], conf_int.iloc[:,1],
                 color='pink', alpha=0.3)
plt.xlabel("Time")
plt.ylabel("Electricity Usage (kW)")
plt.title("Next 1 Hour Forecast with Confidence Interval")
plt.legend()
plt.show()
