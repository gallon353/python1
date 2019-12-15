
import unittest
from appium import webdriver
from time import sleep

import warnings
# warnings.filterwarnings("ignore")
warnings.simplefilter("ignore", ResourceWarning)


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

    def tearDown(self):
        sleep(2)
        # 断开连接,关闭APP
        self.driver.quit()

    def test1(self):
        driver = self.driver

        # 根据控件的xpath表达式匹配控件
        # xpath  xml(xxx.xml)

        # //tag[@属性='属性值' and ...]
        # //tag[n]  选择第n个
        # //tag[text()='元素的文本']

        ########################################
        # //class[@属性='属性值']

        # 根据控件的属性定位

        # 根据index属性
        # el = driver.find_element_by_xpath("//android.widget.TextView[2]")
        # el = driver.find_element_by_xpath("//android.widget.TextView[@index='1']")
        # 根据控件的text属性
        # el = driver.find_element_by_xpath("//android.widget.TextView[@text='Animation']")
        # 根据控件的resource-id属性
        # el = driver.find_element_by_xpath("//android.widget.TextView[@index='1' and @resource-id='android:id/text1']")
        # 根据控件的content-desc属性
        # el = driver.find_element_by_xpath("//android.widget.TextView[@content-desc='Animation']")

        # 根据控件的部分文本定位
        # el = driver.find_element_by_xpath("//android.widget.TextView[contains(@text, 'Ani')]")

        # 层级定位
        # el = driver.find_element_by_xpath("//android.widget.ListView/android.widget.TextView[2]")
        # * 通配符,和selenium一样的
        el = driver.find_element_by_xpath("//android.widget.ListView/*[2]")

        el.click()



