import TicketViewer

class CLI:

    def __init__(self):
        pass

    def showOptions(self):
        """
        A function to show all the main options of viewing all tickets and a single ticket
        :return: None
        """

        print("Welcome to Zendesk coding challenge")
        tv = TicketViewer.TicketViewer()

        while 1:
            print("Enter one of the following options:")

            print("1: View all tickets of your account")
            print("2. View details of a ticket by ID")
            print("3. Exit")

            selection = input()

            if selection.isnumeric() == False:
                print("Invalid option, try again!\n")
                continue

            if selection == '1':
                tv.getAllTickets()
            elif selection == '2':
                id = input("Enter id of the ticket you want information for: ")

                if not id.isnumeric():
                    print("Invalid id format, try again!\n")
                    continue

                tv.getSingleTicket(int(id))
            elif selection == '3':
                return
            else:
                print("Invalid option, try again!\n")

CLI().showOptions()
