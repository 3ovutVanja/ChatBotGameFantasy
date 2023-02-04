import vk_api
from random import randint
import keyboards_main
import time
import quests_section
import sql_connect

start_time = time.time()
token = "vk1.a.xJtuB7m06aJ0NUxP76zraFp_CKdCAlFGi_QozpaM3-7oa9lqoJ7jjFQ6DALQmbCCl3MFq7Twz_SwjX-AWisGcZ5spY0GEvP4E0efgDNl7XaNfwURZ8kdWALjoYkwlpFMwr_p8_Qvtr1ruinz4BR4J6O3dthRR0U0d_0mGzH-20BKIZ-BzXU3VIShwuUJUfx3"
vk = vk_api.VkApi(token=token)
vk._auth_token()
b = 0


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
    return sql_connect.db_connection_select(f'SELECT * FROM users WHERE vk_id = {vk_id} LIMIT 1;')


def return_ammunition_text(us_id, vk_id):
    generated_string = ''
    for work_line in sql_connect.db_connection_select_tuple(f'SELECT durability_left, (SELECT deffence FROM ammunition '
                                                            f'WHERE id = ammunition_id), (SELECT attack FROM '
                                                            f'ammunition WHERE id = ammunition_id), '
                                                            f'(SELECT durability FROM ammunition WHERE id = '
                                                            f'ammunition_id), (SELECT name FROM ammunition WHERE id = '
                                                            f'ammunition_id) FROM ammunition_users WHERE user_id = '
                                                            f'{us_id};'):
        var_string = f'{work_line[4]}: \nатака = {work_line[2]}\nзащита = {work_line[1]}\nПрочность = {work_line[0]}/' \
                     f'{work_line[3]}\n\n'
        generated_string += var_string
    writing('В инвентаре у игрока лежат следующие артефакты:\n\n' + generated_string, vk_id, keyboards_main.keyboard_4)


def shop(us_id, vk_id):
    if sql_connect.db_connection_select(f'SELECT id FROM shop WHERE location_id = (SELECT location_id FROM users '
                                        f'WHERE id = {us_id})') is not None:
        player.part = 'shop'
        generated_string = ''
        kb_list = ['Меню']
        for line_1 in shop_request(us_id):
            var_string = f'{line_1[0]}: \nатака = {line_1[1]} \nзащита = {line_1[2]}\nПрочность: {line_1[3]}\nЦена: ' \
                         f'{line_1[4]}\n\n'
            generated_string += var_string
            kb_list.append(line_1[0])
        writing("Содержимое первой страницы магазина:\n\n" + generated_string,
                vk_id, keyboards_main.new_keyboard(kb_list))

    else:
        writing('Некорректное значение, выбери пункт меню.', user_id,
                keyboards_main.keyboard_3)


def buying_ammunition(us_id, work_text, vk_id):
    working_price = sql_connect.db_connection_select(f"SELECT price FROM ammunition WHERE name = '{work_text}';")
    if player.money >= working_price[0]:
        sql_connect.db_connection_insert(f"INSERT INTO ammunition_users (user_id, ammunition_id, durability_left) "
                                         f"VALUES ({us_id}, (SELECT id FROM ammunition WHERE name = '{work_text}'), "
                                         f"(SELECT durability FROM ammunition WHERE id = (SELECT id FROM ammunition "
                                         f"WHERE name = '{work_text}')));")
        player.money -= working_price[0]
    else:
        writing_only_text('К сожалению у тебя недостаточно средств на приобретение данного артефакта(', vk_id)


def shop_request(us_id):
    return sql_connect.db_connection_select_tuple(f'SELECT name, attack, deffence, durability, price FROM ammunition '
                                                  f'WHERE id IN (SELECT ammunition_id FROM ammunition_shop WHERE '
                                                  f'shop_id = (SELECT id FROM shop WHERE location_id = (SELECT '
                                                  f'location_id FROM users WHERE id = {us_id})));')


class Player:
    room = 1
    part = 'main'

    def __init__(self, name, vk_id, player_id, country, level, location_id, race, born, experience, money, mem_time):
        self.name = name
        self.vk_id = vk_id
        self.id = player_id
        self.country = country
        self.level = level
        self.location_id = location_id
        self.race = race
        self.born = born
        self.experience = experience
        self.money = money
        self.mem_time = mem_time


class PlayerInRegistration:
    name = ''
    country = ''
    location = ''
    race = ''
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
            for message in range(messages["count"]):
                print("%s секунд на отправку сообщения или просто вход в цикл" % (time.time() - start_time))
                start_time = time.time()
                text = messages['items'][message]['last_message']['text']
                user_id = messages['items'][message]['last_message']['from_id']
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
                        players.append(
                            Player(user_now[1], user_now[2], user_now[0], user_now[3], user_now[6], user_now[7],
                                   user_now[5], user_now[4], user_now[8], user_now[9], time.time()))
                        writing("Основная страница героя, меню", user_id, keyboards_main.keyboard_3)
                elif user_id in list_of_players_id:
                    for player in players:
                        if player.vk_id == user_id:
                            player.mem_time = time.time()
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
                                        writing('Некорректное значение, выбери страну.', user_id,
                                                keyboards_main.keyboard_0)
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
                                        writing('Некорректное значение, выбери расу.', user_id,
                                                keyboards_main.keyboard_1)
                                elif player.room == 4:
                                    if text == 'Продолжить':
                                        sql_connect.db_connection_insert(f'INSERT users (name, vk_id, country, race, '
                                                                         f'location_id) VALUES ("{player.name}", '
                                                                         f'{player.vk_id}, "{player.country}",'
                                                                         f'"{player.race}", {player.location});')
                                    for i in range(len(list_of_players_id)):
                                        if list_of_players_id[i] == user_id:
                                            list_of_players_id.pop(i)
                                    for i in range(len(players)):
                                        if players[i].vk_id == user_id:
                                            players.pop(i)
                            else:
                                if player.part == 'main':
                                    if player.room == 1:
                                        if text == 'Карта':
                                            player.part = 'map'
                                            writing("Герой зашёл в карту", user_id, keyboards_main.keyboard_5)
                                        elif text == 'Инвентарь':
                                            player.part = 'inventory'
                                            writing("Герой зашёл в инвентарь", user_id, keyboards_main.keyboard_4)
                                        elif text == "Магазин":
                                            writing_only_text('Герой зашёл в магазин. \n', user_id)
                                            shop(player.id, user_id)
                                        else:
                                            writing('Некорректное значение, выбери пункт меню.', user_id,
                                                    keyboards_main.keyboard_3)
                                elif player.part == 'shop':
                                    if player.room == 1:
                                        if text == 'Меню':
                                            writing("Основная страница героя, меню", user_id, keyboards_main.keyboard_3)
                                            player.part = 'main'
                                        else:
                                            for line in shop_request(player.id):
                                                if text == line[0]:
                                                    buying_ammunition(player.id, text, user_id)
                                                    writing_only_text(f'Герой приобрёл {text}', user_id)
                                                    shop(player.id, user_id)
                                elif player.part == 'inventory':
                                    if player.room == 1:
                                        if text == 'Меню':
                                            writing("Основная страница героя, меню", user_id, keyboards_main.keyboard_3)
                                            player.part = 'main'
                                        elif text == 'Оружие':
                                            return_ammunition_text(player.id, user_id)
                                        else:
                                            writing('Некорректное значение, выбери пункт меню.', user_id,
                                                    keyboards_main.keyboard_4)
                                elif player.part == 'map':
                                    if player.room == 1:
                                        if text == 'Меню':
                                            writing("Основная страница героя, меню", user_id, keyboards_main.keyboard_3)
                                            player.part = 'main'
                                        elif text == 'Квест':
                                            quests_section.get_quests_list(user_id, player.id)
                                        else:
                                            writing('Некорректное значение, выбери пункт меню.', user_id,
                                                    keyboards_main.keyboard_5)
        else:
            var_1 = 0
            for i in range(len(players)):
                if time.time() - players[i - var_1].mem_time >= 30:
                    sql_connect.db_connection_insert(f'UPDATE users SET level_ = {players[i - var_1].level}, '
                                                     f'location_id = {players[i - var_1].location_id}, experience = '
                                                     f'{players[i - var_1].experience}, money = '
                                                     f'{players[i - var_1].money} WHERE id = {players[i - var_1].id};')
                    print(f'Удаляем игрока {players[i - var_1].name} из оперативной памяти')
                    list_of_players_id.remove(players[i - var_1].vk_id)
                    players.pop(i - var_1)
                    print(players)
                    print(list_of_players_id)
                    var_1 += 1
    except vk_api.exceptions.ApiError or ConnectionError or vk_api.exceptions.ApiHttpError:
        pass
