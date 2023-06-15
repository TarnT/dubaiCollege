def zeroZeroesBinary(num):

    return_num = num

    if num <= 0:
        return -1
    
    num = str(bin(num)[2::])
    num = num.replace("0", "")

    multiplier = 1
    total = 0

    for i in range(0, len(num)):
        total += multiplier
        multiplier *= 2
    
    return f"The zero zeroes binary number of {return_num} is {total}"

print(zeroZeroesBinary(53178))