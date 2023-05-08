ins = int(input("How many digits do you want to enter?\n"))
dictionary = {}

for i in range(ins):
    num = int(input(f"Enter number {i+1}: "))
    if num not in dictionary.keys():
        dictionary[num] = 1
    else:
        dictionary[num] += 1

counts = sorted(list(dictionary.values()))
multimodal = False
if counts:
    for i in range(1, len(counts)):
        if counts[i] == counts[0]:
            multimodal = True

if multimodal:
    print("Data is multimodal")
else:
    print(max(counts))