import serial
import serial.tools.list_ports
import time

baud_rate = 115200

def checkConnection(uart_port):
    PortIsConnected = False
    while PortIsConnected == False:
        connected_ports = [port.device for port in serial.tools.list_ports.comports()]
        print("Connected ports:", connected_ports)
        if uart_port in connected_ports:
            PortIsConnected = True
            print("Device is connected.")
        else:
            print("Device is not connected.")
        time.sleep(3)

def enableTSU(uart_port,command,ShowResponse):
    with serial.Serial(uart_port, baud_rate, timeout=1) as ser:
        ser.write(command)
        response = ser.read(20)
        if ShowResponse == True :
            if response:
                print(f"Response: {response}")
            else:
                print("No response received")
            time.sleep(0.5)
    return response


def generateReleasePacket(press_packet):
    if press_packet.startswith(b'\x02\x20\x02\x00'):
        release_packet = press_packet[:3] + b'\x01' + press_packet[4:]
        return release_packet



def shortPress(uart_port,button,ShowResponse):
    with serial.Serial(uart_port, baud_rate, timeout=1) as ser:
        R_button=generateReleasePacket(button)
        ser.write(button)
        ser.write(R_button)
        response = ser.read(5)
        if ShowResponse == True :
            if response:
                print(f"Response: {response}")
            else:
                print("No response received")
            time.sleep(0.5)
    return response


def longPress(uart_port,button,PressDuration,ShowResponse):
    with serial.Serial(uart_port, baud_rate, timeout=1) as ser:
        R_button=generateReleasePacket(button)
        ser.write(button)
        time.sleep(PressDuration)
        ser.write(R_button)
        response = ser.read(5)
        if ShowResponse == True :
            if response:
                print(f"Response: {response}")
            else:
                print("No response received")
            time.sleep(0.5)
    return response



def longPressNTimes(uart_port,button,PressDuration,ReleaseDuration,ShowResponse, NTimes):
    with serial.Serial(uart_port, baud_rate, timeout=1) as ser:
        R_button=generateReleasePacket(button)
        N=0
        while N < NTimes :
            ser.write(button)
            time.sleep(PressDuration)
            ser.write(R_button)
            response = ser.read(5)
            time.sleep(ReleaseDuration)
            if ShowResponse == True :
                if response:
                    print(f"Response: {response}")
                else:
                    print("No response received")
                time.sleep(0.5)
            N=N+1
    return response


def shortPressNTimes(uart_port,button,ShowResponse,NTimes,breakDuration):
    R_button = generateReleasePacket(button)
    with serial.Serial(uart_port, baud_rate, timeout=1) as ser:
        N=0
        while N < NTimes :
            ser.write(button)
            ser.write(R_button)
            time.sleep(breakDuration)
            response = ser.read(5)
            if ShowResponse == True :
                if response:
                    print(f"Response: {response}")
                else:
                    print("No response received")
                time.sleep(0.5)
            N=N+1
    return response





def shortPressMultiple(uart_port, buttonsList, ShowResponse, breakDuration):
    responses = []
    with serial.Serial(uart_port, baud_rate, timeout=1) as ser:
        for button in buttonsList:
            R_button = generateReleasePacket(button)
            ser.write(button)
            ser.write(R_button)
            response = ser.read(5)
            responses.append(response)
            time.sleep(breakDuration)
            if ShowResponse:
                if response:
                    print(f"Response: {response}")
                else:
                    print("No response received")
                time.sleep(0.5)
    return responses







