import datetime
import vk_api
from random import randint
import keyboards_main
import mysql.connector
import time

start_time = time.time()
token = "vk1.a.xJtuB7m06aJ0NUxP76zraFp_CKdCAlFGi_QozpaM3-7oa9lqoJ7jjFQ6DALQmbCCl3MFq7Twz_SwjX-AWisGcZ5spY0GEvP4E0efgDNl7XaNfwURZ8kdWALjoYkwlpFMwr_p8_Qvtr1ruinz4BR4J6O3dthRR0U0d_0mGzH-20BKIZ-BzXU3VIShwuUJUfx3"
vk = vk_api.VkApi(token=token)
vk._auth_token()
b = 0


def db_connection_insert(string):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='12451245',
            database='fantasy'
        )
        with connection.cursor() as mycursor:
            mycursor.execute(string)
            connection.commit()
            print('данные успешно записаны')
    except Exception as ex:
        print('Ошибка ', ex)


def db_connection_select(string):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='12451245',
            database='fantasy'
        )
        with connection.cursor() as mycursor:
            mycursor.execute(string)
            result = mycursor.fetchall()
            for x in result:
                return x
    except Exception as ex:
        print('Ошибка ', ex)


def writing(print_text, us_id, k_b):
    global b
    a = (vk.method("messages.send", {"user_id": us_id, "message": print_text, "random_id": randint(1, 1000),
                                     "keyboard": k_b.get_keyboard()}))
    while a < b:
        print('Ошибка отправки')
        a = (vk.method("messages.send", {"user_id": us_id, "message": print_text, "random_id": randint(1, 1000),
                                         "keyboard": k_b.get_keyboard()}))
    b = a


def writing_only_text(print_text, us_id):
    global b
    a = (vk.method("messages.send", {"user_id": us_id, "message": print_text, "random_id": randint(1, 1000)}))
    while a < b:
        print('Ошибка отправки')
        a = (vk.method("messages.send", {"user_id": us_id, "message": print_text, "random_id": randint(1, 1000)}))
    b = a


def searching_in_db(vk_id):
    return db_connection_select(f'SELECT * FROM users WHERE vk_id = {vk_id} LIMIT 1;')


def map_extractiom(vk_id):
    pass


class Player:

    room = 0
    part = 'main'

    def __init__(self, name, vk_id, player_id, country, level, location_id, race, born, experience, mem_time):
        self.name = name
        self.vk_id = vk_id
        self.id = player_id
        self.country = country
        self.level = level
        self.location_id = location_id
        self.race = race
        self.born = born
        self.experience = experience
        self.mem_time = mem_time


class PlayerInRegistration:
    name = ''
    country = ''
    location = ''
    race = ''
    mem_time = ''
    room = 1

    def __init__(self, vk_id, mem_time):
        self.vk_id = vk_id
        self.mem_time = mem_time


players = []
list_of_players_id = []

while True:
    try:
        start_time = time.time()
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        # print("%s секунд на проверку наличия сообщений" % (time.time() - start_time))
        if messages["count"] >= 1:
            # start_time = time.time()
            text = messages['items'][0]['last_message']['text']
            user_id = messages['items'][0]['last_message']['from_id']
            # print("%s секунд на получение текста и id пользователя" % (time.time() - start_time))
            if user_id not in list_of_players_id:
                user_now = searching_in_db(int(f'{user_id}'))
                if user_now is None:
                    if text == "Регистрация":
                        print('регистрация игрока в базе данных')
                        players.append(PlayerInRegistration(user_id, time.time()))
                        list_of_players_id.append(user_id)
                        writing_only_text('Введи своё игровое имя', user_id)
                    else:
                        writing_only_text("Введи 'Регистрация', начнём твою регистрацию в игре", user_id)
                else:
                    list_of_players_id.append(user_now[2])
                    print(list_of_players_id)
                    players.append(Player(user_now[1], user_now[2], user_now[0], user_now[3], user_now[6], user_now[7],
                                          user_now[5], user_now[4], user_now[8], time.time()))
            elif user_id in list_of_players_id:
                for player in players:
                    if player.vk_id == user_id:
                        if type(player) == PlayerInRegistration:
                            if player.room == 1:
                                player.name = text
                                player.room = 2
                                writing('Выбери страну', user_id, keyboards_main.keyboard_0)
                            elif player.room == 2:
                                if text == 'Империя':
                                    player.country = 'Империя'
                                    player.location = 1
                                    player.room = 3
                                    writing('Выбери расу', user_id, keyboards_main.keyboard_1)
                                elif text == 'Королевство':
                                    player.country = 'Королевство'
                                    player.location = 2
                                    player.room = 3
                                    writing('Выбери расу', user_id, keyboards_main.keyboard_1)
                                else:
                                    writing('Некорректное значение, выбери страну.', user_id, keyboards_main.keyboard_0)
                            elif player.room == 3:
                                if text == 'Эльф':
                                    player.race = 'Эльф'
                                    player.room = 4
                                    writing('переходим в основную игру', user_id, keyboards_main.keyboard_2)
                                elif text == 'Гном':
                                    player.race = 'Гном'
                                    player.room = 4
                                    writing('переходим в основную игру', user_id, keyboards_main.keyboard_2)
                                else:
                                    writing('Некорректное значение, выбери расу.', user_id, keyboards_main.keyboard_1)
                            elif player.room == 4:
                                if text == 'Продолжить':
                                    db_connection_insert(f'INSERT users (name, vk_id, country, race, location_id) '
                                                         f'VALUES ("{player.name}", {player.vk_id}, "{player.country}",' 
                                                         f'"{player.race}", {player.location});')
                                for i in range(len(list_of_players_id)):
                                    if list_of_players_id[i] == user_id:
                                        list_of_players_id.pop(i)
                                for i in range(len(players)):
                                    if players[i].vk_id == user_id:
                                        players.pop(i)
                        else:
                            if player.part == 'main':
                                if player.room == 0:
                                    writing("Основная страница героя, меню", user_id, keyboards_main.keyboard_3)
                                    player.room = 1
                                elif player.room == 1:
                                    if text == 'Карта':
                                        player.part = 'map'
                            elif player.part == 'map':
                                writing_only_text(f"Герой находится в локации", user_id)

        else:
            for i in range(len(players)):
                if time.time() - players[i].mem_time >= 100:
                    print(f'Удаляем игрока {players[i].name} из оперативной памяти')
                    c = players[i].vk_id
                    players.pop(i)
                    list_of_players_id.remove(c)
                    print(players)
                    print(list_of_players_id)
    except vk_api.exceptions.ApiError or ConnectionError or vk_api.exceptions.ApiHttpError:
        pass
