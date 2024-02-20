def most_occuring(array):

    occurences = {}

    for i in array:
        if i not in occurences.keys():
            occurences[i] = 1
        else:
            occurences[i] += 1

    occurences = sorted(occurences.items(), key=lambda item: item[1], reverse=True)

    if occurences[0][1] == occurences[1][1]:
        return "data is multimodal"

    return occurences[0][0]

print(most_occuring([0, 1, 2, 1, 2, 1]))