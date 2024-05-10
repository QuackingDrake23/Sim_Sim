import time
import random
global Humans 
Humans = []
class SEX():
    def __init__(self,GENDER) -> None:
        self.GENDER = GENDER.upper()
    def __str__(self) -> str:
        return f'{self.GENDER}'
    def check_reproduce(self, partner):
        if partner.GENDER != self.GENDER:
            return True
        else:
            return False
class HUMAN():
    def __init__(self,GENDER,NAME) -> None:
        self.DEAD = False
        self.AGE = 0
        self.NAME = NAME
        self.CHILDREN = []
        self.CHILDREN_COUNT = 0
        self.GENDER = SEX(GENDER)
        self.SPOUSE = None
    def __str__(self) -> str:
        return f'{self.NAME}{","}{self.GENDER}'
    def reproduce(self,partner):
        global Humans
        if self.GENDER.check_reproduce(partner.GENDER):
            if random.randint(0,1) == 1:
                self.CHILDREN_COUNT += 1
                partner.CHILDREN_COUNT += 1
                print(self.NAME, " and ", partner.NAME,"had sex and made a kid ")
                if random.randint(0,2) == 1:
                    self.CHILDREN.append(HUMAN("MALE", ("Spawn " + str(self.CHILDREN_COUNT))))
                    Humans.append(HUMAN("MALE", ("Spawn " + str(self.CHILDREN_COUNT))))
                else:
                    self.CHILDREN.append(HUMAN("FEMALE", ("Spawn " + str(self.CHILDREN_COUNT))))
                    Humans.append(HUMAN("FEMALE", ("Spawn " + str(self.CHILDREN_COUNT))))
                print("John the ", self.CHILDREN_COUNT, " has been born")
            else:
                print(self.NAME, " and ", partner.NAME," had sex")
def Sim_No1():
    input1 = "y"
    Humans.append(HUMAN(input("Gender for Human 1 -> "), input("Name for Human 1 -> ")))
    Humans.append(HUMAN(input("Gender for Human 2 -> "), input("Name for Human 2 -> ")))
    Humans[0].SPOUSE = Humans[1]
    Humans[1].SPOUSE = Humans[0]
    count = 0
    while input1 == "Y" or input1 == "y" :
        for i in range(len(Humans)):
            if Humans[i].SPOUSE == None:
                print("attemptioing to find a spouse for ", Humans[i].NAME)
                spouse_num = random.randint(0,len(Humans) - 1)
                if spouse_num != i and Humans[spouse_num].SPOUSE == None:
                    Humans[i].SPOUSE = Humans[spouse_num]
                    Humans[spouse_num].SPOUSE = Humans[i]
                    print("I found", Humans[i] ," a spouse(", Humans[spouse_num], ")")
                else:
                    print("Couldnt find spouse")
        for i in range(len(Humans)):
            print("[",end = "")
            print(Humans[i].NAME, ",", Humans[i].GENDER, end = "]")
        for i in Humans:
            if i.SPOUSE != None:
                i.reproduce(i.SPOUSE)
        for i in range(len(Humans)):
            print("[",end = "")
            print(Humans[i], end = "]")
        time.sleep(.5)
        if count == 2000:
            input1 = input("Keep going ")
            count = 0

#syo
Sim_No1()
