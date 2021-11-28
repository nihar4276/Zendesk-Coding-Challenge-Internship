import unittest
import os
os.environ['username'] = "my_username"
os.environ['token'] = "your_token"
os.environ['subdomain'] = "any_subdomain"
import application.TicketViewer as TicketViewer
from unittest.mock import patch


class TicketViewerTests(unittest.TestCase):

    @patch.object(TicketViewer, 'input', return_value='B')
    def test_displaySingleTicket(self, inputMock):
        inputMock.return_value = 'B'
        tv = TicketViewer.TicketViewer()
        tv.displaySingleTicket({'id': 2, 'subject': 'hola', 'created_at': '12-12-2021 3:15PM',
                                'requester_id': 3, 'status': 'normal'})

    @patch.object(TicketViewer, 'input', return_value='B')
    @patch.object(TicketViewer, 'requests')
    def test_getSingleTicket(self, inputMock, requestsMock):
        requestsMock.get.return_value = {}
        tv = TicketViewer.TicketViewer()
        tv.getSingleTicket(2)

    @patch.object(TicketViewer, 'input', return_value=1)
    @patch.object(TicketViewer, 'requests')
    def test_getAllTickets(self, inputMock, requestsMock):
        requestsMock.get.return_value = {}
        tv = TicketViewer.TicketViewer()
        tv.getSingleTicket(2)

if __name__ == '__main__':
    unittest.main()
