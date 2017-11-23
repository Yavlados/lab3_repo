from clientVK import *
from histogram import Hist
import matplotlib.pyplot as plt


def main():
    username = input('Введите логин VK: ')

    client_get_id = ClientGetID(username)
    user_id = client_get_id.execute()

    if client_get_id.is_success():
        print("ID: ", user_id)
    else:
        print('Не существует пользователя с таким ID.')
        return 0

    # find age list
    friends_ages_list = ClientGetFriendsAges(user_id).execute()
    if not friends_ages_list:
        print('Друзей не найдено')
        return 0
    else:
        print("Ages: ", friends_ages_list)
        # write gist
        username_friend_gist = Hist(friends_ages_list)
        username_friend_gist.printGist()

    # show gist
    title = "Гистограмма"
    title_x = "Возраст"
    title_y = "Количество друзей"
    username_friend_gist.showBar(title, title_x, title_y)


if  __name__ ==  "__main__" : main()