from random import random
#from pil import Image


class slots:
    money = 0
    def __init__(self, name, moneys):
        self.name = name
        self.money = moneys
        money = moneys
    repeat = True
    while repeat == True:
        print("Here is the amount of money you have: $" + str(money))
        x = input("(To pull) or (Not to pull)?")
        if x == "To pull":
            if money <= 0:
                print("Insufficient Funds... Come back when you have more money")
                repeatBool = input("Go again? (True) or (False)")
                if repeatBool == "True":
                    repeat = True
                    print("Thank you for playing again! Here is what you have: $" + str(money))
                else:
                    repeat = False
                    print ("Goodbye! Here are your earnings $" + str(money) + "!")
            else:
                print("One dollar has been taken out of your account")
                money -= 1
                a = int(((random() * 9) / 3) + 1)
                b = int(((random() * 9) / 3) + 1)
                c = int(((random() * 9) / 3) + 1)
                print(str(a) + " ," + str(b) + " ," + str(c))
                if a == b == c:
                    print("''Tis true  + $5")
                    print("Money before: $" + str(money))
                    money += 5
                    print("Money after: $" + str(money))
                elif a == b or b == c or a == c:
                    print("''Tis semi-true  + $1")
                    print("Money before: $" + str(money))
                    money += 1
                    print("Money after: $" + str(money))
                else:
                    print("''Tis false  - $5")
                    print("Money before: $" + str(money))
                    money -= 5
                    print("Money after: $" + str(money))
                repeatBool = input("Go again? (True) or (False)")
                if repeatBool == "True":
                    repeat = True
                    print("Thank you for playing again!")
                else:
                    repeat = False
                    print ("Goodbye! Here are your earnings $" + str(money) + "!")
        elif x == "Not to pull":
            print("Ok Goodbye; Here are your earnings $" + str(money) + "!")
            repeatBool = input("Go again? (True) or (False)")
            if repeatBool == "True":
                repeat = True
                print("Thank you for playing again! Here is what you have: $" + str(money))
            else:
                repeat = False
                print ("Goodbye! Here are your earnings $" + str(money) + "!")
    # return(money)
#class roulette:
    #image = Image.open('roulette_table')
    #image.show()