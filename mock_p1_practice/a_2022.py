def reverse_vowels(string):

    vowel_indexes = []
    word_vowels = []
    change_string = [i for i in string]

    for i in range(len(string)):
        if string[i] in "aeiou":
            vowel_indexes.append(i)
            word_vowels.append(string[i])

    word_vowels = word_vowels[::-1]

    for i in range(len(string)):
        if i in vowel_indexes:
            change_string[i] = word_vowels.pop(0)

    return "".join(change_string)

print(reverse_vowels("nakedmolerat"))