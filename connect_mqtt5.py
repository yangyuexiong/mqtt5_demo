# -*- coding: utf-8 -*-
# @Time    : 2023/7/4 11:10
# @Author  : yangyuexiong
# @Email   : yang6333yyx@126.com
# @File    : connect_mqtt5.py
# @Software: PyCharm

import paho.mqtt.client as mqtt

from mqtt5_example import MQTT5_EXAMPLE

client_id = MQTT5_EXAMPLE.client_id  # 客户端ID
broker_address = MQTT5_EXAMPLE.broker_address  # MQTT broker地址
broker_port = MQTT5_EXAMPLE.broker_port  # MQTT broker地址
username = MQTT5_EXAMPLE.username
password = MQTT5_EXAMPLE.password
topic = MQTT5_EXAMPLE.topic  # 主题


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)


def connect_mqtt5():
    """连接MQTT服务器"""

    client = mqtt.Client(client_id=client_id, protocol=mqtt.MQTTv5)
    client.on_connect = on_connect  # 设置连接回调函数
    client.username_pw_set(username, password)  # 设置用户名和密码
    client.connect(broker_address, port=broker_port)  # 连接到MQTT代理
    return client
