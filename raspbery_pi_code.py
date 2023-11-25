import serial
import time
from serial.serialutil import SerialException

# Replace 'COMx' with the correct serial port on your system


interval = 5  # Interval in seconds


def read_serial_data():
    try:
        ser = serial.Serial("/dev/cu.usbmodem142301", 9600, timeout=1)
        ser.write(b"\r\n")  # Send Enter to trigger the Arduino to send data
        time.sleep(1)  # Allow time for the Arduino to process and send data

        while True:
            line = ser.readline().decode().strip()
            if line == "Reading values succesful":
                print("Received valid data:")
                data = []
                for _ in range(2):  # Read the next 5 lines
                    data_line = ser.readline().decode().strip()
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    data.append(data_line)
                print(data)
                with open("data.txt", "a") as f:
                    f.write(f"{timestamp},{data[0]},{data[1]}\n")
                time.sleep(interval)
                break
            else:
                print("Waiting for valid data...")
                time.sleep(interval)  # Wait for 10 minutes
    except SerialException as e:
        print(f"Serial error: {e}")
        time.sleep(interval)  # Wait for 5 seconds and attempt to reconnect


if __name__ == "__main__":
    try:
        while True:
            read_serial_data()
    except KeyboardInterrupt:
        print("Script terminated by user.")
