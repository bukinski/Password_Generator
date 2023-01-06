import string
import random
import sys

## characters to generate password from
charactersLowerCase = list(string.ascii_letters.lower())
charactersUpperCase = list(string.ascii_letters.upper())
digits = list(string.digits)
specialCharacters = list("!@#$%^&*(),")

def GeneratePW(upper, lower, digits, special):
    PW = list()
    PWLenghtInt = (int(input("Input desired password length: ")))
    #print(PWLenghtInt/4)
    for i in range (0, int(PWLenghtInt)):
        PW.append(random.choice(upper))
        PW.append(random.choice(lower))
        PW.append(random.choice(digits))
        PW.append(random.choice(special))
    
    #print(PW)

    PW = PW[0:PWLenghtInt]
    random.shuffle(PW)
    print("Your random password: ")
    print(''.join(PW))

GeneratePW(charactersUpperCase, charactersLowerCase, digits, specialCharacters)

while True:
    choice = input("Create different password? yes/no:  ")
    if choice == "yes":
        GeneratePW(charactersUpperCase, charactersLowerCase, digits, specialCharacters)
    else:
        sys.exit()