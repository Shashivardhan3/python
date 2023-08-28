
#To extract number of rows and cols using Python 
import xlrd 
  
# Give the location of the file 
loc = ("C:/data/emp2.xls") 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
#print(sheet.cell_value(0, 0))
  
# Extracting number of rows and cols
print(sheet.nrows)
print(sheet.ncols)
