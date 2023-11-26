import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Read the data from data.txt into a pandas DataFrame
df = pd.read_csv("data.txt", names=["Timestamp", "Temperature", "Humidity"])

# Convert the 'Timestamp' column to datetime format
df["Timestamp"] = pd.to_datetime(df["Timestamp"], format="%Y-%m-%d %H:%M:%S")

# Plot Temperature vs. Time
plt.figure(figsize=(10, 5))
plt.plot(df["Timestamp"], df["Temperature"], label="Temperature")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("Temperature vs. Time")
plt.legend()
plt.grid(True)
plt.show()

# Plot Humidity vs. Time
plt.figure(figsize=(10, 5))
plt.plot(df["Timestamp"], df["Humidity"], label="Humidity", color="orange")
plt.xlabel("Time")
plt.ylabel("Humidity (%)")
plt.title("Humidity vs. Time")
plt.legend()
plt.grid(True)
plt.show()
