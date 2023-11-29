
def count_words(file_name):

    word_count = {}
    # lower and upper are considered same

    try:

        with open(file_name, "r") as txt_file:
            data = txt_file.readlines()

    except FileNotFoundError:
        return "File does not exist:"
    
    for line in data:
        line = line.rstrip()  
        print(line)      
        words = [word.lower() for word in line.split(" ")]
        print(words)
        for i in range(len(words)):
            words[i] = "".join([char for char in words[i] if char.isalpha() or char for char in words[i] if ])

        for word in words:
            if str(word) in word_count.keys():
                word_count[word] += 1
            else:
                word_count[word] = 1

    word_count = dict(sorted(word_count.items(), key = lambda x: x[1]))
                       
    remove_items = []
    for word, count in word_count.items():
        if word.strip() == "":
            remove_items.append(word)
    
    for word in remove_items:
        word_count.pop(word)

    print(f"Final list of all words: ")
    print(f"Word | Frequency")
    for word, count in word_count.items():
        print(f"{word} | {count}")

print(count_words("test_file.txt"))