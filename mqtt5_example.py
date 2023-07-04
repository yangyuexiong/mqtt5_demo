# -*- coding: utf-8 -*-
# @Time    : 2023/7/3 17:47
# @Author  : yangyuexiong
# @Email   : yang6333yyx@126.com
# @File    : mqtt5_example.py
# @Software: PyCharm

from config.config import *
from util.auth import BaseMQTT

hy_expand = {
    "productKey": productKey,
    "secretKey": secretKey
}

MQTT5_EXAMPLE = BaseMQTT(
    broker_address=ip,
    port=port,
    client_id=client_id,
    **hy_expand
)

client_id = MQTT5_EXAMPLE.client_id  # 客户端ID
broker_address = MQTT5_EXAMPLE.broker_address  # MQTT broker地址
broker_port = MQTT5_EXAMPLE.broker_port  # MQTT broker地址
username = MQTT5_EXAMPLE.username  # 账号
password = MQTT5_EXAMPLE.password  # 密码
topic = MQTT5_EXAMPLE.topic  # 主题

print(broker_address)
print(broker_port)
print(username)
print(password)

if __name__ == '__main__':
    pass
