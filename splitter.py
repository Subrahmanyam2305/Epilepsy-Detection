from xlrd import open_workbook
import csv
wb = open_workbook('classify_output.xlsx')
for i in range(wb.nsheets):
    sheet = wb.sheet_by_index(i)
    print sheet.name
    with open("testo/%s.csv" %(sheet.name.replace(" ","")), "w") as file:
        writer = csv.writer(file, delimiter = ",")
        print sheet, sheet.name, sheet.ncols, sheet.nrows
       #  header = [cell.value for cell in sheet.row(0)]
       #  writer.writerow(header)
        for row_idx in range(0,sheet.nrows):
             row = [int(cell.value) if isinstance(cell.value, float) else cell.value for cell in sheet.row(row_idx)]
             writer.writerow(row)
