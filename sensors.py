import paho.mqtt.client as mqtt
from time import *
#setup initial definitions for the mqtt.client
def on_connect(client, userdata, flags, rc):
    client.subscribe('/Apartment/Sensors/Alarm/FrontDoor')
    client.subscribe('/Apartment/Sensors/Control/Temp')
def on_message(client, userdata, msg):
    MsgStr = str(msg.payload.decode("utf-8"))
    print(msg.topic+" "+MsgStr)
#using mqtt.message_callback_add: define the different sensors around the apartment and what they will do
def FrontDoor(mosq, onj, msg):
    print('front door change')
def TempSensor(mosq, obj, msg):
    print('temp sensor change')

client = mqtt.Client()
client.message_callback_add('/Apartment/Sensors/Alarm/FrontDoor', FrontDoor)
client.message_callback_add('/Apartment/Sensors/Control/Temp', TempSensor)
#client.on_connect = on_connect
client.on_message = on_message
client.connect('192.168.1.172',1883,0)
client.subscribe('/Apartment/Sensors/#')

while True:
    client.loop_start()
