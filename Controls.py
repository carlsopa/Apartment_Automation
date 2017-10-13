#Using paho mqtt I send string messages to my different boards and sensors.
#They are then controlled by what message they receive
import paho.mqtt.client as mqtt
import time

Server = '192.168.1.172'
client = mqtt.Client()

class Bedroom(object):

    def __init__(self):
        client.connect(Server, 1883, 60)
        client.loop_start()

    def Lights(self,x):
        print(x)
        client.publish('/Apartment/Bedroom/Lights',x)

class Chandelier(object):

    def __init__(self):
        client.connect(Server, 1883, 60)
        client.loop_start()

    def ChandelierControl(self,x):
        client.publish('/Apartment/LivingRoom/Chandelier',x)
