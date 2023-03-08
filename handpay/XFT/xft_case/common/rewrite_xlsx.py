import openpyxl


class Rewrite_Excel():
    '''
    1.获取Excel对象
    2.获取sheet对象
    3.读取需要写入表格的数据
    4.把数据写入到指定单元格里
    5.保存Excel
    '''

    def re_excel(self, filename, nub, file):
        '''
        :param filename: 要保存数据的文件名
        :param nub:  要打开第几个表，nub必须是数字
        :param file: 获取数据的文件名
        :return:  无
        '''
        wb = openpyxl.load_workbook(filename)
        sheet = wb.worksheets[nub]
        with open(file, 'r', encoding='utf-8') as f:
            datas = f.read()
        datas = datas.split('\n')[:-1]
        for data in enumerate(datas):
            if '测试失败' in data[1]:
                sheet['K' + str(data[0] + 2)] = '测试失败'
            else:
                sheet['K' + str(data[0] + 2)] = '测试通过'
            sheet['J' + str(data[0] + 2)] = data[1]
        ## 指定不同的文件名，可以另存为别的文件
        wb.save(filename)
