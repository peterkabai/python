import serial

ser = serial.Serial('/dev/tty.Bluetooth-Incoming-Port')  # open serial port
print(ser.name)         # check which port was really used
#ser.write(b'hello')     # write a string
#ser.close() 

with serial.Serial('/dev/ttyS1', 19200, timeout=1) as ser:
    line = ser.readline()
    print(line)