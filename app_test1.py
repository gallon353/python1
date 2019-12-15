
# from selenium import webdriver
from appium import webdriver
from time import sleep


if __name__ == '__main__':
    desired_caps = {}
    # 操作系统名称 iOS, Android
    desired_caps['platformName'] = 'Android'
    # 设备名 Android平台参数的值可以任意
    desired_caps['deviceName'] = 'tiantian emulator'
    # 指定启动的APP有两种方式
    # 方式1
    desired_caps['appPackage'] = 'io.appium.android.apis'
    desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'
    # desired_caps['appActivity'] = '.ApiDemos'

    # 方式2
    # desired_caps['app'] = r'E:\work\app appium\apks\ApiDemos-debug.apk'
    #     # 与appium服务器建立会话(session),打开APP
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # 定位控件, 参数是控件的文本(text)
    # driver.find_element_by_id("Animation").click()

    # 参数是控件的content-desc的值(content description 控件的描述信息)
    el = driver.find_element_by_accessibility_id('Animation')
    el.click()

    sleep(2)

    # 断开连接,关闭APP
    driver.quit()







