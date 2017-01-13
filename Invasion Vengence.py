import openpyxl
import random

wb = openpyxl.load_workbook('Invasion Vengence.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')


def Card_Get(Col_Letter,range1, range2):
    Range = (random.randint(range1,range2))
    Range = str(Range)

    Card = Col_Letter+Range
    C = sheet[Card]
    Card_Name = C.value
    return Card_Name

def Get_Commons():
    Short_Print = (random.randint(1,20))
    if Short_Print == 1:
        x = Card_Get('F',2,5)
        print(x)
    else:
        x = Card_Get('A',2,45)
        print(x)
def Get_Rares():
    x = Card_Get('B',2,21)
    print(x)
def Get_Shinies():
    Secret = (random.randint(1,12))
    Ultra = (random.randint(1,6))

    if Secret == 1:     #Secret Rares
        x = Card_Get('E',2,9)
        print(x)
    elif Ultra == 1 and Secret != Ultra:    #Ultra Rares
        x = Card_Get('D',2,5)
        print(x)
    else   :    #Super Rares
        x = Card_Get('C',2,15)
        print(x)

for i in range(6):
    Get_Commons()
Get_Rares()
Get_Shinies()