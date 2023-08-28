

# Create a workbook and add multiple worksheets.
import xlsxwriter

workbook = xlsxwriter.Workbook('C:\Python6am\studentmarks3.xlsx')  #create a new workbook object using the Workbook() constructor
worksheet1 = workbook.add_worksheet('Test1')#if worksheet name(Test1) is not specified then it takes sheet1 by default
worksheet2 = workbook.add_worksheet('Test2')  


#By default worksheet names in the spreadsheet will be Sheet1, Sheet2 etc., but we can also specify a name:
# Some data we want to write to the worksheet.
details1 = (
    ['English', 75],
    ['Maths',   95],
    ['Physics',  60],
    ['Chemistry',85],
)
details2 = (
    ['English', 70],
    ['Maths',   90],
    ['Physics',  80],
    ['Chemistry',95],
)


# writing into 1st worksheet
# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0
for subject, marks in (details1):
    worksheet1.write(row, col, subject)
    worksheet1.write(row, col + 1, marks)
    row += 1
# writing into 2nd worksheet
row = 0
col = 0
for subject, marks in (details2):
    worksheet2.write(row, col,     subject)
    worksheet2.write(row, col + 1, marks)
    row += 1

# calculate total for worksheet1
worksheet1.write(row, 0, 'Total')
worksheet1.write(row, 1, '=SUM(B1:B4)')

# calculate total for worksheet2
worksheet2.write(row, 0, 'Total')
worksheet2.write(row, 1, '=SUM(B1:B4)')

workbook.close()
