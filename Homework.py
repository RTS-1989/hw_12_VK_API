import requests, json

token = '50d900525efbaa52a2506ebe5547cf58206fedcb4a745880c4ee3304ccd3c10088c62769cf58d0769c6f5'

class User:

    def __init__(self, user_id: int):
        self.token = token
        self.user_id = user_id

    def __str__(self):
        return str(self.user_id)

    def get_mutual_friends(self, other_user):

        params = {
                  'access_token': self.token,
                  'v': 5.107,
                  'source_uid': self,
                  'target_uid': other_user
                  }

        response = requests.get('https://api.vk.com/method/friends.getMutual', params)

        return response.json()

    def __and__(self, other_user):
        return self.get_mutual_friends(other_user)['response']

user1 = User(175876682)
user2 = User(23542487)

common_friends = user1 & user2

print('Ссылки на список общих друзей:')

for user in common_friends:
    print(f'https://vk.com/id{user}')

