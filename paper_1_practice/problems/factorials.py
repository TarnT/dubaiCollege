def iterationFactorial(num):
    total = 1
    for i in range(1, num + 1):
        total *= i
    return total 

def recursionFactorial(num):
    if num == 1:
        return 1
    return num * recursionFactorial(num - 1)

user_num = int(input("Enter a number to calculate its factorial! "))

print(iterationFactorial(user_num))
print(recursionFactorial(user_num))