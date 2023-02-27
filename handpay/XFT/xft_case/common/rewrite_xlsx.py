import openpyxl

class Rewrite_Excel():

    def re_excel(self,filename,nub,file):
        '''
        :param filename:      要打开的文件名
        :param nub:            要打开第几个表，nub必须是数字
        :return:
        '''
        wb = openpyxl.load_workbook(filename)
        # 得到sheet对象
        # sheet1 = wb.sheetnames[1]       # 以下标获取表名
        # sheet = wb[sheet1]              # 以表名定位表对象
        sheet = wb.worksheets[nub]        # 以下标定位表对象
        with open(file,'r',encoding='utf-8') as f:
            data1 = f.read()
        data2 = data1.split('\n')[:-1]
        print(data2,type(data2))
        for data in enumerate(data2):
            if '测试失败' in data[1]:
                sheet['K' + str(data[0] + 2)] = '测试失败'
            else:
                sheet['K' + str(data[0] + 2)] = '测试通过'
            sheet['J'+str(data[0]+2)] = data[1]
        ## 指定不同的文件名，可以另存为别的文件
        wb.save(filename)
# filename = '数据2.xlsx'
# nub = 0
# Rewrite_Excel =Rewrite_Excel()
# Rewrite_Excel.re_excel(filename,nub)