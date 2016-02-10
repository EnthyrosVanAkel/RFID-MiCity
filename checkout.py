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

    while True:
      # Read data from RFID reader
      buffer = buffer + ser.read(ser.inWaiting())
      if '\n' in buffer:
        lines = buffer.split('\n')
        print lines
        send_message(lines  )