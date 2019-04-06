from grovepi import *
from grove_rgb_lcd import *
from time import sleep
from math import isnan
import os
import requests
import grovepi
import sqlite3
import configparser

#config.ini
config = configparser.ConfigParser(allow_no_value=True)
config.read('config.ini')
config.sections()
if 'dweet' not in config:
	print("dweetName not found")
	exit()
    
dweetName = config.get('dweet', 'dweetName')
print("dweetName")
    
conn = sqlite3.connect('database.db')
c = conn.cursor()


#Dweet.io
dweetIO = "https://dweet.io/dweet/for/"
myName =  dweetName #"yourthingID"
soundKey = "Sound_Level"

# Connect the Grove Sound Sensor to analog port A0
sound_sensor = 0

grovepi.pinMode(sound_sensor,"INPUT")

dht_sensor_port = 7 # Temp and Hum port
dht_sensor_type = 0 # use 0 for the blue-colored sensor and 1 for the white-colored sensor
sound_sensor = 0
sound_value = grovepi.analogRead(sound_sensor)
print("Sound Level =", sound_value)
      
        
#Save to DB
c.execute('INSERT INTO readings(sound) VALUES(?)',(sound_value,))
conn.commit()

        
#Send to Cloud, dweet.io
soundString = dweetIO+myName+'?'+soundKey+'='+str(sound_value)
print(soundString)
rqs3 = requests.get(soundString)
       
conn.close()
