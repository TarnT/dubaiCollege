number1 = int(input("Enter a whole number: "))
number2 = int(input("Enter a whole number: "))
temp1 = number1
temp2 = number2

while temp1 != temp2:
    if temp1 > temp2:
        temp1 = temp1 - temp2
    if temp2 > temp1:
        temp2 = temp2 - temp1

result = temp1
print(f"{result} is the greatest common factor of {number1} and {number2}")