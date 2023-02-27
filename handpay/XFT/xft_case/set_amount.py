# -*- coding=utf-8 -*-
# @Ahthor: zchen
# @Time: 2023/1/30 15:47
# @File: set_amount
from appium.webdriver.common.mobileby import MobileBy

from XFT.xft_case.base_driver import BaseDriver
from XFT.xft_case.set_card import SetCard
from XFT.xft_case import assert_info

class SetAmount(BaseDriver):

  def set_amount(self,data):
      _ele_data = data[5:9]
      if len(data) <=9:
          return  self._opter_page(_ele_data)
      else:
          try:
              list(map(self.find, _ele_data))
          except Exception:
              pass
      return SetCard(self.driver)

  def _opter_page(self,_ele_data):
      list(map(self.find, _ele_data[:-1]))
      result = assert_info._get_alert_info(self.driver)
      if result:
          return result
      else:
          self.driver.back()
          return '设置金额成功'


  # def _handle_data(self,data):
  #     _ele_data = [['id', "com.handpay.xftong:id/et_amount", data[2]], ['id', "com.handpay.xftong:id/rb_dangmianfu"],
  #                  ['id', "com.handpay.xftong:id/btn_pay"], ['id', "com.handpay.xftong:id/btn_sure"]]
  #     return _ele_data