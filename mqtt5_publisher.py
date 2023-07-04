# -*- coding: utf-8 -*-
# @Time    : 2023/7/3 16:23
# @Author  : yangyuexiong
# @Email   : yang6333yyx@126.com
# @File    : mqtt5_publisher.py
# @Software: PyCharm

import json
import time

import paho.mqtt.client as mqtt

from mqtt5_example import *


# 连接回调函数
def on_connect(client, userdata, flags, rc):
    """连接成功,回调该方法"""

    if rc == 0:
        print("Publisher Connected to MQTT Broker!", rc)
    else:
        print("Failed to connect, return code %d" % rc)


def mqtt5_connect():
    """连接MQTT服务器"""

    client = mqtt.Client(client_id=f"{client_id}{int(time.time())}", protocol=mqtt.MQTTv5)
    client.on_connect = on_connect  # 设置连接回调函数
    client.username_pw_set(username, password)  # 设置用户名和密码
    client.connect(broker_address, port=broker_port)  # 连接到MQTT代理
    return client


def mqtt5_publish():
    """发布"""

    client = mqtt5_connect()
    d = {
        "sn": client_id
    }
    message = json.dumps(d, ensure_ascii=False)
    print(message)
    rc, mid = client.publish(topic, message, 1)  # 发布消息
    print(rc, mid)
    client.disconnect()


if __name__ == '__main__':
    mqtt5_publish()
