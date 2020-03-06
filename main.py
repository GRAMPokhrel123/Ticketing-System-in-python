from checkout import Checkout
def main():
    for i in range(2):
        for j in range(90):
            print("*", end="")
        print()
    print("\n\t\t\tThe Federation University Australia Robot Wars Ticket'S")
    print('\t\t\t\t\t\tName: Parminder Pal Singh')
    print('\t\t\t\t\t\tID:   30377649')
    print('\n')

    for i in range(2):
        for j in range(90):
            print("*", end="")
        print()



    def display_tickets():
        a = Checkout()

        digital = a.TicketBooking()
        a.display.append(digital)
        print(a.display)
        result = a.addtolist()
        if result == "a":
            display_tickets()
        else:
            # print('\n')
            print("Total Price:${}".format(sum(a.display)))
            a.cal_ticket()

    display_tickets()

main()







