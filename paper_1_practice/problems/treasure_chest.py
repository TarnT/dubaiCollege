
# 1
class TreasureChest:
    def __init__(self, question, answer, points):
        self.__question = question # string
        self.__answer = int(answer) # int
        self.__points = points # int 
    
    # 4
    def getQuestion(self):
        return self.__question
    
    # 5
    def checkAnswer(self, answer):
        return True if self.__answer == answer else False

    def getPoints(self, attempts):
        if attempts == 1:
            return self.__points
        elif attempts == 2:
            return self.__points // 2
        elif attempts in [3,4]:
            return self.__points // 4
        else:
            return 0

# 2
def readData():
    try:
        with open("TreasureChestData.txt", "r") as file:
            lines = file.readlines()    

        arrayTreasure = []
        lines = [i.strip() for i in lines]

        for i in range(0, len(lines), 3):
            chestData = lines[i: i+3]
            arrayTreasure.append(TreasureChest(chestData[0], chestData[1], chestData[2]))

        return arrayTreasure

    except FileNotFoundError:
        print("File does not exist!")
    
    return None

chests = readData()
if chests:
    attempts = 1
    question = int(input("Enter a question number: "))
    print(chests[question - 1].getQuestion())

    while True:
        answer = int(input("Answer: "))
        if chests[question - 1].checkAnswer(answer):
            break
        else:
            print("Incorrect answer!")
            attempts += 1

    points = chests[question - 1].getPoints(attempts)
    print(points)