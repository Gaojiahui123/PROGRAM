from tkinter import *
import serial
import time

root=Tk()
root.title('LED Window')

ArduinoSerial = serial.Serial('com4',9600)
time.sleep(0.1)

lab = Label(root, width='70', height='5', text='Press button', bg='white')
lab.pack()

button1 = Button(root, width='25', height='3', text='ON', bg='green', command=lambda:on())
button1.pack()

button2 = Button(root, width='25', height='3', text='OFF', bg='red', command=lambda:off())
button2.pack()

def on():
    ArduinoSerial.write(b'1')
    print('LED turned ON')

def off():
    ArduinoSerial.write(b'0')
    print('LED turned OFF')

root.mainloop()