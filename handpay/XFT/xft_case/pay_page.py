# -*- coding=utf-8 -*-
# @Ahthor: zchen
# @Time: 2023/1/30 15:48
# @File: pay_page

from time import  sleep
from XFT.xft_case.base_driver import BaseDriver
from XFT.xft_case import assert_info

class PayPage(BaseDriver):

    def _switch_context(self):
        while True:
            _contexts = self.driver.contexts
            if len(_contexts) >1:
                break
        self.driver.switch_to.context(_contexts[-1])

    def pay_page(self,data):
        try:
            self.driver.switch_to.context('NATIVE_APP')
            list(map(self.find, data[5:11]))
        except Exception:
            self._opter_context(data)
        self.find(data[-1][0],data[-1][1])
        result = assert_info.view_info(self.driver)
        sleep(1)
        return self._opter_page(result,data)

    def _opter_context(self,data):
        try:
            self.driver.find_element_xpath(data[-2][1])
        except Exception:
            self._switch_context()
            self.driver.refresh()
            list(map(self.find, data[11:17]))

    def _opter_page(self,result,data):
        try:
            self.driver.find_element_xpath(data[-2][1])
        except Exception:
            self.driver.back()
        if result:
            for re in result:
                return re.text
        else:
            return '支付完成！'