#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-8 上午10:49
# @Author  : ShaoXin
# @Summary : 日志工具
# @Software: PyCharm
import os
from logging import config, getLogger

from config.pj_config import BASEDIR, LOG_PATH

os.environ.setdefault('log_path', LOG_PATH)

config.fileConfig(os.path.join(BASEDIR, 'conf', "logging.ini"))
code_log = getLogger()

if __name__ == '__main__':
    code_log.info("Here is a very exciting log message, just for you")


