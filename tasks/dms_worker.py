#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-12-24 上午10:38
# @Author  : ShaoXin
# @Summary :
# @Software: PyCharm
from time import sleep

from celery import Celery

from tools.logger import code_log

tags_task = Celery('tags')
tags_task.config_from_object('config.celery_config')


@tags_task.task
def dms_work(params):
    code_log.error(f'begin worker {params}')
    sleep(5)
    code_log.error(f'end worker {params}')
