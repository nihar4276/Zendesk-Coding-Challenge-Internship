import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import requests
import application.APIAuthentication as APIAuthentication
import application.config as config

class TicketViewer:

    def __init__(self):
        self.allTicketsEndpoint = config.subdomain + 'api/v2/tickets.json?page[size]=25'
        self.singleTicketEndpoint = config.subdomain + 'api/v2/tickets/'

    def displaySingleTicket(self, ticket):
        """
        A function to display individual ticket information on the CLI
        :param ticket: the ticket python dict that needs to be displayed for user
        :return: None
        """

        print(f"---------------Ticket {ticket['id']} details----------- ")
        print("Ticket Subject: " + ticket['subject'])
        print("created_at: " + ticket['created_at'])
        print("Requester ID: " + str(ticket['requester_id']))
        print("status: " + ticket['status'] if 'status' in ticket and ticket['status'] else "none")
        print("priority " + ticket['priority'] if 'priority' in ticket and ticket['priority'] else "Ticket priority: none")
        print("tags: " + str(ticket['tags']) if 'tags' in ticket and ticket['tags'] else "none")

        while 1:
            print("\n Press B or b to go back to the previous menu \n")
            selection = input()

            if selection.lower() == 'b':
                return
            else:
                print("Invalid option, try again \n")

    def getAllTickets(self):
        """
        A function to get all the tickets by hitting the /tickets zendesk endpoint.
        The tickets are paged in page sizes of 25.

        :return: None
        """
        url = self.allTicketsEndpoint
        prevUrl = ""
        response = {}
        data = {}

        while url:

            try:
                if prevUrl != url:
                    response = requests.get(url, auth=APIAuthentication.APIAuthentication.getBasicAPITokenCreds())

                    # check for 4xx and 5xx error, which means API or request is unhealthy
                    response.raise_for_status()
                    data = response.json()
                else:
                    prevUrl = url

                ticketsCount = len(data['tickets'])

                print("\nEnter the ticket index number to know more about the ticket from the below list, example: 1...25 \n")

                for i, ticket in enumerate(data['tickets']):
                    print("{}. ".format(i+1) + "Ticket subject: " + ticket['subject'] + " opened by "
                          + str(ticket['requester_id']) + " on " + ticket['created_at'])

                if data['meta']['has_more']:
                    print(f" \n Type 'next' to view the next set of tickets\n")

                print(f" Type 'exit' to go to the previous menu\n")

                selection = input()
                proceedNextPage = False

                if selection.lower() == "next":
                    proceedNextPage = True
                elif selection.isnumeric() and int(selection) <= ticketsCount:
                    ticket = data['tickets'][int(selection) - 1]
                    self.getSingleTicket(ticket['id'])
                elif selection.lower() == "exit":
                    return
                else:
                    print("Invalid selection, try again!")
                    continue

                if data['meta']['has_more'] and proceedNextPage == True:
                    url = data['links']['next']
                elif proceedNextPage == True and not data['meta']['has_more']:
                    url = None

            except requests.exceptions.HTTPError as err:
                print("There was error communicating with Zendesk API, please try again letter.")
                print(err)
                sys.exit(1)

    def getSingleTicket(self, id):

        """
        A function to retrieve ticket details according to the id specified by the user
        :param id: The id of the ticket entered by the user
        :return: None (The function will passes the retrieved information to function displaySingleTicket)
        """

        try:
            response = requests.get(self.singleTicketEndpoint + f"{id}.json",
                                    auth=APIAuthentication.APIAuthentication.getBasicAPITokenCreds())
            response.raise_for_status()
            data = response.json()
            self.displaySingleTicket(data['ticket'])

        except requests.exceptions.HTTPError as err:
            print("There was error communicating with Zendesk API, please try again letter.")
            print(err)
            sys.exit(1)
