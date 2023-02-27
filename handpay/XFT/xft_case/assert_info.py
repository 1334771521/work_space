# -*- coding=utf-8 -*-
# @Ahthor: zchen
# @Time: 2023/2/6 16:38
# @File: assert_info
from appium.webdriver.common.mobileby import MobileBy


def _get_alert_info(driver):
    try:
        message = driver.find_element(MobileBy.ID, 'android:id/message').text
        print(message)
        driver.find_element(MobileBy.ID, 'android:id/button1').click()
        return message
    except Exception:
        pass


def _get_toast_info(driver):
    try:
        toast_text = driver.find_element(MobileBy.XPATH, '//*[@class=\"android.widget.Toast\"]').text
        print(toast_text)
        return toast_text
    except Exception:
        pass

def view_info(driver):
    try:
        result =driver.find_elements_by_xpath('/html/body/div[4]')
        return result
    except Exception:
        pass