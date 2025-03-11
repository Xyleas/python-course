from openpyxl import Workbook

tabular_data = """ | Fruit | Vegetable |
| --- | --- |
| Apple | Carrot |
| Banana | Brocoli |
| Grapes | Cucumber |
| Orange | Tomato |
| Peach | Potato |
| Pineapple | Sweet Potato |
| Watermelon | Zucchini | """

rows = tabular_data.split('\n')

spreadsheet = []

for row in rows:
    split_row = row.split('|')
    spreadsheet.append(split_row[1:-1])

#testing print(rows)
print(spreadsheet)

wb = Workbook()
ws = wb.active

for row in spreadsheet:
    ws.append(row)

wb.save('example.xlsx')