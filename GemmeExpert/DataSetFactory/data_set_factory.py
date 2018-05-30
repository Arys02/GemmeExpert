from xlrd import open_workbook

import csv

def open_csv(filename):
    return open_workbook(filename)

def from_xls_to_csv(filename):
    file_xls = open_csv(filename)
    for i in range(2, file_xls):
        sheet = file_xls.sheet_by_index(i)
        with open("data/%s.csv" %(sheet.name.replace(" ", "")), "w") as file :
            writer = csv.writer(file, delimiter = ";")
            header = [cell.value for cell in sheet.row(0)]
            write.writerow(header)
                    
            for row_idx in range(1, sheet.nrows):
                row = [int(cell.value) if isinstance(cell.value, float) else cell.value for cell in sheet.row(row_idx) ]
                writer.writerow(row)
            

            
         



def test_1():
    return ("lolmdr")
