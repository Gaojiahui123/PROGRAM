from tkinter import *
import serial
import time

root=Tk()
root.title('LED Control')

ArduinoSerial = serial.Serial('com5',9600)
time.sleep(0.1)

lab1 = Label(root, width='25', height='5', text='LED 1', bg='white',)
lab1.grid(column = 1, row = 1)

lab2 = Label(root, width='25', height='5', text='LED 2', bg='white',)
lab2.grid(column = 2, row = 1)

LED1_ON = Button(root, width='25', height='3', text='ON', bg='green', command=lambda:on1())
LED1_ON.grid(column = 1, row = 2)

LED1_OFF = Button(root, width='25', height='3', text='OFF', bg='red', command=lambda:off1())
LED1_OFF.grid(column = 1, row = 3)

LED1_Blink = Button(root, width='25', height='3', text='Blink', bg='yellow', command=lambda:blink1())
LED1_Blink.grid(column = 1, row = 4)

LED2_ON = Button(root, width='25', height='3', text='ON', bg='green', command=lambda:on2())
LED2_ON.grid(column = 2, row = 2)

LED2_OFF = Button(root, width='25', height='3', text='OFF', bg='red', command=lambda:off2())
LED2_OFF.grid(column = 2, row = 3)

LED2_Blink = Button(root, width='25', height='3', text='Blink', bg='yellow', command=lambda:blink2())
LED2_Blink.grid(column = 2, row = 4)

def on1():
    ArduinoSerial.write(b'1')

def off1():
    ArduinoSerial.write(b'0')

def blink1():
    ArduinoSerial.write(b'2')

def on2():
    ArduinoSerial.write(b'4')

def off2():
    ArduinoSerial.write(b'3')

def blink2():
    ArduinoSerial.write(b'5')

root.mainloop()