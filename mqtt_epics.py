#!/usr/bin/env python

###
## Bridge between EPICS and MQTT
####################################

from pcaspy import Driver, SimpleServer 
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
from pyxtension.Json import Json
from epicsDefinition import *
import variables as var
from epicsDriver import *

###
# MQTT brocker and topics
###
MQTT_SERVER = "129.129.130.80"
MQTT_TOPIC_01 = "dataV"
MQTT_TOPIC_02 = "dataP"
MQTT_TOPIC_03 = "dataC"
MQTT_TOPIC_04 = "dataL"

if __name__ == '__main__':
    server = SimpleServer()
    server.createPV(prefix, pvdb)
    driver = myDriver()


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_TOPIC_01)
    client.subscribe(MQTT_TOPIC_02)
    client.subscribe(MQTT_TOPIC_03)
    client.subscribe(MQTT_TOPIC_04)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    #DATAP
    if msg.topic == MQTT_TOPIC_02:
        dataP = Json(str(msg.payload))
	var.ppc = float(dataP.dataP.pressurePC)
        var.ppv = float(dataP.dataP.pressurePV)

    #DATAV
    elif msg.topic == MQTT_TOPIC_01:
        dataV = Json(str(msg.payload))
	var.V1 = int(dataV.dataV.V1)
        var.V2 = int(dataV.dataV.V2)
        var.V3 = int(dataV.dataV.V3)
        var.V4 = int(dataV.dataV.V4)
        var.V5 = int(dataV.dataV.V5)
        var.V6 = int(dataV.dataV.V6)
        var.V7 = int(dataV.dataV.V7)
        var.V8 = int(dataV.dataV.V8)

    #DATAC
    elif msg.topic == MQTT_TOPIC_03:
        dataC = Json(str(msg.payload))
	var.ic = int(dataC.dataC.IC)
        var.gas1 = int(dataC.dataC.gas1)
        var.gas2 = int(dataC.dataC.gas2)
        var.pgas1 = int(dataC.dataC.pgas1)
        var.pgas2 = int(dataC.dataC.pgas2)
	var.cycle = int(dataC.dataC.zyklusnr)
        var.actcycle = int(dataC.dataC.actzyklus)
	var.status = int(dataC.dataC.status)
	var.setpoint = float(dataC.dataC.setpoint)

    #DATAL
    elif msg.topic == MQTT_TOPIC_04:
        dataL = Json(str(msg.payload))
	for x in range(len(dataL.dataL.pcGM)):
    		var.list[x] = dataL.dataL.pcGM[x]
    else:
        print("unknown topic: "+msg.topic)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_SERVER, 1883, 60)
client.loop_start()
#client.loop_forever()

while True:
	server.process(0.1)
