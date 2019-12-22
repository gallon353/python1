
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep




class AndroidTest(unittest.TestCase):
    """
    APP测试用例
    """

    # test fixture

    # override
    def setUp(self):
        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
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
        x = loc['x'] + 60 * size['width'] / 100
        y = loc['y'] + size['height'] / 2

        action = TouchAction(driver)
        # 点击屏幕
        # action.tap(x=x, y=y).perform()
        # press()  手指按下  release() 抬起手指
        # action.press(x=x, y=y).release().perform()
        # long_press() 长按
        # action.long_press(x=x, y=y, duration=3000).release().perform()

        # 屏幕滑动
        # move_to() 移动到指定坐标
        action.press(x=100, y=y).wait(0).move_to(x=x,y=y).release().perform()


