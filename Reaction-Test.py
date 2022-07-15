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
    
def zero():
    off()
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(21, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(20, GPIO.HIGH)
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(5, GPIO.HIGH) 

def one():
    off()
    GPIO.output(bottomright, GPIO.HIGH)
    GPIO.output(topright, GPIO.HIGH)

def two():
    off()
    GPIO.output(top, GPIO.HIGH)
    GPIO.output(topright, GPIO.HIGH)
    GPIO.output(middle, GPIO.HIGH)
    GPIO.output(bottomleft, GPIO.HIGH)
    GPIO.output(bottom, GPIO.HIGH)

def three():
    off()
    GPIO.output(top, GPIO.HIGH)
    GPIO.output(middle, GPIO.HIGH)
    GPIO.output(bottom, GPIO.HIGH)
    GPIO.output(topright, GPIO.HIGH)
    GPIO.output(bottomright, GPIO.HIGH)

def four():
    off()
    GPIO.output(middle, GPIO.HIGH)
    GPIO.output(topleft, GPIO.HIGH)
    GPIO.output(topright, GPIO.HIGH)
    GPIO.output(bottomright, GPIO.HIGH)

def five():
    off()
    GPIO.output(middle, GPIO.HIGH)
    GPIO.output(top, GPIO.HIGH)
    GPIO.output(bottom, GPIO.HIGH)
    GPIO.output(topleft, GPIO.HIGH)
    GPIO.output(bottomright, GPIO.HIGH)

def six():
    GPIO.output(middle, GPIO.HIGH)
    GPIO.output(top, GPIO.HIGH)
    GPIO.output(topleft, GPIO.HIGH)
    GPIO.output(bottomleft, GPIO.HIGH)
    GPIO.output(bottom, GPIO.HIGH)
    GPIO.output(bottomright, GPIO.HIGH)

def seven():
    off()
    GPIO.output(top, GPIO.HIGH)
    GPIO.output(topright, GPIO.HIGH)
    GPIO.output(bottomright, GPIO.HIGH)

def eight():
    off()
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(21, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(20, GPIO.HIGH)
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(middle, GPIO.HIGH)

def nine():
    off()
    GPIO.output(top, GPIO.HIGH)
    GPIO.output(middle, GPIO.HIGH)
    GPIO.output(bottom, GPIO.HIGH)
    GPIO.output(topright, GPIO.HIGH)
    GPIO.output(bottomright, GPIO.HIGH)
    GPIO.output(topleft, GPIO.HIGH)

def ast():
    off()
    GPIO.output(period, GPIO.HIGH)

def hasht():
    off()
    GPIO.output(topright, GPIO.HIGH)
    GPIO.output(bottomright, GPIO.HIGH)
    GPIO.output(middle, GPIO.HIGH)
    GPIO.output(topleft, GPIO.HIGH)
    GPIO.output(bottomleft, GPIO.HIGH)

def a():
    off()
    GPIO.output(bottomleft, GPIO.HIGH)
    GPIO.output(bottomright, GPIO.HIGH)
    GPIO.output(topleft, GPIO.HIGH)
    GPIO.output(topright, GPIO.HIGH)
    GPIO.output(middle, GPIO.HIGH)
    GPIO.output(top, GPIO.HIGH)
    GPIO.output(period, GPIO.HIGH)

def c():
    off()
    GPIO.output(bottomleft, GPIO.HIGH)
    GPIO.output(topleft, GPIO.HIGH)
    GPIO.output(bottom, GPIO.HIGH)
    GPIO.output(top, GPIO.HIGH)
    GPIO.output(period, GPIO.HIGH)

def b():
    off()
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(middle, GPIO.HIGH)
    GPIO.output(period, GPIO.HIGH)

def d():
    off()
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(21, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(20, GPIO.HIGH)
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(period, GPIO.HIGH)

#7 segment display changer
def setscr(target):
    if target == "0":
        zero()
    if target == "1":
        one()
    if target == "2":
        two()
    if target == "3":
        three()
    if target == "4":
        four()
    if target == "5":
        five()
    if target == "6":
        six()
    if target == "7":
        seven()
    if target == "8":
        eight()
    if target == "9":
        nine()
    if target == "hasht":
        hasht()
    if target == "ast":
        ast()
    if target == "A":
        a()
    if target == "B":
        b()
    if target == "C":
        c()
    if target == "D":
        d()

#Checks if you did the right input and handles it
def checknum(inputt, target, scoe):
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
    if(GPIO.input(C1) == 1):
        GPIO.output(25, GPIO.HIGH)
        time.sleep(0.1)
        if characters[0] == "1":
            checknum("1", numberrr, score)
            GPIO.output(25, GPIO.LOW)
        elif characters[0] == "4":
            checknum("4", numberrr, score)
            GPIO.output(25, GPIO.LOW)
        elif characters[0] == "7":
            checknum("7", numberrr, score)
            GPIO.output(25, GPIO.LOW)
        else:
            checknum("ast", numberrr, score)
            GPIO.output(25, GPIO.LOW)
    if(GPIO.input(C2) == 1):
        GPIO.output(25, GPIO.HIGH)
        time.sleep(0.1)
        if characters[1] == "2":
            checknum("2", numberrr, score)
            GPIO.output(25, GPIO.LOW)
        elif characters[1] == "5":
            checknum("5", numberrr, score)
            GPIO.output(25, GPIO.LOW)
        elif characters[1] == "8":
            checknum("8", numberrr, score)
            GPIO.output(25, GPIO.LOW)
        else:
            checknum("0", numberrr, score)
            GPIO.output(25, GPIO.LOW)
    if(GPIO.input(C3) == 1):
        GPIO.output(25, GPIO.HIGH)
        time.sleep(0.1)
        if characters[2] == "3":
            checknum("3", numberrr, score)
            GPIO.output(25, GPIO.LOW)
        elif characters[2] == "6":
            checknum("6", numberrr, score)
            GPIO.output(25, GPIO.LOW)
        elif characters[2] == "9":
            checknum("9", numberrr, score)
            GPIO.output(25, GPIO.LOW)
        else:
            checknum("hasht", numberrr, score)
            GPIO.output(25, GPIO.LOW)
    if(GPIO.input(C4) == 1):
        GPIO.output(25, GPIO.HIGH)
        time.sleep(0.1)
        if characters[3] == "A":
            checknum("A", numberrr, score)
            GPIO.output(25, GPIO.LOW)
        elif characters[3] == "B":
            checknum("B", numberrr, score)
            GPIO.output(25, GPIO.LOW)
        elif characters[3] == "C":
            checknum("C", numberrr, score)
            GPIO.output(25, GPIO.LOW)
        else:
            checknum("D", numberrr, score)
            GPIO.output(25, GPIO.LOW)
    GPIO.output(line, GPIO.LOW)

#Main loop
try:
    setup(funnyword, score)
    numberrr = str(selectionlist[random.randrange(-1,16)])
    setscr(numberrr)
    print(numberrr)
    for i in range(0,50):
        readLine(L1, ["1","2","3","A"])
        readLine(L2, ["4","5","6","B"])
        readLine(L3, ["7","8","9","C"])
        readLine(L4, ["*","0","#","D"])
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nApplication stopped!")
