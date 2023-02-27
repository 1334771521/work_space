# -*- coding=utf-8 -*-
# @Ahthor: zchen
# @Time: 2023/1/28 11:45
# @File: xft

from appium.webdriver.common.touch_action import TouchAction

from XFT.xft_case.base_driver import BaseDriver
from XFT.xft_case.set_amount import SetAmount
from XFT.xft_case import assert_info

class LoginPage(BaseDriver):

    def login_xft(self,data):
        _ele_data = data[:5]
        try:
            try:
                list(map(self.find,_ele_data))
            except Exception:
                list(map(self.find,_ele_data[1:]))
            # try:
            #     self.driver.find_elements_by_class_name('android.widget.ImageView')
            #     self._back_login()
            # except Exception:
            #     pass
            if len(data) <=5:
                return self._opter_page()
        except  Exception as e:
          try:
              self.driver.find_element_by_id('com.handpay.xftong:id/gesture_login_user_phone_no_tv')
              TouchAction(self.driver).press(x=220,y=850).wait(100).move_to(x=300,y=0).move_to(x=300,y=0).move_to(x=0,y=300).move_to(x=0,y=300).release().perform()
          except Exception:
              pass
        return SetAmount(self.driver)


    def _opter_page(self):
        result = assert_info._get_toast_info(self.driver)
        result1 = assert_info._get_alert_info(self.driver)
        if result:
            return result
        elif result1:
            return result1
        else:
            return '登陆成功'

    # def _handle_data(self,data):
    #     _ele_data = (('id', "android:id/button1"), ('id', "com.handpay.xftong:id/et_phone", data[0]),
    #          ('id', "com.handpay.xftong:id/btn_getcode"),
    #          ('id', "com.handpay.xftong:id/et_verfcode", data[1]), ('id', "com.handpay.xftong:id/btn_login"))
    #     return _ele_data

    # def _back_login(self):
    #     while True:
    #         _name = self.driver.find_elements_by_class_name('android.widget.ImageView')
    #         if len(_name) >1:
    #             break
    #     _name[-1].click()
    #     self.driver.find_elements_by_class_name('android.widget.ImageView')[5].click()
    #     self.driver.find_element_by_id('com.handpay.xftong:id/tv_gesture_pwd').click()
    #     if len(self.driver.find_elements_by_id('com.handpay.xftong:id/leftTv'))>1:
    #         self.driver.find_element_by_id('com.handpay.xftong:id/use_gesture_pwd_switch_button').click()
    #     self.driver.back()
    #     self.driver.find_element_by_id('com.handpay.xftong:id/bt_setting_exit').click()

# LoginPage().login_xft().set_amount().set_card().pay_page()