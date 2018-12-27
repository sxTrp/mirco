#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-12-24 上午10:42
# @Author  : ShaoXin
# @Summary :
# @Software: PyCharm
from config.zk_config import master_name, celery_broker, broker_password

CELERY_TIMEZONE = 'Asia/Shanghai'
BROKER_TRANSPORT_OPTIONS = {'master_name': master_name}
BROKER_URL = celery_broker
BROKER_PASSWORD = broker_password
CELERYD_HIJACK_ROOT_LOGGER = False  # 禁用celery日志
TASK_SERIALIZER = 'json',
CELERY_ACCEPT_CONTENT = ['json'],  # Ignore other content
CELERY_RESULT_SERIALIZER = 'json'
