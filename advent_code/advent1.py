with open("advent1_external.txt", "r") as file:
    lines = file.readlines()

# total = 0

# for line in lines:
#     print(line)
#     digits = [i for i in line if i.isdigit()]
#     calibration = int(digits[0] + digits[-1])
#     print(calibration)
#     total += calibration

numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

# new_lines = []

# for line in lines:

#     new_line = ""

#     current_word = ""
#     for i in range(len(line)):
#         if i + 1 == len(line):
#             print("final line")
#             print(f"final word is {current_word}")

#         if line[i].isdigit():
#             new_line += line[i]
#             current_word = ""
#             continue

#         current_word += line[i]

#         if current_word in list(numbers.keys()):
#             new_line += str(numbers[current_word])

#             current_word = ""
    
#     print(f"{line} | {new_line}")
#     new_lines.append(new_line)

new_lines = []

for line in lines:
    current_line = line
    for number_string, number in numbers.items():
        current_line = current_line.replace(number_string, str(number))
    print(line, [i for i in current_line if i.isdigit()])
    new_lines.append(current_line)

total = 0

for line in new_lines:
    digits = [i for i in line if i.isdigit()]
    calibration = int(digits[0] + digits[-1])
    total += calibration

print(total)