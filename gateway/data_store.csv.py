import random
import time
import json

def generate_packet():
    return {
        "device_id": "node_01",
        "temperature": round(random.uniform(18, 35), 2),
        "humidity": round(random.uniform(30, 80), 2),
    }

while True:
    print(json.dumps(generate_packet()))
    time.sleep(2)