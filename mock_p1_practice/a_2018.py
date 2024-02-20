def is_prime():

    while True:

        n = int(input("Enter a number: "))

        if n > 1:
            prime = True
            for i in range(2, n):
                if n % i == 0:
                    prime = False
                    break

            if not prime:
                print("Not a prime number")
            else:
                print("Prime number")
        
        else:
            print("Not greater than 1")
        
        choice = input("Enter another number: Y/N ")

        if choice == "N":
            break

is_prime()