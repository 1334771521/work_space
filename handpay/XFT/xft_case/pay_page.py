# -*- coding=utf-8 -*-
# @Ahthor: zchen
# @Time: 2023/1/30 15:48
# @File: pay_page

from XFT.xft_case.base_driver import BaseDriver
from XFT.xft_case import assert_info


class PayPage(BaseDriver):
    '''
    支付页面操作
    '''

    def _switch_context(self):
        '''
        获取上下文，用于切换原生页面和h5页面
        :return: 无
        '''
        while True:
            _contexts = self.driver.contexts
            if len(_contexts) > 1:
                break
        self.driver.switch_to.context(_contexts[-1])

    def pay_page(self, data):
        '''
        1.先切换到原生页面，进行数据输入，如果报错，则不做处理
        2.调用h5切换函数，切换到h5页面，进行页面数据输入
        3.点击确认按钮
        4.获取页面报错信息
        :param data: 定位数据，包含定位元素和定位方式
        :return: 返回断言数据
        '''
        try:
            self.driver.switch_to.context('NATIVE_APP')
            list(map(self.find, data[5:11]))
        except Exception:
            pass
        self._opter_context(data)
        self.find(data[-1][0], data[-1][1])
        try:
            result = assert_info.view_info(self.driver)
        except Exception as e:
            result = ''
        return self._opter_page(result, data)

    def _opter_context(self, data):
        '''
        1.获取支付页面元素，如果能获取，则不用切换h5页面，如果不能获取则切换到h5页面
        2.刷新h5页面，方便下次输入
        3.进行页面数据的输入
        :param data: 定位数据，包含定位元素和定位方式
        :return: 无
        '''
        try:
            self.driver.find_element_xpath(data[-2][1])
        except Exception:
            self._switch_context()
        self.driver.refresh()
        list(map(self.find, data[11:17]))

    def _opter_page(self, result, data):
        '''
        1.获取支付页面元素，如果能获取，则返回页面报错信息，否则切换到下一个h5页面，获取页面信息，返回断言信息
        :param result:  返回报错信息
        :param data: 定位数据，包含定位元素和定位方式
        :return: 返回断言数据
        '''
        try:
            self.driver.find_element_xpath(data[-2][1])
            for re in result:
                return re.text
        except Exception:
            self.driver.switch_to.window(self.driver.window_handles[-1])
            result = self.find('xpath', '/html/body/div[1]/div/span')
            self.driver.back()
            return result
