def hashN():
    n = int(input("Enter the nth hashed number you want to find. \n"))
    hash_counter = 0
    number = 0
    while hash_counter < n:
        number += 1
        total = sum([int(i) for i in str(number)])
        if number % total == 0:
            hash_counter += 1
    return number
    

print(hashN())