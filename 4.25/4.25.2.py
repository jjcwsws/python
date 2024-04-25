#import openpyxl as vb
#路径 = r'C:\Users\86138\OneDrive\桌面\生信\颜一决.xlsx'
#工作簿 = vb.load_workbook(路径)
#显示所有工作表 = 工作簿.worksheets
#print(显示所有工作表)

#import openpyxl as vb
#路径 = r'C:\Users\86138\OneDrive\桌面\生信\颜一决.xlsx'
#工作簿 = vb.load_workbook(路径)
#显示所有工作表 = 工作簿.worksheets
#for i in 显示所有工作表:
#   print(i.title)
#
#第一步，导入模块
#第二部，指定路径
#第三步，打开路径


##第四步，此步骤为删除工作表并保存在原文件中。
##import openpyxl as vb
##路径 = r'C:\Users\86138\OneDrive\桌面\生信\颜一决.xlsx'
##工作簿 = vb.load_workbook(路径)
##工作表 = 工作簿['二月']
##工作簿.remove(工作表)
##工作簿.save(路径)


##第四步，首先指定该工作表是什么!!!此步骤为删除工作表方式并且原文件不变，改动文件重新保存在新文件中。
##import openpyxl as vb
##路径 = r'C:\Users\86138\OneDrive\桌面\生信\颜一决.xlsx'
##路径1 = r'C:\Users\86138\OneDrive\桌面\生信\颜一决1.xlsx'
##工作簿 = vb.load_workbook(路径)
#工作簿.remove(工作簿['二月'])#此处为省略形式，原为：工作表 = 工作簿['二月']
#工作簿.save(路径1)           #                      工作簿.remove(工作表)

##第五步，如何新建工作表
##import openpyxl as vb
##路径 = r'C:\Users\86138\OneDrive\桌面\生信\颜一决.xlsx'
##工作簿 = vb.load_workbook(路径)
##工作簿.create_sheet('二月')
##工作簿.save(路径)

##第五步，如何复制工作表并且更改工作表名（sheet名称），此处未省略缩写
##import openpyxl as vb
##路径 = r'C:\Users\86138\OneDrive\桌面\生信\颜一决.xlsx'
##工作簿 = vb.load_workbook(路径)
##工作表 = 工作簿['四月']
##复制表 = 工作簿.copy_worksheet(工作表)
##复制表.title = '全写复制的表'
##工作簿.save(路径)
##
##第五步，如何复制工作表并且更改工作表名（sheet名称），此处进行省略缩写
##import openpyxl as vb
##路径 = r'C:\Users\86138\OneDrive\桌面\生信\颜一决.xlsx'
##工作簿 = vb.load_workbook(路径)
##复制表 = 工作簿.copy_worksheet(工作簿['四月'])
##复制表.title = '刚刚复制的表'
##工作簿.save(路径)

