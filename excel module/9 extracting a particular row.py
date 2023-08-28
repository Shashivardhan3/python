# Program to extract a particular row 
import xlrd 
  
loc = ("C:/data/emp2.xls")
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)

print(sheet.row_values(1)) 
