# -*- coding: utf-8 -*-
# @Time    : 2023/7/3 17:51
# @Author  : yangyuexiong
# @Email   : yang6333yyx@126.com
# @File    : mqtt5_subscriber.py
# @Software: PyCharm
import time

import paho.mqtt.client as mqtt

from mqtt5_example import *

from mqtt5_publisher import mqtt5_publish


# 连接回调函数
def on_connect(client, userdata, flags, rc, properties=None):
    """连接成功,回调该方法"""

    if rc == 0:
        print("Subscriber Connected to MQTT Broker!", rc)
        # 订阅主题
        client.subscribe("v1/gateway/9c9fb71c402b4a4db3b80ec44cef96ca/sub/get/respond", 1)
    else:
        print("Failed to connect, return code %d" % rc)


# 消息接收回调函数
def on_message(client, userdata, message, properties):
    """订阅到消息,回调该方法"""

    print(f"主题:{message.topic}, 消息:", message.payload)
    # received_message = message.payload.decode()
    # print("Received message: %s" % received_message)

    # 进行回复
    # response_message = "Received your message: " + received_message
    # client.publish(topic, response_message, qos=1, retain=False)
    # print("Response sent:", response_message)


def mqtt5_connect():
    """连接MQTT服务器"""

    client = mqtt.Client(client_id=f"{client_id}{int(time.time())}", protocol=mqtt.MQTTv5)
    client.on_connect = on_connect  # 设置连接回调函数
    client.on_message = on_message  # 设置订阅消息回调函数
    client.username_pw_set(username, password)  # 设置用户名和密码
    client.connect(broker_address, port=broker_port)  # 连接到MQTT代理
    client.loop_start()  # 开启MQTT的网络循环
    return client


def on_subscribe():
    """订阅主题"""

    print('启动订阅...')
    client = mqtt5_connect()
    # client.subscribe(topic, 2)
    while True:
        pass


if __name__ == '__main__':
    on_subscribe()
