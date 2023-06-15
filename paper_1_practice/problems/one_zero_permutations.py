from itertools import permutations

def numPermutations(zeros, ones):

    # generate all possible permutations
    all = ["".join(i) for i in permutations(f"{'1' * ones}{'0' * zeros}")]

    all = list(set(all))

    criterion = []

    for permutation in all:

        consecutive_count_1 = 1
        add_to_list = True

        for i in range(len(permutation) - 1):
            if permutation[i] == permutation[i + 1] and permutation[i] == "1":
                consecutive_count_1 += 1
            
            elif permutation[i] == "1" and permutation[i + 1] == "0":
                if consecutive_count_1 % 2 == 0:
                    add_to_list = False
                    break
                else:
                    consecutive_count_1 = 1
        
        if consecutive_count_1 % 2 == 0:
            add_to_list = False 
        
        if add_to_list:
            criterion.append(permutation)

    return len(criterion), criterion

print(numPermutations(2, 5))