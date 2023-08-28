import pandas

# find your sheet name at the bottom left of your excel file and assign it to sheet_name
my_sheet = 'Sheet1'
file_name = 'C:/data/emp2.xls' # name of your excel file
df = pandas.read_excel(file_name, sheet_name = my_sheet) #dataframe gets created
print(df) # shows headers with row


