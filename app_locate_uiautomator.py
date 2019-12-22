
import unittest
from appium import webdriver
from time import sleep

from selenium.common.exceptions import *


class AndroidTest(unittest.TestCase):
    """
    APP测试用例
    """

    # test fixture

    # override
    def setUp(self):
        desired_caps = {}
        # 操作系统名称 iOS, Android
        desired_caps['platformName'] = 'Android'
        # 设备名 Android平台参数的值可以任意
        desired_caps['deviceName'] = 'tiantian emulator'
        # 指定启动的APP有两种方式
        # 方式1
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        sleep(2)
        # 断开连接,关闭APP
        self.driver.quit()

    def test1(self):
        driver = self.driver

        # driver.find_element_by_xpath()

        # 使用uiautomator方式定位
        # 根据控件的text匹配
        # el = driver.find_element_by_android_uiautomator('new UiSelector().text("Animation");')


        # el = driver.find_element_by_android_uiautomator('.text("Animation")')

        # 根据控件的部分text匹配

        # el = driver.find_element_by_android_uiautomator('.textContains("ation")')

        # 根据控件的text开头匹配
        # el = driver.find_element_by_android_uiautomator('.textStartsWith("Ani")')

        # 根据正则表达式(regular expression  RE)匹配控件文本
        # el = driver.find_element_by_android_uiautomator('.textMatches("^An[a-z]{10,}n$")')

        # 根据控件的content-desc属性
        # el = driver.find_element_by_android_uiautomator('.description("Animation")')

        # 根据控件的content-desc属性部分值
        # el = driver.find_element_by_android_uiautomator('.descriptionContains("mation")')

        # 根据控件的content-desc属性开始部分
        # el = driver.find_element_by_android_uiautomator('.descriptionStartsWith("Ani")')

        # 根据正则表达式匹配控件的content-desc属性
        # el = driver.find_element_by_android_uiautomator('.descriptionMatches("^An[a-z]{3,}n$")')

        # 根据class属性匹配
        # el = driver.find_element_by_android_uiautomator('.className("android.widget.TextView")')
        # 同时使用class和index属性匹配
        # el = driver.find_element_by_android_uiautomator('.className("android.widget.TextView").index(1)')


        # 层级定位
        # el = driver.find_element_by_android_uiautomator('.className("android.widget.ListView").childSelector(.index(1))')

        # clickable(true)
        # el = driver.find_element_by_android_uiautomator('.index(0).className("android.widget.TextView").clickable(true)')
        # el = driver.find_element_by_android_uiautomator('.index(0).className("android.widget.TextView").clickable(false)')

        # 使用resource-id匹配
        el = driver.find_element_by_android_uiautomator('.resourceId("android:id/text1").index(1)')


        # 二次定位
        # parent = driver.find_element_by_android_uiautomator('.className("android.widget.ListView")')
        # el = parent.find_element_by_android_uiautomator('.index(1)')




        # el.click()
        print('控件的文本:')
        print(el.text)
        print(el.get_attribute('text'))


