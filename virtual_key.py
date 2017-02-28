from win32api import keybd_event, MapVirtualKey
import json
import serial

with open('codes.json', 'r') as fp:
    codes = json.load(fp)

def press_key(key):
    print("Pressing "+key)
    keybd_event(int(codes[key],16), MapVirtualKey(int(codes[key],16),0))


ser_port = serial.Serial(port="COM10",baudrate=9600)
while 1:
    try:
        key = ser_port.readline().decode("utf-8").replace("\r","").replace("\n","")
        if key in codes.keys():
            press_key(key)
        else:
            print("Invalid key "+key)
    except KeyboardInterrupt:
        ser_port.close()
        break
