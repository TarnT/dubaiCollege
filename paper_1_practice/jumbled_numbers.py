class Jumble:
    def __init__(self):
        self.num = input("Enter a number:")
    
    def checkJumbled(self):
        jumbled = True
        if len(self.num) == 1:
            pass
        elif len(self.num) == 2:
            if abs(int(self.num[0]) - int(self.num[1])) >= 2:
                jumbled = False
        else:
            jumbled = True 
            for i in range(1, len(self.num) - 1):
                if abs(int(self.num[i]) - int(self.num[i+1])) >= 2 or abs(int(self.num[i]) - int(self.num[i - 1])) >= 2:
                    jumbled = False
        if jumbled:
            return "Output: True, all neighbouring digits differ by a maximum of 1
        else:
            return "Output: False"


new = Jumble()
print(new.checkJumbled())
