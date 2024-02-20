def check_isbn():

    ISBN = []

    for i in range(13):
        isbn_digit = int(input("Enter a digit into the ISBN: "))
        ISBN.append(isbn_digit)

    # used to select a number within the array
    Count = 0

    # stores results of calculated number form array
    CalculatedDigit = 0

    while Count < 12:
        if Count % 2 == 0:
            CalculatedDigit += (ISBN[Count])
        else:
            CalculatedDigit += (ISBN[Count] * 3)
        
        Count += 1
    
    CalculatedDigit = CalculatedDigit % 10

    CalculatedDigit = 10 - CalculatedDigit

    if CalculatedDigit == 10:
        CalculatedDigit = 0

    if CalculatedDigit == ISBN[Count]:
        print("Valid ISBN")
    else:
        print("Invalid ISBN")

    return None

check_isbn()