import time
from pyvlcclient.vlcclient import VLCClient

vlc = VLCClient("::1")
vlc.connect()

vlc.clear()
vlc.loop()         # ToDo: need to ensure this stays toggled off
vlc.add("videos/eyevideo.avi")

time.sleep(5)
vlc.pause()
time.sleep(2)
vlc.play()
time.sleep(7)
print(vlc.info())
vlc.stop()
vlc.disconnect()
