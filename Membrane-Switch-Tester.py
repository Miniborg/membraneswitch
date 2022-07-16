# GPIO setup and imports
import RPi.GPIO as GPIO
import time
import random
import LCD1602
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#Variables
startTime = time.time()
pin = 21
iterations = 1000
interval = .05
topright = 21
top = 20
middle = 12
topleft = 16
bottomleft = 5
period = 26
bottomright = 19
bottom = 13
Test = False

#Keypad
C1 = 27
C2 = 24
C3 = 18
C4 = 23

L1 = 4
L2 = 6
L3 = 17
L4 = 22

#Screen
score = "Get Ready..."
funnyword = ""

#Selection system
selectionlist = ["0","1","2","3","4","5","6","7","8","9","hasht","ast","A","B","C","D"]

#Pin setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#7 segment display number def setup
def off():
    GPIO.output(22, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)

d = {
    '0': [22,21,16,20,19,19,5],
    '1': [bottomright, topright],
    '2': [top, topright, bottomleft, middle, bottom],
    '3': [top, topleft, middle, bottomleft, bottom],
    '4': [topleft, topright, middle, bottomright],
    '5': [top, topleft, bottomright, middle, bottom],
    '6': [top, topleft, middle, bottomleft, bottomright, bottom],
    '7': [top, topright, bottomright],
    '8': [top, topright, bottomright, middle, bottom, bottomleft, topleft],
    '9': [top, topright, topleft, middle, bottomright, bottom],
    'ast': [period],
    'hasht': [topleft, topright, middle, bottomleft, bottomright],
    'A': [period, top, topleft, topright, middle, bottomleft, bottomright],
    'B': [top, topright, bottomright, middle, bottom, bottomleft, topleft, period],
    'C': [top, topleft, bottomleft, bottom, period],
    'D' : [top, topleft, bottomleft, bottom, bottomright, topright, period],
    
}

def set_screen(n):
    off()
    for i in d[n]:
        GPIO.output(i, GPIO.HIGH)

#7 segment display changer

#Checks if you did the right input and handles it
def checknum(inputt, target):
    if inputt == target:
        target = selectionlist[random.randrange(-1,16)]
        tim = time.time() - startTime - 2.5
        setup(tim, "Cleared")
        time.sleep(.15)
        GPIO.output(25, GPIO.LOW)
    else:
        pass
    pass
#Turns on the screen and score
def setup(lie, scoe):
    LCD1602.init(0x27, 1) # init(slave address, background light)
    LCD1602.write(0, 0, "Time :" + str(lie))
    LCD1602.write(1, 1, str(scoe))
    time.sleep(2)
    
#Removes screen details
def destroy():
    LCD1602.clear()


#Checks the keypad for input
def readLine(line, characters):
    GPIO.output(line, GPIO.HIGH)
    idx = 0
    if(GPIO.input(C1) == 1):
        idx = 0
    elif(GPIO.input(C2) == 1):
        idx = 1
    elif(GPIO.input(C3) == 1):
        idx = 2
    elif(GPIO.input(C4) == 1):
        idx = 3
    GPIO.output(25, GPIO.HIGH)
    time.sleep(0.1)
    if Test:
        print(characters[idx])
    else:
        checknum(characters[idx], numberrr)
    set_screen(characters[idx])
    GPIO.output(25, GPIO.LOW)
    GPIO.output(line, GPIO.LOW)

#Main loop
try:
    if input("test?") == "Y":
        Test = True
    setup(funnyword, score)
    numberrr = str(selectionlist[random.randrange(-1,16)])
    set_screen(numberrr)
    print(numberrr)
    while True:
        readLine(L1, ["1","2","3","A"])
        readLine(L2, ["4","5","6","B"])
        readLine(L3, ["7","8","9","C"])
        readLine(L4, ["*","0","#","D"])
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nApplication stopped!")
