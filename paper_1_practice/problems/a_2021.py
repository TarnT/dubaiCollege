nth = int(input("Enter the nth hashard number: "))

num = 1
count = 0 

while count < nth:
    sumDigits = sum([int(i) for i in str(num)])
    if num % sumDigits == 0:
        count += 1
    num += 1

print(f"The {nth} Hashard number is {num - 1}")