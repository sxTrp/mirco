#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-12-24 上午10:02
# @Author  : ShaoXin
# @Summary : 项目配置文件
# @Software: PyCharm
import os


BASEDIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

PROJECT_NAME = BASEDIR.split(os.path.sep)[-1]

ENV = os.environ.get('{project_name}_ENV'.format(project_name=PROJECT_NAME.upper()), 'LOCAL')  # PROD/UAT/DEV/LOCAL

ZK_HOSTS = '10.10.1.80:2181,10.10.1.81:2182,10.10.1.82:2182' if ENV == 'LOCAL' else os.environ.get('ZK_HOSTS')

LOG_PATH = os.path.join(BASEDIR, 'logs')

if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)
os.environ.setdefault('log_path', LOG_PATH)  # logging.int使用

if __name__ == '__main__':
    print(PROJECT_NAME)
