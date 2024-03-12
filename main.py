from Functions import *


Enable_TSU = b'\x02\x10\x05\x01\x54\x45\x53\x54\x03'
Button_ChanUp= b'\x02\x20\x02\x00\x18\x03'

send_packet(Enable_TSU)
time.sleep(0.5)
send_packet(Enable_TSU)
time.sleep(0.5)
send_packet(Enable_TSU)
time.sleep(0.5)
send_packet(Enable_TSU)
time.sleep(0.5)
send_packet(Enable_TSU)
time.sleep(0.5)
send_packet(Enable_TSU)
time.sleep(0.5)
send_packet(Enable_TSU)
time.sleep(0.5)
send_packet(Enable_TSU)
time.sleep(0.5)
send_packet(Enable_TSU)
time.sleep(0.5)
send_packet(Enable_TSU)
time.sleep(0.5)

while True:

    send_packet(Button_ChanUp)

