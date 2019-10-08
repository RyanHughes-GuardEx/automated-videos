import time
from pyvlcclient.vlcclient import VLCClient

vlc = VLCClient("::1")
vlc.connect()

vlc.clear()
vlc.loop()         # ToDo: need to ensure this stays toggled off
vlc.add("videos/eyevideo.avi")

time.sleep(15)
print(vlc.info())
vlc.stop()
vlc.disconnect()
