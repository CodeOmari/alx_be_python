number = int(input("Enter a number to see its multiplication table:"))

for n in range(1, 11):
    Z = number * n
    print(f"{number} * {n} = {Z}")
