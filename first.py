#!/usr/bin/env python
import time
import sys

card = '0019171125'        # Stored good card number consider using a list or a file.

def main():                # define a main function.
    while True:            # loop until the program encounters an error.
        sys.stdin = open('/dev/tty0', 'r')
        RFID_input = input()            
        if RFID_input == card:      # compare the stored number to the input and if True execute code.
            print "Access Granted" 
            print "Read code from RFID reader:{0}".format(RFID_input)
        else:                    # and if the condition is false excecute this code.
            print "Access Denied"

# where is tty defined??
            tty.close()

if __name__ == '__main__':
    main()