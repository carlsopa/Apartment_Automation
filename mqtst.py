import paho.mqtt.client as mqtt
import time
from Controlsa import *



def on_message(client, userdata, msg):
    print('on message')
    print('message received: ',str(msg.payload.decode("utf-8")))
    print('message topic: ',msg.topic)
    global tst
    tst = str(msg.payload.decode("utf-8"))
    print(str(msg.payload.decode("utf-8")))
server = '192.168.1.172'
print('start')
client = mqtt.Client()
clienta = mqtt.Client()
clienta.on_message = on_message
client.connect('192.168.1.172',1883,0)
clienta.connect('192.168.1.172',1883,0)
client.loop_start()
clienta.loop_start()
print('subscribing')
clienta.subscribe('/Apartment/Bedroom/Lights/Status/right')
print('publishing')
client.publish('/Apartment/Bedroom/Lights/Status/right','right')
time.sleep(4.0)
#print(tst)
