import vk
import getpass

APP_ID = 6274359


def get_user_login():
    login_vk = input('Type login VK: ')
    return login_vk


def get_user_password():
    password_vk = getpass.getpass('Type your password: ')
    return password_vk


def get_online_friends(accaunt_login, accaunt_password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=accaunt_login,
        user_password=accaunt_password,
        scope='friends'
    )
    api = vk.API(session)
    return api.getProfiles(user_ids=api.friends.getOnline())


def output_friends_to_console(friends_online_vk):
    print('Friends online: ')
    for friend in friends_online_vk:
            print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
