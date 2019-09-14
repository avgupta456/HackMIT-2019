import ocr
import abbrev

import os
import sys

def repNum(str):
    try:
        return float(str)
    except ValueError:
        try: return float(str[1:])
        except ValueError: return -1

for filename in os.listdir(os.getcwd()+"/DATA"):
    if("jpg" in filename):
        print(filename)
        document = open("Data/"+filename, 'rb')
        data = ocr.getOCR(document)

        totals = []
        print_next = False
        for item in data['Blocks']:
            if item['BlockType'] == 'LINE':
                if(print_next):
                    totals.append(item['Text'])
                    print_next = False
                if("total" in item['Text'].lower()):
                    print_next = True

        newTotals = []
        for i in range(len(totals)):
            newTotals.append(repNum(totals[i]))

        print(max(newTotals))
