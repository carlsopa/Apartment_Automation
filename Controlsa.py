#using mqtt messaging basic communication to the different light fixtures around the apartment.
import paho.mqtt.client as mqtt
import time

Server = '192.168.1.172'
client = mqtt.Client()
#used to publish on/off messages to the bedroom lights.
class Bedroom(object):

    def __init__(self):
        client.connect(Server, 1883, 60)
        client.loop_start()

    def Lights(self,x):
        print(x)
        client.publish('/Apartment/Bedroom/Lights',x)
#used to publish messages to the chandelier
class Chandelier(object):

    def __init__(self):
        client.connect(Server, 1883, 60)
        client.loop_start()

    def ChandelierControl(self,x):
        client.publish('/Apartment/LivingRoom/Chandelier',x)
