
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
    LOGOUT_URL = 'https://aleks512-project-v.fr/api/logout/'

    _instance = None # Instance unique de la classe

    @classmethod
    def get_instance(cls, email=None, password=None):
        if cls._instance is None:
            if email is None or password is None:
                raise ValueError("Pour la première utilisation, il est nécessaire de fournir un adresse email et un mot de passe..")
            cls._instance = cls(email, password)
        return cls._instance

    def __init__(self, email, password): # Constructeur de la classe
        if LoginSession._instance is not None:
            raise Exception("This class is a singleton!")
        self.email = email
        self.password = password
        self.headers = {'Content-Type': 'application/json'}
        self.login() # Initiate login upon instance creation

    def login(self): # Méthode pour se connecter
        payload = {"email": self.email, "password": self.password} # Données de connexion
        response = requests.post(self.LOGIN_URL, json=payload, headers=self.headers) # Envoi de la requête POST
        if response.status_code == 200:
            self.access_token = response.json().get("access") # Récupération du token d'accès depuis la réponse
            self.refresh_token = response.json().get("refresh") # Récupération du token de rafraîchissement depuis la réponse
            self.headers['Authorization'] = f'Bearer {self.access_token}' # Mise à jour de l'en-tête avec le nouveau token
        else:
            raise Exception("Login failed")

    # Other methods...

    def refresh_access_token(self): # Méthode pour rafraîchir le token d'accès
        payload = {"refresh_token": self.refresh_token} # Données de rafraîchissement
        response = requests.post(self.REFRESH_URL, json=payload, headers=self.headers) # Envoi de la requête POST
        if response.status_code == 200:
            self.access_token = response.json().get("access" ) # Récupération du nouveau token d'accès
            # Update Authorization header with the new token
            self.headers['Authorization'] = f'Bearer {self.access_token}'
        else:
            raise Exception("Token refresh failed")

    def make_request(self, method, endpoint, data=None): # Méthode pour effectuer une requête
        url = f'{endpoint}'  # Direct use of the full endpoint URL
        response = requests.request(method, url, json=data, headers=self.headers) # Send the request with the provided method and data
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

    def logout(self):
        try:
            payload = {"refresh": self.refresh_token}
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.access_token}'  # Ajouter le token d'accès ici
            }
            print(f"Payload: {payload}")
            print(f"Headers: {headers}")
            response = requests.post('https://aleks512-project-v.fr/api/logout/', json=payload, headers=headers)

            print(f"Logout response status code: {response.status_code}")
            print(f"Logout response content: {response.content}")

            if response.status_code == 205:
                return  # Succès de la déconnexion, pas besoin de renvoyer du JSON
            else:
                raise Exception(f"Failed to logout, status code: {response.status_code}, response: {response.content}")
        except Exception as e:
            raise Exception(f"Logout failed: {str(e)}")


if __name__ == '__main__':
    login_session = LoginSession.get_instance('joe.black@ventalis.com', 'motdepasse')


    # #SEND MESSAGE
    # receiver_email = 'meghan.m@mail.com'
    # content = 'Sroda '
    #
    # message_response = login_session.create_message(receiver_email, content)
    # print(message_response)

    # GET SENT MESSAGES
    # sent_messages = login_session.get_sent_messages()
    # print(sent_messages)

    # GET MESSAGES
    # sent_messages = login_session.get_the_messages()
    # print(sent_messages)

    # GET ORDERS
    # order_items = login_session.get_order_items()
    # print(order_items)

    # UPDATE ORDER
    # Données à mettre à jour
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



