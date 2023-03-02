# -*- coding=utf-8 -*-
# @Ahthor: zchen
# @Time: 2023/1/28 11:45
# @File: xft

from appium.webdriver.common.touch_action import TouchAction

from XFT.xft_case.base_driver import BaseDriver
from XFT.xft_case.set_amount import SetAmount
from XFT.xft_case import assert_info


class LoginPage(BaseDriver):
    '''
    登陆页面的操作
    '''

    def login_xft(self, data):
        '''
        1.截取data数据的前5个数据，进行登陆操作
        2.判断data长度是否小于等于5，如果是则进行登陆操作，返回登陆的结果
        3.如果再手势密码页面，则进行手势密码登陆
        4.如果传递的data参数长度大于5,则返回下一个模块的对象
        5.通过继承，把driver对象传递给下一个模块
        :param data: 页面定位数据和需要输入的值
        :return: 断言或者下一个模块的对象
        '''
        _ele_data = data[:5]
        try:
            try:
                list(map(self.find, _ele_data))
            except Exception:
                list(map(self.find, _ele_data[1:]))
            if len(data) <= 5:
                return self._opter_page()
        except  Exception as e:
            try:
                self.driver.find_element_by_id('com.handpay.xftong:id/gesture_login_user_phone_no_tv')
                TouchAction(self.driver).press(x=220, y=850).wait(100).move_to(x=300, y=0).move_to(x=300, y=0).move_to(
                    x=0, y=300).move_to(x=0, y=300).release().perform()
            except Exception:
                pass
        return SetAmount(self.driver)

    def _opter_page(self):
        '''
        1.调用toast方法，获取toast提示语
        2.调用弹出框方法，对弹出框进行处理，获取弹出框提示语
        3.如果两个值为空，则返回登陆成功
        '''
        toast_result = assert_info._get_toast_info(self.driver)
        alert_result = assert_info._get_alert_info(self.driver)
        if toast_result:
            return toast_result
        elif alert_result:
            return alert_result
        else:
            return '登陆成功'
