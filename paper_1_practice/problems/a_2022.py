vowels = "aeiou"
word = input("Enter word: ")
vowelIndexes = []

for i in range(len(word)):
    if word[i] in vowels:
        vowelIndexes.append(i)

vowelIndexes = vowelIndexes[::-1]
newWord = ""
vowelCount = 0

for i in range(len(word)):
    if word[i] in vowels:
        newWord += word[vowelIndexes[vowelCount]]
        vowelCount += 1
    else:
        newWord += word[i]

print(newWord)