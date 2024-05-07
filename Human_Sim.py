class GENDER():
    def __init__(self,GENDER) -> None:
        self.GENDER = GENDER
    def check_reproduce(self, partner):
        if partner.GENDER != self.GENDER:
            return True
class HUMAN():
    def __init__(self) -> None:
        self.AGE = 0
        self.CHILDREN = 0
        self.GENDER = GENDER()







def main():
    print("Hello")



if __name__ == "main":
    main()