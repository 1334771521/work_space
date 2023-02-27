import openpyxl

class ReadXlsx():

    def get_data(self,filename,nub):
        '''
        :param filename:      需要读取的文件
        :param nub:           要读取的第几张表
        :return:
        '''
        wook = openpyxl.load_workbook(filename)
        sheet = wook.worksheets[nub]
        value1 = sheet['H']
        value2 = sheet['I']
        data = [eval(s.value) for s in value1[1:]]
        data1 = [s.value for s in value2[1:] ]
        return list(zip(data, data1)),data1

# filename = r'数据1.xlsx'
# nub = 0
# print(ReadXlsx().get_data(filename,nub))


# filename = r'C:\Users\zchen\Desktop\新建文件夹\商户数据1.xlsx'
# ws = openpyxl.load_workbook(filename)
# # 根据下标获取工作表的名称
# # sheet = ws.sheetnames[1]
# # print(sheet)
# # sheet = ws[sheet]
# sheet = ws.worksheets[1]
#
# # 按行遍历
# for row in sheet:  # 循环获取表数据
#     for cell in row:  # 循环获取每个单元格的数据
#         print(cell.value,end = ',')
#     print()