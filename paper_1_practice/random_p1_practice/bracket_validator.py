def bracket_validator(string):

    brackets = [i for i in string if i in "()"]

    if len(brackets) % 2 == 1:
        return "Brackets are not valid"

    for i in range(len(brackets) // 2):

        if (brackets[-i+1] == ")" and brackets[i] == "(") or brackets[-i+1] == "(" and brackets[i] == ")":
            continue
        else:
            return "Brackets are not valid"


    return "Brackets are valid"

string = "11+4*)+(15"
print(f"Entering {string}")
print(bracket_validator(string))