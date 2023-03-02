# -*- coding=utf-8 -*-
# @Ahthor: zchen
# @Time: 2023/2/6 16:38
# @File: assert_info

from appium.webdriver.common.mobileby import MobileBy


def _get_alert_info(driver):
    '''
    1.APP弹出框处理
    :param driver:  driver对象
    :return: 弹出框提示语
    '''
    try:
        message = driver.find_element(MobileBy.ID, 'android:id/message').text
        driver.find_element(MobileBy.ID, 'android:id/button1').click()
        return message
    except Exception:
        pass


def _get_toast_info(driver):
    '''
    1.APP的Toast处理
    :param driver: driver对象
    :return: Toast提示语
    '''
    try:
        toast_text = driver.find_element(MobileBy.XPATH, '//*[@class=\"android.widget.Toast\"]').text
        return toast_text
    except Exception:
        pass


def view_info(driver):
    '''
    1.获取H5页面的提示语
    :param driver: driver对象
    :return: H5页面的提示语
    '''
    try:
        result = driver.find_elements_by_xpath('/html/body/div[4]')
        return result
    except Exception:
        pass
