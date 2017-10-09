import paho.mqtt.client as mqtt
from time import *

def on_message(client, userdata, msg):
    MsgStr = str(msg.payload.decode("utf-8"))
    print(MsgStr)

client = mqtt.Client()
clienta = mqtt.Client()

client.on_message = on_message
clienta.on_message = on_message

client.subscribe('/Foo/Bar/Example/')
clienta.subscribe('/Foo/Bar/Example/Test/')

client.connect('192.168.1.172',1883,0)
clienta.connect('192.168.1.172',1883,0)

while True:
    client.loop_start()
    #clienta.loop_start()
