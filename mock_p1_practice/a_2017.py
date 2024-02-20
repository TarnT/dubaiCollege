def rle(string):

    count = 1
    current_char = string[0]

    rle = ""

    for i in range(len(string) - 1):
        if string[i+1] == current_char:
            count += 1
        else:
            rle = rle + f"{current_char} {count} "
            count = 1
            current_char = string[i+1]

    rle = rle + f"{current_char} {count}"

    return rle

print(rle("CUTLASSES"))