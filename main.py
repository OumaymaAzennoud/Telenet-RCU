from Functions import *
from Commands import *
import serial


#----------------------------------------
#Variable
#----------------------------------------
uart_port = 'COM14'
PressDuration = 3
ReleaseDuration = 1
breakDuration=1
buttonsList = [Digit1, Back, Digit2, Back,Digit3, Back, Digit4, Back,Digit5, Back, Digit6, Back,Digit7, Digit8, Back, Digit9, Back,Digit0, Back , NavUp, Back, Context, Back, ChanDown, Back,  Yellow, Back, NavLeft, Back, VolUp, Back, Rewind, Back, Mute, Back, Blue, Back, Home, Back, Select, Back, Voice, Back, PlayPause, Back, SidekeyProfile, Back, NavRight, Back, ChanUp, Back, FastFwd, Back, Input, Back, Epg, Back, NavDown, Back, VolDown, Back, Red, Back, LiveTv, Back, Record, Back, Green, StbPower,Back,StbPower]
ShowResponse=True

#----------------------------------------

check_connection(uart_port)

response=0
while response != TSU_Is_Enabled :
    response=EnableTSU(uart_port,Enable_TSU, ShowResponse)

while True:
    shortPressMultiple(uart_port,buttonsList,ShowResponse, breakDuration)



