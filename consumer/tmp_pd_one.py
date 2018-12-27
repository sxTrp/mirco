#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-12-21 下午2:55
# @Author  : ShaoXin
# @Summary :
# @Software: PyCharm
from tools.redis_cli import redis_cli

for i in range(10):
    redis_cli.rpush(i)
