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
        self.SPOUSE = HUMAN()
    def reproduce(self,partner):
        if self.GENDER.check_reproduce(partner.GENDER):
            if random.randint(0,1) == 1:
                self.CHILDREN_COUNT += 1
                print(self.NAME, " and ", partner.NAME,"had sex and made a kid ")
                self.CHILDREN.append(HUMAN("MALE", ("Spawn " + str(self.CHILDREN_COUNT))))
                print("John the ", self.CHILDREN_COUNT, " has been born")
            else:
                print(self.NAME, " and ", partner.NAME," had sex")
 
def John_Martha():
    John = HUMAN("Male","John")
    Martha = HUMAN("Female","Martha")
    stop = True
    while stop:
        if John.DEAD == False and Martha.DEAD == False:
            if random.randint(0,40) != 40:
                John.reproduce(Martha)
                time.sleep(1)
            else:
                if random.randint(0,1) == 1:
                    John.DEAD = True
                    print("John Died")
                    stop = False
                    print("[ ", end= "")
                    for i in range(len(John.CHILDREN)):
                        print(John.CHILDREN[i].NAME, end=" ")
                    print("]")
                else:
                    Martha.DEAD = True
                    print("Martha Died")
                    stop = False
                    print("[", end= "")
                    for i in range(len(John.CHILDREN)):
                        print(John.CHILDREN[i].NAME, end=" ")
                    print("]")
                    
if input("What do you want to do (run) -> ").upper() == "RUN":
    John_Martha()
else:
    print()
