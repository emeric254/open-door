# -*- coding: utf-8 -*-

import sys
import serial

port = '/dev/ttyACM0'
baudrate = '9600'


class Arduino:

    def __init__(self):
        try:
            self.ser = serial.Serial(port, baudrate)
        except serial.SerialException:
            print('Can\'t open' + port + '@' + baudrate, file=sys.stderr)
            return

    def send_msg(self, msg: str):
        try:
            self.ser.write((msg + '\n').encode('utf-8'))
        except serial.portNotOpenError:
            print('Can\'t send «' + msg + '» to ' + port + '@' + baudrate + ', the port is not open', file=sys.stderr)
            return

    def wait_answer(self, wanted: str = ''):
        response = ''
        try:
            while response != wanted:
                try:
                    response = self.ser.readline().decode().strip()
                    if response:
                        print('«' + response + '»')
                except serial.portNotOpenError:
                    print('Can\'t read from ' + port + '@' + baudrate + ', the port is not open', file=sys.stderr)
        except KeyboardInterrupt:
            pass
