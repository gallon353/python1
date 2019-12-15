
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

        # 根据控件的class属性匹配控件
        # driver.find_element_by_class_name('android.widget.TextView')

        # driver.find_element_by_xxx()   定位一个控件
        # driver.find_elements_by_xxx()  定位一组控件

        elements = driver.find_elements_by_class_name('android.widget.TextView')
        print(type(elements))
        print(len(elements))

        elements[2].click()
        # Locator Strategy 'css selector' is not supported for this session
        # 不支持的方式
        # el = driver.find_element_by_css_selector('xxxx')
        # el = driver.find_element_by_link_text('xxx')
        # el = driver.find_element_by_partial_link_text('xxx')
        # el = driver.find_element_by_tag_name('xxx')
        # el = driver.find_element_by_name('xxx')


