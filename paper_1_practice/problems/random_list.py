import random, string

alphabet = string.ascii_lowercase + string.ascii_uppercase

ls = []
upper, lower = 0, 0

for i in range(random.randint(1, 1000)):
    letter = random.choice(alphabet)
    ls.append(letter)
    if letter.isupper():
        upper += 1
    else:
        lower += 1

print(ls)
print(f"There are {lower} lowercase letters and {upper} upercase letters")