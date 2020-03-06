import re
from ticket import Ticket


class Checkout(Ticket):

    display = []


    def __init__(self, s=0):
        Ticket.__init__(self, s=0)

    def addtolist(self):
        while(True):
            add = input('\t\t\tType a To Add New To List or c To Checkout or e to Exit:')
            if add == "a":
                return add

            elif add == 'c':
            # print(Checkout.display)
                return add

            elif add == 'e':
                exit()

            else:
                print("\t\t\tNot a valid option")



    def cal_ticket(self):
        while(True):
            display = sum(Checkout.display)
            credit = input("Enter the CREDIT-CARD number at-least 4 digit:")
            flag = 0
            while(True):
                if (len(credit) < 4):
                    flag = -1
                    break
                elif not re.search("[0-9]", credit):
                    flag = -1
                    break

                elif re.search("\s", credit):
                    flag = -1
                    break
                else:
                    flag = 0
                    print("Card Accepted")
                    break

            if flag == -1:
                print("Card Not Accepted")
                print("TRY AGAIN With VALID CARD")
                break

            if (credit.isdigit()):
                f = open("recipe.txt", "w")
                f.write('TOTAL Price: $')
                f.write(str(display))
                f.close()
                break
            else:
                print("PLEASE ENTER VALID NUMBER")