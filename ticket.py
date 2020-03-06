


class Ticket:

    def __init__(self, s=0,):

        print("\n\n***** TICKET BOOKING *****\n")
        self.s = s



    def TicketBooking(self):

        print("The following are  Category for Ticket :")

        print("SNo:   Category:     Price:")

        print("1.     Child-------- $5:")

        print("2.     Adult-------- $15:")

        print("3.     Senior------- $10:")

        print("4.     Concession----$20:")

        x = int(input(
            '\t\t\tENTER 1,2,3,4 TO YOUR CHOICE OF CATEGORY TO BUY TICKET:'))
        n = int(input(
            '\t\t\tEnter the Number of Ticket you want to BUY TICKET:'))



        if (x == 1):

            print("Category: child")
            self.s = 5 * n



        elif (x == 2):

            print("Category: Adult")
            self.s = 15 * n


        elif (x == 3):

            print("Category: Senior")
            self.s = 10 * n


        elif (x == 4):
            print("Category: Concession")
            self.s = 20 * n


        else:

            print("PLEASE ENTER VALID NUMBER")

        print("Total price:$",self.s, "\n")
        return self.s


















