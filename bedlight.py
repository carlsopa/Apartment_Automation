import paho.mqtt.client as mqtt
import time

Client = mqtt.Client()

Client.connect('192.168.1.172', 1883, 0)
Client.publish('bedroom/lights','left')
print('hello PAUL')
