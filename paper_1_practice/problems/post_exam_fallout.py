while True:

    num = input("Enter a number between 0 and 100 inclusive: ")

    if num == "":
        print("Can't enter empty values")
        continue

    try:
        int(num)
    except ValueError:
        print("Don't enter integer problems")
        continue
    else:
        num = int(num)

        if num > 100 or num < 0:
            print("Only enter values from 0-100 inclusive")
            continue

        break 

print(num)