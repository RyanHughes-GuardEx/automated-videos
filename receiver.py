from serial import Serial
import time

def setup():
    Serial.begin(9600) # Starting serial communication


if __name__ == '__main__':
    dataString = ''
    a = 0

    while True:
        a = a+1  # a value increase every loop
        # print(dataString, "%02X", a); # convert a value to hexa
        print(a)
        print(dataString)
        Serial.println(dataString)  # send the data
        time.sleep(2)  # give the loop a break

