

# Write some  headers to the columns


#Note :XlsxWriter can only create new files. It cannot read or modify existing files.
import xlsxwriter


# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('C:\python6am\studentmarks2.xlsx')  #create a new workbook object using the Workbook() constructor
worksheet = workbook.add_worksheet()

details = (
    ['English', 75],
    ['Maths',   95],
    ['Physics',  60],
    ['Chemistry',85],
)

# Write some data headers.
worksheet.write('A1', 'Subject')
worksheet.write('B1', 'Marks')
 
# Start from the first cell. Rows and columns are zero indexed.
row = 1
col = 0

# Iterate over the data and write it out row by row.
for subject, marks in (details):
    worksheet.write(row, col,     subject) #We can then use the worksheet object to write data via the write() method:
    worksheet.write(row, col + 1, marks)
    row += 1

# Write a total using a formula.

worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B2:B5)')

workbook.close()
