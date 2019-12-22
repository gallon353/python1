
import unittest
from appium import webdriver
from time import sleep




class AndroidTest(unittest.TestCase):
    """
    APP测试用例
    """

    # test fixture

    # override
    def setUp(self):
        desired_caps = dict()
        # 操作系统名称 iOS, Android
        desired_caps['platformName'] = 'Android'
        # 设备名 Android平台参数的值可以任意
        desired_caps['deviceName'] = 'tiantian emulator'
        #
        desired_caps['appPackage'] = 'com.android.androidui'
        desired_caps['appActivity'] = '.MainActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        sleep(2)
        # 断开连接,关闭APP
        self.driver.quit()

    def test1(self):
        driver = self.driver
        el = driver.find_element_by_android_uiautomator('.resourceId("com.android.androidui:id/seekBar1")')
        # el.click()

        size = el.size
        loc = el.location
        print('size:', size)
        print('loc:', loc)
        x = loc['x'] + 62 * size['width'] / 100
        y = loc['y'] + size['height'] / 2
        # tap 点击屏幕(支持单点和多点,最多支持5个手指点击)
        driver.tap([(x, y)], duration=3000)

        # 屏幕滑动
        # driver.swipe(100, y, x, y, duration=3000)

        # 快速滑动
        # driver.flick(100, y, x, y)


