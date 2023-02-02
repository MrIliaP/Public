money = int(input("Deposit Amount:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
income = list(per_cent.values())
deposit = int(income[0] * money/100), int(income[1] * money/100), int(income[2] * money/100), int(income[3] * money/100)

print(list(deposit))
print("Maximum possible income -", max(deposit))
