data = open('./CupcakeInvoices.csv')

for row in data:
    print(row)

for row in data:
    row = row.split(',')
    print(row[2])

for row in data:
    row = row.split(',')
    total = int(row[3]) * float(row[4])
    print(total)

total = 0

for row in data:
    row = row.split(',')
    total = total + (int(row[3]) * float(row[4]))

    print(round(total))


data.close()

