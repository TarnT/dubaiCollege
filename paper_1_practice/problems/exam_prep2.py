while True:

    userIn = input("Enter a string: ")

    if len(userIn) < 5 or len(userIn) > 7:
        print("Input must be between 5 and 7 characters long!")
        continue

    if userIn.upper() != userIn:
        print("Input must be uppercase only!")
        continue

    letters = {}

    for letter in userIn:
        if letter in letters.keys():
            letters[letter] += 1
        else:
            letters[letter] = 1
    
    noRepeats = True

    for key, count in letters.items():
        if count > 1:
            print("No repeated characters!")
            noRepeats = False 
    
    if not noRepeats:
        continue

    total = 0

    for letter in userIn:
        total += ord(letter)

    if total < 420 or total > 600:
        print("Sum of ASCII characters must be between 400 and 600!")
        continue
    
    print(f"{userIn} is valid!")
    break