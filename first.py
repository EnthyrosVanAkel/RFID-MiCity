import serial
serial = serial.Serial("/dev/ttyAMA0", baudrate=9600)

code = ''

while True:
    data = serial.read()
    if data == '\r':
        print(code)
        code = ''
    else:
        code = code + data