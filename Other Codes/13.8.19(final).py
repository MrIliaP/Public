while True:
    try:
        ticket = int(input("How many tickets:\n"))
        if 1 < ticket < 99:
            break
        else:
            raise ValueError
    except ValueError:
        print("Please, input amount 1-99")

price = []

for i in range(1, ticket + 1):
    while True:
        try:
            age = int(input(f"Age of {i} person?\n"))
            if age < 18:
                price.append(0)
                break
            if 18 <= age <= 24:
                price.append(990)
                break
            if 25 <= age <= 99:
                price.append(1390)
                break
            else:
                raise ValueError
        except ValueError:
            print("Please, input age between 1-99")

while price.count(0) > 0:
    price.remove(0)

total = sum(price)
if len(price) > 3:
    print()
    print("You get discount!!!")
    print("__________________________")
    print(f"Amount:\n {int(total * 0.9)} rub.")
else:
    print("__________________________")
    print(f"Amount:\n {total} rub.")

print("Please don't forget to bring your ID")
