import unittest
import os
os.environ['username'] = "my_username"
os.environ['token'] = "your_token"
os.environ['subdomain'] = "any_subdomain"
import application.APIAuthentication


class APIAuthenticationTests(unittest.TestCase):

    def test_getBasicAPITokenCreds(self):
        auth = application.APIAuthentication.APIAuthentication.getBasicAPITokenCreds()
        self.assertEqual(auth.username, 'my_username/token')
        self.assertEqual(auth.password, 'your_token')


if __name__ == '__main__':
    unittest.main()
