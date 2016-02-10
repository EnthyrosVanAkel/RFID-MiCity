import re, sys, signal, os, time, datetime
import serial
import OSC


URL = '127.0.0.1'
PORT = 57120
BITRATE = 9600


def send_message(message):
	cliente = OSC.OSCClient()
	cliente.connect((URL,PORT))
	oscmsg = OSC.OSCMessage()
	oscmsg.setAddress("/checkout")
	oscmsg.append(message)
	cliente.send(oscmsg)



if __name__ == '__main__':
    buffer = ''
    ser = serial.Serial('/dev/ttyUSB0', BITRATE, timeout=0)
     rfidPattern = re.compile(b'[\W_]+')

    while True:
      # Read data from RFID reader
      buffer = buffer + ser.readline(ser.inWaiting())
      if '\n' in buffer:
        lines = buffer.split('\n')
        last_received = lines[-2]
        match = rfidPattern.sub('', last_received)
        print last_received
        send_message(last_received)
        buffer = ''
        lines = ''