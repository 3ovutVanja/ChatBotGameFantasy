import sql_connect

# Хотел заняться переносом всех функций из основного тела программы в отдельный файл, но столкнулся с проблемой,
# что многие функции сслыаются на функцию отправки сообщений, которая пользуется глобальной переменной основной
# программы, перенести её сюда легко не получится. Так что я не стал пока этим заниматься, программу всё равно
# полностью переделывать под другую библиотеку.


def quests_list(vk_id, uid):
    work_str = 'Список квестов в этой локации:\n'
    a = sql_connect.db_connection_select_tuple(f'SELECT q.name, q.reward FROM quests q JOIN users u ON u.location_id '
                                               f'= q.location_id WHERE u.id = {uid};')
    counter = 1
    kb_list = ['Меню', 'Карта']
    for i in a:
        kb_list.append(i[0])
        work_str += f'{counter}) {i[0]} с наградой {i[1]}\n'
        counter += 1
    return kb_list, work_str
