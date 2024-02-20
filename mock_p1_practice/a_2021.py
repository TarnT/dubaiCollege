def harshard_number():

    n = int(input("Enter value for n: "))

    count = 0
    current_value = 1

    while count < n:
        if current_value % sum([int(i) for i in str(current_value)]) == 0:
            count += 1
        current_value += 1

    return current_value - 1

print(harshard_number())