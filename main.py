import requests

token = 'f5cb4ce132708150d1e8b7f1bd2f0bc2de8bf812d6586780d648408f9bb0e023db9195d75ed0d413e4538'
params = {
    'access_token': token,
    'v': '5.92',
}


class User:
    id = ''
    first_name = ''
    last_name = ''


    def __init__(self, id, name, surname):
        self.id = id
        self.first_name = name
        self.last_name = surname

    def __and__(self, user):

        mutual_friend_list = []

        params['source_uid'] = self.id

        params['target_uid'] = user.id

        mutual_friends = requests.get('https://api.vk.com/method/friends.getMutual', params).json()

        params.pop('source_uid')
        params.pop('target_uid')


        for id in mutual_friends['response']:

            params['user_id'] = id
            response = requests.get('https://api.vk.com/method/users.get', params).json()
            id = response['response'][0]['id']
            first_name = response['response'][0]['first_name']
            last_name = response['response'][0]['last_name']
            mutual_friend_list.append(User(id, first_name, last_name))

        return mutual_friend_list



def main():

    user1 = User('4917618', 'Mark', 'Cole')

    user2 = User('9819150', 'Дмитрий', 'Груша')

    mutual_friends = user1 & user2

    for friend in mutual_friends:
        print(str(friend.id) + ' ' + friend.first_name + ' ' + friend.last_name)


if __name__ == '__main__':
    main()
