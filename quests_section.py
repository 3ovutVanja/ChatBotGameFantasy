import keyboards_main
import main
import sql_connect


def get_quests_list(vk_id, uid):
    work_str = 'Список квестов в этой локации:\n'
    a = sql_connect.db_connection_select_tuple(f'SELECT q.name, q.reward FROM quests q JOIN users u ON u.location_id '
                                               f'= q.location_id WHERE u.id = {uid};')
    counter = 1
    kb_list = ['Меню', 'Карта']
    for i in a:
        kb_list.append(i[0])
        work_str += f'{counter}) {i[0]} с наградой {i[1]}\n'
        counter += 1
    main.writing(work_str, vk_id, keyboards_main.new_keyboard(kb_list))