import time
import board
import adafruit_dht

# Setup DHT11 sensor on BCM pin 4
dhtDevice = adafruit_dht.DHT11(board.D4)

while True:
    try:
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity

        if temperature is not None and humidity is not None:
            print(f"Temp: {temperature:.1f}°C  Humidity: {humidity:.1f}%")
        else:
            print("Sensor read error.")

    except RuntimeError as error:
        print(f"Runtime error: {error}")
        # Don't quit on errors; retry in the next loop

    time.sleep(2)
