# -*- coding: utf-8 -*-
# @Time    : 2023/7/3 16:21
# @Author  : yangyuexiong
# @Email   : yang6333yyx@126.com
# @File    : auth.py
# @Software: PyCharm


import time
import hashlib


class BaseMQTT:
    """MQTT基类"""

    def __init__(self, broker_address: str, broker_port: int = 1883, username: str = "", password: str = "",
                 client_id="客户端ID", topic="主题", connect_type="hy", **kwargs):
        """

        :param connect_type:连接类型默认hy
        :param kwargs:`hy`扩展参数-> productKey,secretKey...
        :param broker_address: MQTT broker地址
        :param broker_port: MQTT broker地址
        :param username:    MQTT broker的用户名
        :param password:    MQTT broker的密码
        :param client_id:   客户端ID
        :param topic:       主题
        """
        self.connect_type = connect_type
        self.hy_expand = kwargs
        self.broker_address = broker_address
        self.broker_port = broker_port
        self.username = self.hy_username() if self.connect_type == 'hy' else username
        self.password = self.hy_password() if self.connect_type == 'hy' else password
        self.client_id = client_id
        self.topic = topic

    def hy_username(self):
        """生成用户名"""

        productKey = self.hy_expand.get("productKey")
        username = f"{productKey}|{int(time.time() * 1000)}"
        return username

    def hy_password(self):
        """生成密码"""

        secretKey = self.hy_expand.get("secretKey")
        password = f"{secretKey}|{int(time.time() * 1000)}"
        md5_hash = hashlib.md5()  # 创建MD5哈希对象
        md5_hash.update(password.encode('utf-8'))  # 更新哈希对象，传入要计算哈希值的数据
        password = md5_hash.hexdigest()
        return password


if __name__ == '__main__':
    hy_expand = {
        "productKey": "9c9fb71c402b4a4db3b80ec44cef96ca",
        "secretKey": "98970019183d428ca4c2b0ca9f483973"
    }
    mqtt5 = BaseMQTT(
        broker_address="192.168.9.2", port=1883, **hy_expand
    )
