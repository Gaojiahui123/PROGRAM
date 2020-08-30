from tkinter import *
from tkinter import ttk
import serial
import time

root=Tk()
root.title('LED Control')

ArduinoSerial = serial.Serial('com5',9600)
time.sleep(0.1)

lab_power = Label(root, width='25', height='3', text='Power', bg='white',)
lab_power.grid(column = 1, row = 1)

Divider = Label(root, height='2')
Divider.grid(column = 1, row = 2, columnspan=3)

lab_sleep = Label(root, width='25', height='3', text='Sleep', bg='white',)
lab_sleep.grid(column = 1, row = 3)

lab_air = Label(root, width='25', height='3', text='Air', bg='white',)
lab_air.grid(column = 2, row = 3)

lab_calib = Label(root, width='25', height='3', text='Calibration(times)', bg='white',)
lab_calib.grid(column = 3, row = 3)

lab_delay = Label(root, width='25', height='3', text='Delay', bg='white',)
lab_delay.grid(column = 4, row = 3)

power_butt = Button(root, width='25', height='3', text='ON', bg='white', command=lambda:power())
power_butt.grid(column = 2, row = 1)

sleep_butt = Button(root, width='25', height='3', text='ON', bg='white', command=lambda:sleep())
sleep_butt.grid(column = 1, row = 4)

air_butt = Button(root, width='25', height='3', text='ON', bg='white', command=lambda:air())
air_butt.grid(column = 2, row = 4)

calib_butt = Button(root, width='25', height='3', text='Start', bg='white', command=lambda:calib())
calib_butt.grid(column = 3, row = 5)

delay_butt = Button(root, width='25', height='3', text='confirm', bg='white', command=lambda:delay())
delay_butt.grid(column = 4, row = 5)

calib_value = StringVar()
calib_box = ttk.Combobox(root, textvariable= calib_value)  # 初始化
calib_box["values"] = (1, 2, 3)
calib_box.current(0)
calib_box.grid(column = 3, row = 4)

delay_value = StringVar()
delay_box = ttk.Combobox(root, textvariable= delay_value)  # 初始化
delay_box["values"] = (0, 150, 300)
delay_box.current(0)
delay_box.grid(column = 4, row = 4)

def power():
    if power_butt['text'] == 'ON':
        power_butt['text'] = 'OFF'
        power_butt['bg'] = 'green'
        ArduinoSerial.write(b'1')
    else:
        power_butt['text'] = 'ON'
        power_butt['bg'] = 'white'
        ArduinoSerial.write(b'2')

def sleep():
    if sleep_butt['text'] == 'ON':
        sleep_butt['text'] = 'OFF'
        sleep_butt['bg'] = 'green'
        ArduinoSerial.write(b'3')
    else:
        sleep_butt['text'] = 'ON'
        sleep_butt['bg'] = 'white'
        ArduinoSerial.write(b'4')

def air():
    if air_butt['text'] == 'ON':
        air_butt['text'] = 'OFF'
        air_butt['bg'] = 'green'
        ArduinoSerial.write(b'5')
    else:
        air_butt['text'] = 'ON'
        air_butt['bg'] = 'white'
        ArduinoSerial.write(b'6')

def calib():
    if calib_value.get() == '1': ArduinoSerial.write(b'7')
    elif calib_value.get() == '2': ArduinoSerial.write(b'8')
    elif calib_value.get() == '3':ArduinoSerial.write(b'9')

def delay():
    if delay_value.get() == '0': ArduinoSerial.write(b'a')
    elif delay_value.get() == '150': ArduinoSerial.write(b'b')
    elif delay_value.get() == '300': ArduinoSerial.write(b'c')


root.mainloop()