import RPi.GPIO as GPIO
from tkinter import *

root = Tk()
root.title("RC Driver")
root.geometry("300x200")

# servo TowerPro SG90 or SG92R
freq = 50.0
deg_min = 0.0
deg_max = 180.0
dc_min = 5.0
dc_max = 10.0

# motor driver GVS output 12, 18, 22, 31
servo = 31

# speed and direction configuration
spd = IntVar()
spd.set(0)

leftForward = 36
leftReverse = 35
rightForward = 33
rightReverse = 32

def init():
    global p, LF, LR, RF, RR

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(servo, GPIO.OUT)
    p = GPIO.PWM(servo, freq)
    p.start(0)

    GPIO.setup(leftForward, GPIO.OUT)
    LF = GPIO.PWM(leftForward, 20)
    LF.start(0)

    GPIO.setup(leftReverse, GPIO.OUT)
    LR = GPIO.PWM(leftReverse, 20)
    LR.start(0)

    GPIO.setup(rightForward, GPIO.OUT)
    RF = GPIO.PWM(rightForward, 20)
    RF.start(0)

    GPIO.setup(rightReverse, GPIO.OUT)
    RR = GPIO.PWM(rightReverse, 20)
    RR.start(0)

def convert_dc(degree):
    dc = ((float(degree) - deg_min) * (dc_max - dc_min) / (deg_max - deg_min) + dc_min)
    p.ChangeDutyCycle(dc)

def forward(speed):
    LF.ChangeDutyCycle(speed)
    LR.ChangeDutyCycle(0)
    RF.ChangeDutyCycle(speed)
    RR.ChangeDutyCycle(0)
    LF.ChangeFrequency(speed + 5)
    RF.ChangeFrequency(speed + 5)

def reverse(speed):
    LF.ChangeDutyCycle(0)
    LR.ChangeDutyCycle(speed)
    RF.ChangeDutyCycle(0)
    RR.ChangeDutyCycle(speed)
    LR.ChangeFrequency(speed + 5)
    RR.ChangeFrequency(speed + 5)

def stop():
    LF.ChangeDutyCycle(0)
    LR.ChangeDutyCycle(0)
    RF.ChangeDutyCycle(0)
    RR.ChangeDutyCycle(0)

def change_spd(s):
    if(spd.get() > 0):
        forward(spd.get())
        lblSpeed.config(text = 'Forward = %.2f' % spd.get())
    elif(spd.get() == 0):
        stop()
        lblSpeed.config(text = 'Stop')
    elif(spd.get() < 0):
        reverseSpeed = spd.get() * -1
        reverse(reverseSpeed)
        lblSpeed.config(text = 'Reverse = %.2f' % reverseSpeed)

def cleanup():
    GPIO.cleanup()

init()

pw = PanedWindow(root)
pw.pack(expand = True, fill = BOTH)

f1 = Frame(pw)

lblSteer = Label(f1, text = 'Steering Wheel')
lblSteer.pack(pady = 35)

steerSlider = Scale(f1, length = 130, orient = 'h', from_ = -180.0, to = 180.0, showvalue = False, command = convert_dc)
steerSlider.pack()

f2 = Frame(pw)

spdSlider = Scale(f2, length = 160, orient = 'v', from_ = -100, to = 100, showvalue = False, variable = spd, command = change_spd)
spdSlider.pack()

lblSpeed = Label(f2, text = 'Speed = %.2f' % spd.get())
lblSpeed.pack(pady = 10)

pw.add(f1)
pw.add(f2)

root.mainloop()

cleanup()
