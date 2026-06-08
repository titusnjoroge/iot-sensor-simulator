# 🌡️ IoT Sensor Node Simulator (No Hardware Required)

## 📌 Overview
This project simulates a real IoT embedded system using Python and C-style logic without any physical hardware.

It demonstrates how IoT devices send data to a gateway and how data is processed and visualized.

---

## System Architecture

Sensor Node → Gateway → CSV Storage → Data Visualization

---

## ⚙️ Features
- Simulated temperature & humidity sensor data
- Embedded-style firmware logic (C simulation)
- IoT gateway logging system
- Data visualization using Python
- Beginner-friendly IoT pipeline

---

##  Tech Stack
- C (embedded firmware simulation)
- Python (IoT simulation + backend)
- Pandas (data handling)
- Matplotlib (visualization)

---

##  Project Structure
firmware_sim/
gateway/
analytics/

---

##  How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```
python gateway/logger.py

python analytics/visualize.py

#Output
CSV log of sensor data
Live terminal logging
Graph showing sensor trends

#Future Improvements
Add MQTT communication
Replace simulation with ESP32 hardware
Build Flask web dashboard
Add real-time WebSocket updates

