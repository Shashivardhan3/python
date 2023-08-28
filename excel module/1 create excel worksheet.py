
#For working with Excel files,we have 2 modules

#1.xlrd ------>for reading a Excel file
#2.xlsxwriter-->for creating and writing into Excel file

#External Modules: The Modules which are not part of python software
#such modules,we call them as external modules ,these modules we need to
#download and install using a component called pip.

#Pip: Pip is a package manager which quickly downloads and installs the
#     external modules which are not part of python software

#Creating Excel files with Python and xlsxwriter
#xlsxwriter is a Python module for creating Excel XLSX files.

#Installing External modules:
#Installing xlsxwriter and xlrd module
#Goto cmdprompt
#C:\Users\DELL>cd\

#C:\>cd python39\scripts

#C:\Python39\Scripts>pip install xlsxwriter

#C:\Python39\Scripts>pip install xlrd


#Note :xlsxwriter can only create new files. It cannot read or modify existing files.
import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('C:\python6am\studentmarks.xlsx')  #create a new workbook object using the Workbook() constructor
worksheet = workbook.add_worksheet() #Workbook() constructor takes one argument which is the filename that we want to create:
#The workbook object is then used to add a new worksheet via the add_worksheet() method:


#By default worksheet names in the spreadsheet will be Sheet1, Sheet2 etc., but we can also specify a name:
# Some data we want to write to the worksheet.
details = (
    ['English', 75],
    ['Maths',   95],
    ['Physics',  60],
    ['Chemistry', 85]
)



# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Iterate over the data and writing row by row.
for subject,marks in details:
    worksheet.write(row, col,subject) #We can then use the worksheet object to write data via the write() method:
    worksheet.write(row, col + 1, marks)
    row += 1

# Write a total using a formula.
worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B1:B4)')

workbook.close()
