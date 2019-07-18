#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
@作者：wuchengan
@文件名：Django/functional_tests.py
@时间：2019/7/17 10:10
@文档说明:
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('localhost:8000')
assert 'Django' in driver.title
