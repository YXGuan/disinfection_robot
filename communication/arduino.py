#!/usr/bin/env python3
import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.flush()

    while True:
        ser.write(b"1\n")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(1)

'''
import serial
ser = serial.Serial('/dev/ttyUSB0',9600)  #/dev/ttyUSB0

while True:
    read_serial=ser.readline()
    print(read_serial)
    '''