# assuming that both upper and lowercase letters are valid

def check_validity(number):

    valid = True 

    first_two = number[0:2]
    middle_six = number[2:7]
    last = number[-1]

    if len(number) != 9 or not first_two.isalpha() or not middle_six.isdigit() or not last.isalpha():
        print("Number is not valid")
        return
    
    print("Number is valid")
    return

   
number = input("Input a National Insurance Number to Check for Validity: ")
check_validity(number)