import time
import random
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
        self.SPOUSE = []
    def reproduce(self,partner):
        if self.GENDER.check_reproduce(partner.GENDER):
            if random.randint(0,1) == 1:
                self.CHILDREN_COUNT += 1
                print(self.NAME, " and ", partner.NAME,"had sex and made a kid ")
                self.CHILDREN.append(HUMAN("MALE", ("Spawn " + str(self.CHILDREN_COUNT))))
                print("John the ", self.CHILDREN_COUNT, " has been born")
            else:
                print(self.NAME, " and ", partner.NAME," had sex")
def Sim_No1():
    Humans = []
    input1 = ""
    while input1 != "Y" and input1 != "y" :
        Humans.append(HUMAN(input("Gender for Human 1 -> "), input("Name for Human 1 -> ")))
        Humans.append(HUMAN(input("Gender for Human 2 -> "), input("Name for Human 2 -> ")))
        for i in range(len(Humans)):
            print("[",end = "")
            print(Humans[i].NAME, ",", Humans[i].GENDER, end = "]")
        input1 = input(" Are these your starting humnans? Y/N -> ")
    for i in range(len(Humans)):
        try:
            Humans.append(Humans[i].reproduce(Humans[i + 1]))
        except:
            print("All done")
    for i in range(len(Humans)):
        print("[",end = "")
        print(Humans[i].NAME, ",", Humans[i].GENDER, end = "]")

#syo
Sim_No1()
