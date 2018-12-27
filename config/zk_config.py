#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-12-24 上午10:01
# @Author  : ShaoXin
# @Summary : 加载zk配置文件
# @Software: PyCharm
import json

from config.pj_config import ZK_HOSTS, PROJECT_NAME, ENV
from kazoo.client import KazooClient


class ZkConnectException(Exception):
    pass


try:
    zk = KazooClient(hosts=ZK_HOSTS)
    zk.start()
except Exception as e:
    raise ZkConnectException("ZK cannot connect, please contact xxx to resolve it.")


def get_config_by_env(name, is_json=False):
    data = zk.get(f"/{PROJECT_NAME}/{ENV.lower()}/{name}")[0].decode('utf8')
    return json.loads(data) if is_json else data


master_name = get_config_by_env("celery/master_name")
celery_broker = get_config_by_env("celery/celery_broker")
broker_password = get_config_by_env("celery/broker_password")


if __name__ == '__main__':
    pass
