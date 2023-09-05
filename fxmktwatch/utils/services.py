"""
contains services needed to make transactions
"""
import enum
import requests
import os

class ServiceStatus(enum.Enum):
    """
    indicate the status of services
    """
    loading = 'loading'
    error = 'error'
    success = 'success'

class TelegramServices:
    _token = os.environ.get('TELEGRAM_API_KEY')

    def __init__(self, chat_id=None):
        if( chat_id ):
            self.chat_id = chat_id

    def get_messages(self):
        url = f'https://api.telegram.org/bot{self._token}/getUpdates'
        start_at = 0
        response = None

        if os.path.exists('lastread'):
            with open("lastread", "r") as file:
                start_at = int(file.readline())
                print(type(start_at))

        if(start_at > 0):
            params = {'offset': start_at, 'limit': 100}
            response= requests.post(url, params=params).json()
        else:
            response = requests.post(url).json()

        if response.get('result'):
            with open("lastread", "w") as file:
                file.write(str(response.get('result')[-1].get('update_id')))

        return response


        # print(response)
        # print(response.get('result')[0].get('update_id'))
        # print(response.get('result')[0].get('message').get('from').get('is_bot')) #is bot
        # print(response.get('result')[0].get('message').get('from').get('username'))
        # print(response.get('result')[0].get('message').get('chat').get('id')) #chat id
        # print(response.get('result')[0].get('message').get('text')) #message
        # print(response.get('result')[0].get('message').get('date')) #is bot

        # return response

    def search_code(self,acct_id, code):
        message_data = self.get_messages()
        print(code)
        for item in message_data.get('result'):
            # print (item.get('message').get('text'))
            # print(item)
            if item.get('message').get('from').get('username') == acct_id[1:] and\
            item.get('message').get('text') == str(code):
                print('code found')
                self.chat_id = item.get('message').get('chat').get('id')
                return self.chat_id
        return None
    
    def send_message(self, message, chat_id):
        url = f'https://api.telegram.org/bot{self._token}/sendMessage'
        data = {'chat_id': chat_id, 'text': message}

        response = requests.post(url, data).json()
        print(response)

    def send_success(self):
        if self.chat_id != None:
            self.send_message(
                f'Welcome to Fx-market-watch bot service\nYour account have been acativated',
                self.chat_id
                )