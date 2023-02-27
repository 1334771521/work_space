# -*- coding=utf-8 -*-
# @Ahthor: zchen
# @Time: 2023/1/29 14:48
# @File: base_driver
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy



class BaseDriver():

    def __init__(self,base_driver=None):
        with open('../xft_case/data/mobile_m6_config_data.yaml', 'r') as f:
            _caps = yaml.safe_load(f)
        if base_driver==None:
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",_caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver = base_driver


    def find(self,by='',el='',value=''):
        '''
        封装元素查找方法
        :param by:      查找元素的方式
        :param el:      元素的定位
        :param value:   输入的值
        :return:        返回元素的对象
        '''
        _name = {'id':MobileBy.ID,'class':MobileBy.CLASS_NAME,'name':MobileBy.NAME,'css':MobileBy.CSS_SELECTOR,'link':MobileBy.LINK_TEXT,'xpath':MobileBy.XPATH}
        if el!='':
            by,el,value = by,el,value
        elif el=='' and value=='' and len(by)==3:
            by,el,value= by
        elif el=='' and len(by)==2:
            by,el= by
        _ele = self.driver.find_element(_name[by], el)
        self._opter_ele(_ele,value,el)

    def _opter_ele(self,_ele,value,el):
        if value=='':
            _ele.click()
        else:
            if value==' ':
                _ele.clear()
                self.driver.hide_keyboard()
            else:
                _ele.send_keys(value)
                if el =='//*[@id="noCardPayForm"]/div/div[10]/div[2]/input':
                    self.driver.hide_keyboard()

