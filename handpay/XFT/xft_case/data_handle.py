# -*- coding=utf-8 -*-
# @Ahthor: zchen
# @Time: 2023/1/31 17:47
# @File: data_handle

import yaml

def handle_data(data):
    _order = [1,3,5,9,11,12,13,15]
    _long = {2:5,3:9,4:11,8:18}
    with open('../xft_case/data/ele_data.yaml', 'r') as f:
        _ele_data = yaml.safe_load(f)
    def get_data(number,da):
        _ele_data[number].append(da)
    list(map(get_data,_order[:(len(data))],data))
    _ele_data =_ele_data[:_long[len(data)]]
    return _ele_data

# # data  = ['data[0]','data[1]','data[2]','data[3]','data[4]','data[5]','data[6]','data[7]']
# data  = ['data[0]','data[1]','data[2]','data[3]','data[4]','data[5]','data[6]','data[7]']
# print(_handle_data(data))