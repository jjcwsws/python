import openpyxl as vb
路径 = r'C:\Users\86138\OneDrive\桌面\生信\颜一决.xlsx'
工作簿 = vb.load_workbook(路径)
工作表 = 工作簿 .active#.active打开的是excel关闭前打开并保存过的工作表。（自动保存也算保存）/.active 是打开当前激活的工作表，不是第1张工作表
print(工作表)


import openpyxl as vb
路径 = r'C:\Users\86138\OneDrive\桌面\生信\颜一决.xlsx'
工作簿 = vb.load_workbook(路径)
工作表 = 工作簿['工作表名']
print(工作表)




