num = int(input("Enter an integer greater than 1: \n"))
product = 1
factor = 0
while product < num:
    factor += 1
    product = product * factor
if num == product:
    product = 1
    for i in range(1, factor + 1):
        product = product * i
        print(i)
else:
    print("No result")