# import requests
#
# class LoginSession:
#     LOGIN_URL = 'https://aleks512-project-v.fr/api/token/'
#     REFRESH_URL = 'https://aleks512-project-v.fr/api/token/refresh/'
#     CREATE_MESSAGE_URL = 'https://www.aleks512-project-v.fr/consultant-create-message/'
#     MESSAGES_URL = 'https://www.aleks512-project-v.fr/consultant-read-messages/'
#     SENT_MESSAGES_URL = 'https://www.aleks512-project-v.fr/consultant-sent-messages/'
#     GET_ORDERS_URL = 'https://www.aleks512-project-v.fr/consultant-orderitems/'
#     UPDATE_ORDER_URL = 'https://www.aleks512-project-v.fr/consultant-orderitem-update/'
#
#     def __init__(self, email, password):
#         self.email = email
#         self.password = password
#         self.headers = {'Content-Type': 'application/json'}
#         self.access_token = None
#         self.refresh_token = None
#         self.login()  # Initiate login upon instance creation
#
#     def login(self):
#         payload = {"email": self.email, "password": self.password}
#         response = requests.post(self.LOGIN_URL, json=payload, headers=self.headers)
#         if response.status_code == 200:
#             self.access_token = response.json().get("access")
#             self.refresh_token = response.json().get("refresh")
#             # Update Authorization header with the new token
#             self.headers['Authorization'] = f'Bearer {self.access_token}'
#             print("access token", self.access_token)
#         else:
#             raise Exception("Invalid credentials")
#
#     def refresh_access_token(self):
#         payload = {"refresh_token": self.refresh_token}
#         response = requests.post(self.REFRESH_URL, json=payload, headers=self.headers)
#         if response.status_code == 200:
#             self.access_token = response.json().get("access")
#             # Update Authorization header with the new token
#             self.headers['Authorization'] = f'Bearer {self.access_token}'
#         else:
#             raise Exception("Token refresh failed")
#
#     def make_request(self, method, endpoint, data=None):
#         url = f'{endpoint}'  # Direct use of the full endpoint URL
#         response = requests.request(method, url, json=data, headers=self.headers)
#         if response.status_code == 401:  # Unauthorized, token might have expired
#             self.refresh_access_token()
#             response = requests.request(method, url, json=data, headers=self.headers)  # Retry the request with the new token
#         return response
#
#     def create_message(self, receiver_email, content):
#         data = {
#             "receiver_email": receiver_email,
#             "content": content
#         }
#         response = self.make_request('POST', self.CREATE_MESSAGE_URL, data=data)
#         if response.status_code == 201:
#             return response.json()  # Successfully created the message
#         else:
#             raise Exception(f"Failed to create message, status code: {response.status_code}")
#
#     def get_the_messages(self):
#         response = self.make_request('GET', self.MESSAGES_URL)
#         if response.status_code == 200:
#             return response.json()  # Successfully retrieved messages
#         else:
#             raise Exception(f"Failed to retrieve messages, status code: {response.status_code}")
#
#     def get_sent_messages(self):
#         response = self.make_request('GET', self.SENT_MESSAGES_URL)
#         if response.status_code == 200:
#             return response.json()  # Successfully retrieved messages
#         else:
#             raise Exception(f"Failed to retrieve messages, status code: {response.status_code}")
#
#     def get_order_items(self):
#         response = self.make_request('GET', 'https://www.aleks512-project-v.fr/consultant-orderitems/')
#         if response.status_code == 200:
#             return response.json()  # Retourne les données JSON de la réponse
#         else:
#             raise Exception(
#                 f"Failed to retrieve order items, status code: {response.status_code}, details: {response.json().get('detail')}")
#
#     def patch_order_item(self, item_id, data):
#         endpoint = f'https://www.aleks512-project-v.fr/consultant-orderitem-update/{item_id}/'
#         response = self.make_request('PATCH', endpoint, data=data)
#         if response.status_code == 200:
#             return response.json()  # Retourne les données mises à jour de l'item
#         else:
#             raise Exception(
#                 f"Failed to update order item, status code: {response.status_code}, details: {response.text}")
#
#
# if __name__ == '__main__':
#     login_session = LoginSession('joe.black@ventalis.com', 'MerryChristmas&12')
# # GET ORDERS
#     order_items = login_session.get_order_items()
#     print(order_items)
# # UPDATE ORDER
# # Données à mettre à jour
#     update_data = {
#         "status": "P",  # Exemple de mise à jour du statut
#         "comment": "Updated comment"  # Exemple de mise à jour d'un commentaire
#     }
#
# # ID de l'item de commande à mettre à jour
#     item_id = 123
#
# # Appel de la méthode pour mettre à jour l'item
#     updated_item = login_session.patch_order_item(item_id, update_data)
#     print(updated_item)


############################################SINGELTON#################################################
import requests

class LoginSession:
    LOGIN_URL = 'https://aleks512-project-v.fr/api/token/'
    REFRESH_URL = 'https://aleks512-project-v.fr/api/token/refresh/'
    CREATE_MESSAGE_URL = 'https://www.aleks512-project-v.fr/consultant-create-message/'
    MESSAGES_URL = 'https://www.aleks512-project-v.fr/consultant-read-messages/'
    SENT_MESSAGES_URL = 'https://www.aleks512-project-v.fr/consultant-sent-messages/'
    GET_ORDERS_URL = 'https://www.aleks512-project-v.fr/consultant-orderitems/'
    UPDATE_ORDER_URL = 'https://www.aleks512-project-v.fr/consultant-orderitem-update/'

    _instance = None

    @classmethod
    def get_instance(cls, email=None, password=None):
        if cls._instance is None:
            if email is None or password is None:
                raise ValueError("Pour la première utilisation, il est nécessaire de fournir un adresse email et un mot de passe..")
            cls._instance = cls(email, password)
        return cls._instance

    def __init__(self, email, password):
        if LoginSession._instance is not None:
            raise Exception("This class is a singleton!")
        self.email = email
        self.password = password
        self.headers = {'Content-Type': 'application/json'}
        self.login()

    def login(self):
        payload = {"email": self.email, "password": self.password}
        response = requests.post(self.LOGIN_URL, json=payload, headers=self.headers)
        if response.status_code == 200:
            self.access_token = response.json().get("access")
            self.refresh_token = response.json().get("refresh")
            self.headers['Authorization'] = f'Bearer {self.access_token}'
        else:
            raise Exception("Login failed")

    # Other methods...

    def refresh_access_token(self):
        payload = {"refresh_token": self.refresh_token}
        response = requests.post(self.REFRESH_URL, json=payload, headers=self.headers)
        if response.status_code == 200:
            self.access_token = response.json().get("access")
            # Update Authorization header with the new token
            self.headers['Authorization'] = f'Bearer {self.access_token}'
        else:
            raise Exception("Token refresh failed")

    def make_request(self, method, endpoint, data=None):
        url = f'{endpoint}'  # Direct use of the full endpoint URL
        response = requests.request(method, url, json=data, headers=self.headers)
        if response.status_code == 401:  # Unauthorized, token might have expired
            self.refresh_access_token()
            response = requests.request(method, url, json=data,
                                        headers=self.headers)  # Retry the request with the new token
        return response

    def create_message(self, receiver_email, content):
        data = {
            "receiver_email": receiver_email,
            "content": content
        }
        response = self.make_request('POST', self.CREATE_MESSAGE_URL, data=data)
        if response.status_code == 201:
            return response.json()  # Successfully created the message
        else:
            raise Exception(f"Failed to create message, status code: {response.status_code}")

    def get_the_messages(self):
        response = self.make_request('GET', self.MESSAGES_URL)
        if response.status_code == 200:
            return response.json()  # Successfully retrieved messages
        else:
            raise Exception(f"Failed to retrieve messages, status code: {response.status_code}")

    def get_sent_messages(self):
        response = self.make_request('GET', self.SENT_MESSAGES_URL)
        if response.status_code == 200:
            return response.json()  # Successfully retrieved messages
        else:
            raise Exception(f"Failed to retrieve messages, status code: {response.status_code}")

    def get_order_items(self):
        response = self.make_request('GET', 'https://www.aleks512-project-v.fr/consultant-orderitems/')
        if response.status_code == 200:
            return response.json()  # Retourne les données JSON de la réponse
        else:
            raise Exception(
                f"Failed to retrieve order items, status code: {response.status_code}, details: {response.json().get('detail')}")

    def patch_order_item(self, item_id, data):
        endpoint = f'https://www.aleks512-project-v.fr/consultant-orderitem-update/{item_id}/'
        response = self.make_request('PATCH', endpoint, data=data)
        if response.status_code == 200:
            return response.json()  # Retourne les données mises à jour de l'item
        else:
            raise Exception(
                f"Failed to update order item, status code: {response.status_code}, details: {response.text}")

if __name__ == '__main__':
    login_session = LoginSession.get_instance('joe.black@ventalis.com', 'MerryChristmas&12')


    # #SEND MESSAGE
    # receiver_email = 'meghan.m@mail.com'
    # content = 'Sroda '
    #
    # message_response = login_session.create_message(receiver_email, content)
    # print(message_response)

    # # GET SEBT MESSAGES
    # sent_messages = login_session.get_sent_messages()
    # print(sent_messages)

    # GET MESSAGES
    sent_messages = login_session.get_the_messages()
    print(sent_messages)

    # GET ORDERS
    # order_items = login_session.get_instance().get_order_items()
    # print(order_items)

    # # UPDATE ORDER
    # # Données à mettre à jour
    # update_data = {
    #     "status": "P",  # Exemple de mise à jour du statut
    #     "comment": "Updated comment"  # Exemple de mise à jour d'un commentaire
    # }
    #
    # # ID de l'item de commande à mettre à jour
    # item_id = 123
    #
    # # Appel de la méthode pour mettre à jour l'item
    # updated_item = login_session.patch_order_item(item_id, update_data)
    # print(updated_item)



