from serial import Serial
import time
import re
import subprocess

def get_device():
    device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
    df = subprocess.check_output("lsusb")
    devices = []
    for i in str(df).split('\\n'):
        if i:
            info = device_re.match(i)
            if info:
                dinfo = info.groupdict()
                dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
                devices.append(dinfo)

    return next(item for item in devices if item["tag"] == "Linux Foundation 2.0 root hub")

if __name__ == '__main__':
    dataString = ''
    a = 0
    dev = get_device()['device']
    ser = Serial(port='/dev/ttyAMA0', baudrate=9600, write_timeout=10)

    print('Devices: {dev}'.format(dev=dev))

    while True:
        a = a+1  # a value increase every loop
        dataString = bytearray(a); # convert a value to hexa
        print(dataString)
        ser.write(dataString)  # send the data
        time.sleep(2)  # give the loop a break

