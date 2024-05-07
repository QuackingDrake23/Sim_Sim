class SEX():
    def __init__(self, GENDER) -> None:
        self.GENDER = GENDER

    def __str__(self) -> str:
        return f'{self.GENDER}'

    def check_reproduce(self, partner):
        if partner.GENDER != self.GENDER:
            return True
        else:
            return False

class HUMAN():
    def __init__(self, GENDER) -> None:
        self.AGE = 0
        self.CHILDREN = 0
        self.GENDER = SEX(GENDER)

def main():
    John = HUMAN("Male")
    Martha = HUMAN("Male")  # Correcting Martha's gender
    print(John.GENDER.check_reproduce(Martha.GENDER))

main()