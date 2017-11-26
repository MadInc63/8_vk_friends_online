import vk
import getpass

APP_ID = 6274359


def get_user_login():
    login_vk = input('Type login VK: ')
    return login_vk


def get_user_password():
    password_vk = getpass.getpass('Type your password: ')
    return password_vk


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    my_friend_status = api.friends.get(fields='online')
    return my_friend_status


def output_friends_to_console(friends_online):
    print('Friends online: ')
    for friend in friends_online:
        if friend['online'] == 1:
            print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
