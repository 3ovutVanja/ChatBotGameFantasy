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


while True:
    try:
        start_time = time.time()
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        # print("%s секунд на проверку наличия сообщений" % (time.time() - start_time))
        print(messages)
    except vk_api.exceptions.ApiError or ConnectionError or vk_api.exceptions.ApiHttpError:
        pass