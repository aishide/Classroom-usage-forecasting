"""
generate_data.py
Simulate Wi-Fi occupancy data for a classroom.
Saves as 'data/wifi_occupancy.csv'
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Start time for simulation
start_time = datetime(2025, 1, 1, 8, 0)

# Number of records: 5-min intervals for 10 hours
num_records = 120

timestamps = []
occupancy = []
current_time = start_time

for i in range(num_records):
    hour = current_time.hour

    # Class hours: 9 AM to 4 PM → high occupancy
    if 9 <= hour <= 16:
        people = np.random.randint(20, 50)
    else:  # off-hours → low occupancy
        people = np.random.randint(0, 5)

    timestamps.append(current_time)
    occupancy.append(people)
    current_time += timedelta(minutes=5)

# Create DataFrame
df = pd.DataFrame({
    "timestamp": timestamps,
    "connected_devices": occupancy
})

# Save CSV
df.to_csv("data/wifi_occupancy.csv", index=False)
print("Wi-Fi occupancy data generated and saved.")
