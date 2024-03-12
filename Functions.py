import serial
import time

uart_port = 'COM13'
baud_rate = 115200

def send_packet(packet):

    with serial.Serial(uart_port, baud_rate, timeout=1) as ser:
        ser.write(packet)
        response = ser.read(9)
        if response:
            print(f"Response: {response}")
        else:
            print("No response received")
        time.sleep(0.5)
