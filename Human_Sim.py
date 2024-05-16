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
    def __init__(self,GENDER,NAME,PARENT) -> None:
        self.DEAD = False
        self.AGE = 0
        self.NAME = NAME
        self.CHILDREN = []
        self.CHILDREN_COUNT = 0
        self.GENDER = SEX(GENDER)
        self.SPOUSE = None
        self.PARENT = PARENT
        
    def __str__(self) -> str:
        return f'{self.NAME}{","}{self.GENDER}'
    def reproduce(self,partner):
        global Humans
        if self.GENDER.check_reproduce(partner.GENDER):
            if random.randint(0,1) == 1:
                self.CHILDREN_COUNT += 1
                partner.CHILDREN_COUNT += 1
                #print(self.NAME, " and ", partner.NAME,"had sex and made a kid ")
                if random.randint(0,2) == 1:
                    self.CHILDREN.append(HUMAN("MALE", ("Spawn " + str(self.CHILDREN_COUNT)),partner))
                    Humans.append(HUMAN("MALE", ("Spawn " + str(self.CHILDREN_COUNT)),partner))
                else:
                    self.CHILDREN.append(HUMAN("FEMALE", ("Spawn " + str(self.CHILDREN_COUNT)),partner))
                    Humans.append(HUMAN("FEMALE", ("Spawn " + str(self.CHILDREN_COUNT)),partner))
                #print("John the ", self.CHILDREN_COUNT, " has been born")
            else:
                kk = 0
                #print(self.NAME, " and ", partner.NAME," had sex")
def Sim_No1(count2):
    input1 = "y"
    print(count2)
    if count2 < 60 :

        for i in range(len(Humans)):
            if Humans[i].SPOUSE == None:
                #print("attemptioing to find a spouse for ", Humans[i].NAME)
                spouse_num = random.randint(0,len(Humans) - 1)
                if spouse_num != i and Humans[spouse_num].SPOUSE == None:
                    Humans[i].SPOUSE = Humans[spouse_num]
                    Humans[spouse_num].SPOUSE = Humans[i]
                    #print("I found", Humans[i] ," a spouse(", Humans[spouse_num], ")")
                else:
                    funny = 0
                    #print("Couldnt find spouse")
        for j in Humans:
            if j.SPOUSE != None:
                j.reproduce(j.SPOUSE)
        return Sim_No1(count2 + 1)
    time.sleep(.5)
   
    
    

#syo
Humans.append(HUMAN("MALE", "John",None))
Humans.append(HUMAN("FEMALE", "Martha",None))
Humans[0].SPOUSE = Humans[1]
Humans[1].SPOUSE = Humans[0]
Sim_No1(0)
rand = random.randint(0,len(Humans))
print(rand)
for i in range(len(Humans[rand].CHILDREN)):
    print(Humans[rand].CHILDREN[i])
print("Parents")
print(len(Humans))
while Humans[rand].PARENT != None:
    print(Humans[rand].PARENT)
    rand = (Humans.index(Humans[rand].PARENT))

