# Monitoring-Temperature-and-Humidity-with-Raspberry-Pi-and-DHT11

**🔧 Tools & Technologies Used:**

1: Raspberry Pi 4 (or any Raspberry Pi model)  

2: Python 3  

3: DHT11 Temperature & Humidity Sensor  

4: Adafruit_DHT Python Library 

6: Raspberry Pi OS  

7: Terminal / CLI

**📁 Project Files Overview:**

File  Description:

 task1raspberry.py    | Reads real-time temperature and humidity data from the DHT11 sensor using Raspberry Pi GPIO pins and prints it to the terminal.

**⚙️ Setup Instructions:**

**1:Hardware Connections:**

| DHT11 Pin | Connect To             |
|-----------|------------------------|
| VCC       | 5V Power on Raspberry Pi |
| GND       | GND Pin                |
| DATA      | GPIO Pin (e.g., GPIO4) |

**2:Install Required Packages:**

sudo apt update

sudo apt install python3-pip

pip3 install Adafruit_DHT

**3:Run the Python Script:**

python3  task1raspberry.py

**-> This will display output like:**

Temp=26.5*C  Humidity=60.2%

Temp=26.6*C  Humidity=60.0%

**✅ Significance of Project:**

i): Demonstrates how to connect and interface a real-world sensor with Raspberry Pi GPIO pins.

ii): Useful for building DIY weather stations, IoT systems, or smart home temperature monitoring.

iii): Simple and effective for beginners in Raspberry Pi or electronics.

iv): No external display needed — all output is shown via the terminal.


