from win32api import keybd_event, MapVirtualKey
import json
import serial
import time

with open('codes.json', 'r') as f:
    codes = json.load(f)

with open('sequences.json', 'r') as f:
    sequences = json.load(f)

def press_key(key):
    print("Pressing "+key)
    keycode = int(codes[key],16)
    keybd_event(keycode, MapVirtualKey(keycode,0))

def press_sequence(sequence):
    print("Pressing sequence " + sequence + ": ",end="")
    for key in sequences[sequence]:
        print(key+", ",end="")
        keycode = int(codes[key],16)
        keybd_event(keycode,MapVirtualKey(keycode,0),0,0) # press
    print("")
    time.sleep(0.3)

    for key in sequences[sequence][::-1]:
        keycode = int(codes[key],16)
        keybd_event(keycode,MapVirtualKey(keycode,0),2,0) # release
    
        
    


ser_port = serial.Serial(port="COM10",baudrate=9600)
while 1:
    try:
        key = ser_port.readline().decode("utf-8").replace("\r","").replace("\n","")
        if key in codes.keys():
            press_key(key)
        elif key in sequences.keys():
            press_sequence(key)
        else:
            print("Invalid key "+key)
            
    except KeyboardInterrupt:
        ser_port.close()
        break

