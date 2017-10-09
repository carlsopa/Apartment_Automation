import paho.mqtt.client as mqtt
import time

Bedroom_lights = '192.168.1.172'
Bedroom_Alarmclock = '192.168.1.161'
Livingroom_Chandelier = '192.168.1.172'

client = mqtt.Client()

#def on_message(client, userdata, message):
#    print("message: ",str(message.payload.decode("utf-8")))

class Chandelier(object):
    def __init__(self):
        client.connect(Livingroom_Chandelier, 1883, 0)
        client.loop_start()

class Bedroom_Light(object):
    

    def __init__(self):
        client.connect(Bedroom_lights, 1883, 60)
        #client.on_connect = on_connect
        #client.on_message = on_message
        client.loop_start()

    def on_message(client, userdata, message):
        print("message: ",str(message.payload.decode("utf-8")))
    
    def on_connect(client, userdata, flags, rc):
        print('connected')
        client.subscribe('/Apartment/Bedroom/Lights/Status/left')
        client.subscribe('/Apartment/Bedroom/Lights/Status/right')

    def Lights(self,x):
        client.publish('/Apartment/Bedroom/Lights',x)
        print('goofy me')

    def LightsStatus(self):
        print('Lights Status')
        #client.on_connect = on_connect()
        client.on_message = on_message
        
