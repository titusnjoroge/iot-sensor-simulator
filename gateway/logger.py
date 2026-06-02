import csv
from datetime import datetime
import random
import time

print("IoT Gateway Running...")

with open("gateway/data_store.csv", "a") as f:
    writer = csv.writer(f)

    while True:
        data = {
            "device_id": "node_01",
            "temperature": round(random.uniform(18, 35), 2),
            "humidity": round(random.uniform(30, 80), 2)
        }

        writer.writerow([
            datetime.now(),
            data["device_id"],
            data["temperature"],
            data["humidity"]
        ])

        print("Logged:", data)
        time.sleep(2)