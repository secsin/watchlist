# -*- coding: utf-8 -*-
# @Time    : 2022/6/30 15:00
# @Author  : secsin
# @Email   : cjc3705@@163.com
# @File    : wsgi.py
# @Project  : watchlist
# @Software: PyCharm
import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from watchlist import app
