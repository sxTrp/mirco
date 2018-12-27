#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-12-24 上午10:17
# @Author  : ShaoXin
# @Summary :
# @Software: PyCharm
import json

from tools.logger import code_log
from tools.redis_cli import redis_cli
from redis.exceptions import TimeoutError

from tasks.dms_worker import dms_work

while 1:
    try:
        a = redis_cli.blpop('dms')
        code_log.info(f'receive task {a}')
        dms_work.delay(str(a))
    except TimeoutError as e:
        print('block timeout, there is nothing!')


