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
                raise ValueError("Email and password must be provided for the first instantiation.")
            cls._instance = cls(email, password)
        return cls._instance

    def __init__(self, email, password):
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

    def refresh_access_token(self):
        payload = {"refresh_token": self.refresh_token}
        response = requests.post(self.REFRESH_URL, json=payload, headers=self.headers)
        if response.status_code == 200:
            self.access_token = response.json().get("access")
            self.headers['Authorization'] = f'Bearer {self.access_token}'
        else:
            raise Exception("Token refresh failed")

    def make_request(self, method, endpoint, data=None):
        url = f'{endpoint}'
        response = requests.request(method, url, json=data, headers=self.headers)
        if response.status_code == 401:
            self.refresh_access_token()
            response = requests.request(method, url, json=data, headers=self.headers)
        return response

    def create_message(self, receiver_email, content):
        data = {"receiver_email": receiver_email, "content": content}
        return self.make_request('POST', self.CREATE_MESSAGE_URL, data=data)

    def get_the_messages(self):
        return self.make_request('GET', self.MESSAGES_URL)

    def get_sent_messages(self):
        return self.make_request('GET', self.SENT_MESSAGES_URL)

    def get_order_items(self):
        return self.make_request('GET', self.GET_ORDERS_URL)

    def patch_order_item(self, item_id, data):
        endpoint = f'{self.UPDATE_ORDER_URL}/{item_id}/'
        return self.make_request('PATCH', endpoint, data=data)

# Utilisation de l'instance pour envoyer un message et manipuler d'autres fonctions
if __name__ == '__main__':
    # Initialisation de l'instance avec des identifiants (à titre d'exemple)
    login_session = LoginSession.get_instance('joe.black@ventalis.com', 'MerryChristmas&12')

    # Envoyer un email à meghan.m@mail.com avec le contenu "hello from pyside"
    message_response = login_session.create_message('meghan.m@mail.com', 'hello from pyside')
    print('Message envoyés: ',message_response)  # Affiche la réponse de la création de message

    # Exemple de récupération des messages reçus
    received_messages = login_session.get_the_messages()
    print('Message reçus : ',received_messages)  # Affiche les messages reçus

    # Exemple de récupération des messages envoyés
    sent_messages = login_session.get_sent_messages()
    print('Message envoyés : ', sent_messages)  # Affiche les messages envoyés

    # Exemple de récupération des commandes
    orders = login_session.get_order_items()
    print(orders)  # Affiche les commandes

    # Exemple de mise à jour d'une commande
    #update_data = {'status': 'Processed', 'comment': 'Updated by script'}
    #updated_order_response = login_session.patch_order_item(123, update_data)
    #print(updated_order_response)  # Affiche la réponse à la mise à jour de la commande
