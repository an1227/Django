#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
@作者：wuchengan
@文件名：Django/functional_tests.py
@时间：2019/7/17 10:10
@文档说明:
"""
from selenium import webdriver
import unittest

class DjangoTest(unittest.TestCase):
    def setUp(self):
        '''准备工作：启动浏览器'''
        self.driver=webdriver.Chrome()

    def test_url_and_assert(self):
        '''测试项：打开URL和断言测试'''
        self.driver.get('http://localhost:8000')
        self.assertIn('Django',self.driver.title)

    def tearDown(self):
        '''善后工作：关闭浏览器'''
        self.driver.quit()

if __name__ == '__main__':
        unittest.main(verbosity=2)
