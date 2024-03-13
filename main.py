from Functions import *
from Commands import *
import serial


#----------------------------------------
#Variable
#----------------------------------------
PressDuration = 3
ReleaseDuration = 1
breakDuration=1
buttonsList=[ChanDown,ChanUp,Home,Back,Digit1,Home,Back,Digit4]
ShowResponse=True
response=0
#----------------------------------------

check_connection()

while response != b'\x02\x10\x06\x02\x01\x00\x03\x00\x07' :
    response=EnableTSU(Enable_TSU, ShowResponse)

while True:
    shortPressMultiple(buttonsList,ShowResponse, breakDuration)

