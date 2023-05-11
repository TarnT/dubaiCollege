text = input("Enter text you want to compress: \n")

compressed = ""

count = 0
index = 0

while index < len(text) - 1:
    if text[index] == text[index + 1]:
        count += 1
    else:
        compressed += f"{text[index]}{count + 1} "
    index += 1

compressed += f"{text[- 1]}{count + 1} "

print(compressed)