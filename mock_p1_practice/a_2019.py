def can_be_made(base, word):

    base = [i for i in base]
    word = [i for i in word]

    for letter in word:
        try:
            base.pop(base.index(letter))
        except:
            return False
    
    return True

print(can_be_made("ELEPHANTINE", "NINEEEE"))