import openpyxl
import random
xfile = openpyxl.load_workbook("Template.xlsx")
cols = ['A', 'B', 'C', 'D', 'E']
def questionBronze(i):
    if(i<6):
        return ""+str(random.randint(1, 10))+"+"+str(random.randint(1, 10))+"="
    elif(i<9):
        return ""+str(random.randint(10, 30))+"-"+str(random.randint(1, 10))+"="
    return ""+str(random.randint(1, 10))+"x"+str(random.randint(1, 10))+"="

sheet = xfile.get_sheet_by_name('Sheet1')

for col in cols:
    for row in range(2, 12):
        sheet[''+col+str(row)+'']=questionBronze(random.randint(1, 10))

xfile.save('testContent.xlsx')