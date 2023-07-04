# -*- coding: utf-8 -*-
# @Time    : 2023/7/4 15:42
# @Author  : yangyuexiong
# @Email   : yang6333yyx@126.com
# @File    : pub_and_sub.py
# @Software: PyCharm


import paho.mqtt.client as mqtt
import time
import json

from mqtt5_example import username, password

received_message = None


def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d" % rc)


def on_publish(client, userdata, mid):
    print("Message Published")


def on_message(client, userdata, msg):
    print("Received message: " + str(msg.payload.decode("utf-8")))
    global received_message
    received_message = str(msg.payload.decode("utf-8"))


broker_address = "192.168.9.2"

client = mqtt.Client("9c9fb71c402b4a4db3b80ec44cef96ca", protocol=mqtt.MQTTv5)
client.on_connect = on_connect
client.on_publish = on_publish
client.on_message = on_message
client.username_pw_set(username, password)
client.connect(broker_address)
client.loop_start()


def run():
    """run"""
    d = {
        "sn": "9c9fb71c402b4a4db3b80ec44cef96ca"
    }
    message = json.dumps(d, ensure_ascii=False)
    while not received_message:
        rc, mid = client.publish("v1/gateway/9c9fb71c402b4a4db3b80ec44cef96ca/sub/get/request", message)
        time.sleep(1)
        print(rc, mid)
        if received_message:
            print(received_message)
            break


if __name__ == '__main__':
    run()
