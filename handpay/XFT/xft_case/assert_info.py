# -*- coding=utf-8 -*-
# @Ahthor: zchen
# @Time: 2023/2/6 16:38
# @File: assert_info

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def _get_alert_info(driver):
    '''
    1.APP弹出框处理
    :param driver:  driver对象
    :return: 弹出框提示语
    '''
    try:
        message = driver.find_element(MobileBy.ID, 'android:id/message').text
        driver.find_element(MobileBy.ID, 'android:id/button1').click()
    except Exception:
        message = ''
    return message


def _get_toast_info(driver):
    '''
    1.APP的Toast处理
    :param driver: driver对象
    :return: Toast提示语
    '''
    try:
        toast_text = driver.find_element(MobileBy.XPATH, '//*[@class=\"android.widget.Toast\"]').text
    except Exception:
        toast_text = ''
    return toast_text


def view_info(driver):
    '''
    1.获取H5页面的提示语
    :param driver: driver对象
    :return: H5页面的提示语
    '''
    try:
        WebDriverWait(driver, 2, 0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]')))
        results = driver.find_elements_by_xpath('/html/body/div[4]')
    except Exception:
        results = ''
    return results
