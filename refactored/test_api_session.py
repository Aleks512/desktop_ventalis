import unittest
from unittest.mock import patch
from api_session import LoginSession

class TestLoginSession(unittest.TestCase):

    @patch('requests.post')
    def successful_login(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"access": "access_token", "refresh": "refresh_token"}

        session = LoginSession.get_instance('test@test.com', 'password')
        self.assertEqual(session.access_token, "access_token")
        self.assertEqual(session.refresh_token, "refresh_token")

    @patch('requests.post')
    def unsuccessful_login(self, mock_post):
        mock_post.return_value.status_code = 400

        with self.assertRaises(Exception):
            LoginSession.get_instance('test@test.com', 'wrong_password')

    @patch('requests.post')
    def successful_token_refresh(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"access": "new_access_token"}

        session = LoginSession.get_instance('test@test.com', 'password')
        session.refresh_access_token()
        self.assertEqual(session.access_token, "new_access_token")

    @patch('requests.post')
    def unsuccessful_token_refresh(self, mock_post):
        mock_post.return_value.status_code = 400

        session = LoginSession.get_instance('test@test.com', 'password')
        with self.assertRaises(Exception):
            session.refresh_access_token()

    @patch('requests.request')
    def successful_make_request(self, mock_request):
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = {"data": "response_data"}

        session = LoginSession.get_instance('test@test.com', 'password')
        response = session.make_request('GET', 'https://test.com')
        self.assertEqual(response.json(), {"data": "response_data"})

    @patch('requests.request')
    def unsuccessful_make_request(self, mock_request):
        mock_request.return_value.status_code = 400

        session = LoginSession.get_instance('test@test.com', 'password')
        with self.assertRaises(Exception):
            session.make_request('GET', 'https://test.com')

    @patch('requests.request')
    def successful_create_message(self, mock_request):
        mock_request.return_value.status_code = 201
        mock_request.return_value.json.return_value = {"message": "created"}

        session = LoginSession.get_instance('test@test.com', 'password')
        response = session.create_message('receiver@test.com', 'Hello')
        self.assertEqual(response, {"message": "created"})

    @patch('requests.request')
    def unsuccessful_create_message(self, mock_request):
        mock_request.return_value.status_code = 400

        session = LoginSession.get_instance('test@test.com', 'password')
        with self.assertRaises(Exception):
            session.create_message('receiver@test.com', 'Hello')

if __name__ == '__main__':
    unittest.main()