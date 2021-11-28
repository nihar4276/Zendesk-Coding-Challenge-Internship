
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from requests.auth import HTTPBasicAuth
import application.config as config



class APIAuthentication:

    @staticmethod
    def getBasicAPITokenCreds():
        """
        A function to return authentication credentials required for making API requests

        :return: returns the requests.auth.HTTPBasicAuth credentials required for making API requests
        """
        return HTTPBasicAuth(config.username + "/token", config.apiToken)


