import serial
import serial.tools.list_ports
import time

uart_port = 'COM13'
baud_rate = 115200

def check_connection():
    PortIsConnected = False
    while PortIsConnected == False:
        connected_ports = [port.device for port in serial.tools.list_ports.comports()]
        print("Connected ports:", connected_ports)
        if 'COM13' in connected_ports:
            PortIsConnected = True
            print("Device is connected.")
        else:
            print("Device is not connected.")
        time.sleep(3)

def EnableTSU(button,ShowResponse):
    with serial.Serial(uart_port, baud_rate, timeout=1) as ser:
        ser.write(button)
        response = ser.read(9)
        if ShowResponse == True :
            if response:
                print(f"Response: {response}")
            else:
                print("No response received")
            time.sleep(0.5)
    return response


def generate_release_packet(press_packet):
    if press_packet.startswith(b'\x02\x20\x02\x00'):
        release_packet = press_packet[:3] + b'\x01' + press_packet[4:]
        return release_packet



def ShortPress(button,ShowResponse):
    with serial.Serial(uart_port, baud_rate, timeout=1) as ser:
        R_button=generate_release_packet(button)
        ser.write(button)
        ser.write(R_button)
        response = ser.read(9)
        if ShowResponse == True :
            if response:
                print(f"Response: {response}")
            else:
                print("No response received")
            time.sleep(0.5)
    return response


def longPress(button,PressDuration,ReleaseDuration,ShowResponse):
    with serial.Serial(uart_port, baud_rate, timeout=1) as ser:
        R_button=generate_release_packet(button)
        ser.write(button)
        time.sleep(PressDuration)
        ser.write(R_button)
        time.sleep(ReleaseDuration)
        response = ser.read(9)
        if ShowResponse == True :
            if response:
                print(f"Response: {response}")
            else:
                print("No response received")
            time.sleep(0.5)
    return response



def longpress_N_Times(button,PressDuration,ReleaseDuration,ShowResponse, NTimes):
    with serial.Serial(uart_port, baud_rate, timeout=1) as ser:
        R_button=generate_release_packet(button)
        N=0
        while N <= NTimes :
            ser.write(button)
            time.sleep(PressDuration)
            ser.write(R_button)
            time.sleep(ReleaseDuration)
            response = ser.read(9)
            if ShowResponse == True :
                if response:
                    print(f"Response: {response}")
                else:
                    print("No response received")
                time.sleep(0.5)
            N=N+1
    return response


def ShortPress_N_Times(button,ShowResponse,NTimes,breakDuration):
    R_button = generate_release_packet(button)
    with serial.Serial(uart_port, baud_rate, timeout=1) as ser:
        N=0
        while N <= NTimes :
            ser.write(button)
            ser.write(R_button)
            time.sleep(breakDuration)
            response = ser.read(9)
            if ShowResponse == True :
                if response:
                    print(f"Response: {response}")
                else:
                    print("No response received")
                time.sleep(0.5)
            N=N+1
    return response





def shortPressMultiple(buttonsList, ShowResponse, breakDuration):
    with serial.Serial(uart_port, baud_rate, timeout=1) as ser:
        for button in buttonsList:
            R_button = generate_release_packet(button)
            ser.write(button)
            ser.write(R_button)
            response = ser.read(9)
            time.sleep(breakDuration)
            if ShowResponse:
                if response:
                    print(f"Response: {response}")
                else:
                    print("No response received")
                time.sleep(0.5)
    return response