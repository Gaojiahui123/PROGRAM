import xlwt
import time
import serial

ser = serial.Serial( #读取参数
    port='COM3',
    baudrate=74880,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)
data = ''
a_x = 0
a_y = 0
a_z = 0
r_x = 0
r_y = 0
r_z = 0
m_x = 0
m_y = 0
m_z = 0
tt = 0

workbook = xlwt.Workbook(encoding = 'utf-8')#创建excel，设定编码
worksheet = workbook.add_sheet('Data')#创建sheet
worksheet.write(0,0, label = 'Time')#写入标题
worksheet.write(0,1, label = 'xAccel')
worksheet.write(0,2, label = 'yAccel')
worksheet.write(0,3, label = 'zAccel')
worksheet.write(0,4, label = 'xGyro')
worksheet.write(0,5, label = 'yGyro')
worksheet.write(0,6, label = 'zGyro')
worksheet.write(0,7, label = 'xMag')
worksheet.write(0,8, label = 'yMag')
worksheet.write(0,9, label = 'zMag')

while True:
    data = ser.readline()#读取串口数据
    data = str(data)

    if '-----' in data:
        continue
    try:
        line = data.split(" ")[1].split("\\")[0].split(",") #分离参数
    except:
        continue
    if 'Accl' in data: #将各个参数写入excel
        try :
            tt += 1
            time_now = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            worksheet.write(tt, 0, label=time_now)
            a_x += 1
            worksheet.write(a_x,1, label = float(line[0]))
        except:
            worksheet.write(a_x,1, label= '')#出错时写入''
        try :
            a_y += 1
            worksheet.write(a_y,2, label = float(line[1]))
        except:
            worksheet.write(a_y,2, label= '')
        try :
            a_z += 1
            worksheet.write(a_z,3, label = float(line[2]))
        except:
            worksheet.write(a_z,3, label= '')
    if 'Gyro' in data:
        try :
            r_x += 1
            worksheet.write(r_x,4, label = float(line[0]))
        except:
            worksheet.write(r_x,4, label= '')
        try :
            r_y += 1
            worksheet.write(r_y,5, label = float(line[1]))
        except:
            worksheet.write(r_y,5, label= '')
        try :
            r_z += 1
            worksheet.write(r_z,6, label = float(line[2]))
        except:
            worksheet.write(r_z,6, label= '')
    if 'Mag' in data:
        try :
            m_x += 1
            worksheet.write(m_x,7, label = float(line[0]))
        except:
            worksheet.write(m_x,7, label= '')
        try :
            m_y += 1
            worksheet.write(m_y,8, label = float(line[1]))
        except:
            worksheet.write(m_y,8, label= '')
        try :
            m_z += 1
            worksheet.write(m_z,9, label = float(line[2]))
        except:
            worksheet.write(m_z,9, label= '')

        workbook.save('data01.xls')#保存excel