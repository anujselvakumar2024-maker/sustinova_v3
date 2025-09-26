# 🔌 ESP32 Setup Guide

## 📡 **HARDWARE SETUP:**
```
GPIO 27 → DHT11/DHT22 (Temperature/Humidity)
GPIO 34 → Soil Moisture Sensor (Analog)
GPIO 32 → Water Level Sensor
GPIO 33 → Rain Sensor (Digital)
GPIO 26 → Pump Relay Control
GPIO 25 → Buzzer (Optional)
GPIO 2  → Status LED
```

## 💻 **SOFTWARE SETUP:**
1. Open `esp32_agrosmart_eco.ino` in Arduino IDE
2. Update WiFi credentials:
   ```cpp
   const char* ssid = "YOUR_WIFI_NAME";
   const char* password = "YOUR_WIFI_PASSWORD";
   ```
3. Update server URL:
   ```cpp
   const char* serverURL = "http://YOUR_PC_IP:5000/api/sensors";
   ```
4. Upload to ESP32

## 🔍 **TESTING:**
- Open Serial Monitor (115200 baud)
- Should see WiFi connection and data transmission
- Backend will show "Sensor data updated" messages

**Real-time data every 2 seconds to your backend!**
