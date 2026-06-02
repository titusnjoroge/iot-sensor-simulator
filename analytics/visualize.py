import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(
    "gateway/data_store.csv",
    names=["time", "device", "temp", "humidity"]
)

plt.plot(data["temp"], label="Temperature")
plt.plot(data["humidity"], label="Humidity")
plt.legend()
plt.title("IoT Sensor Simulation")
plt.show()