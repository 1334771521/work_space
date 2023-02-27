# -*- coding=utf-8 -*-
# @Ahthor: zchen
# @Time: 2023/1/30 15:47
# @File: set_card
from appium.webdriver.common.mobileby import MobileBy

from XFT.xft_case.base_driver import BaseDriver
from XFT.xft_case.pay_page import PayPage
from XFT.xft_case import assert_info


class SetCard(BaseDriver):
    def set_card(self,data):
        try:
            list(map(self.find,data[5:11]))
        except Exception:
            try:
              list(map(self.find, data[9:11]))
            except Exception:
              pass
        if len(data) <= 11:
            return self._opter_page(data)
        return PayPage(self.driver)

    def _opter_page(self,data):
        result = assert_info._get_alert_info(self.driver)
        try:
            self.driver.find_element_by_id(data[10][1])
        except Exception:
            self.driver.back()
        if result:
            return result
        else:
            return '设置卡号成功'

  # def _handle_data(self,data):
  #     _ele_data = [['id', "com.handpay.xftong:id/bank_card_no_et",data[3]], ['id', "com.handpay.xftong:id/btn_pay"]]
  #     return _ele_data