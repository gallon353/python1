
import unittest
from appium import webdriver
from time import sleep

import warnings



class AndroidTest(unittest.TestCase):
    """
    APP测试用例
    """


    def test1(self):
        print('test1')
        self.assertEqual(1, 2)

    def test2(self):
        print('test1')

