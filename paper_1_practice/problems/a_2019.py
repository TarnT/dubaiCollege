word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

word2 = [i for i in word2]

made = True

for letter in word1:
    if letter in word2:
        word2.pop(word2.index(letter))
    else:
        made = False

if made:
    print("Can be made")
else:
    print("Can't be made")