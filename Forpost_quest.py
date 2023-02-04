import datetime
from random import randint
import vk_api
import keyboards


class Player:
    room = 1
    move = 1
    part = 1
    day = 1
    fin = 1
    population = 50
    food = 100
    peasants = 0
    workers = 0
    recruiter = 0
    soldiers = 0.0
    chance = 0
    defence = 0.0
    attack = 0.0
    fight_num = 1
    enemy_attack = 0.0
    enemy_type = 0.0
    enemy_defence = 0.0
    enemy_num = 0.0
    hp = 7
    enemy_hp = 0
    before = 0
    turn = 0

    def __init__(self, name, us_id):
        self.name = name
        self.us_id = us_id


token = "vk1.a.xJtuB7m06aJ0NUxP76zraFp_CKdCAlFGi_QozpaM3-7oa9lqoJ7jjFQ6DALQmbCCl3MFq7Twz_SwjX-AWisGcZ5spY0GEvP4E0efgDNl7XaNfwURZ8kdWALjoYkwlpFMwr_p8_Qvtr1ruinz4BR4J6O3dthRR0U0d_0mGzH-20BKIZ-BzXU3VIShwuUJUfx3"

vk = vk_api.VkApi(token=token)
vk._auth_token()

b = 0


def writing(print_text, us_id, k_b):
    global b
    a = (vk.method("messages.send", {"user_id": us_id, "message": print_text, "random_id": randint(1, 1000),
                                     "keyboard": k_b.get_keyboard()}))
    print(a)
    while a <= b:
        print('Ошибка отправки')
        a = (vk.method("messages.send", {"user_id": us_id, "message": print_text, "random_id": randint(1, 1000),
                                         "keyboard": k_b.get_keyboard()}))
        print(a)
    b = a


def writing_only_text(print_text, us_id):
    global b
    a = (vk.method("messages.send", {"user_id": us_id, "message": print_text, "random_id": randint(1, 1000)}))
    print(a)
    while a <= b:
        print('Ошибка отправки')
        a = (vk.method("messages.send", {"user_id": us_id, "message": print_text, "random_id": randint(1, 1000)}))
        print(a)
    b = a


def vilage(day_num, us_id, k_b, finish, pop, f_d, peas, work, verb, sold, at):
    writing(f'День {day_num}\nЗамок Феантул\nГотовность {finish}%\nНаселение: {pop}\nЕда: {f_d}\nКрестьяне: {peas}\n'
            f'Рабочие: {work}\nВербовщики: {verb}\nСолдаты: {int(sold)}\nВероятность нападения {at}%', us_id, k_b)


def line(day_num, fin):
    if fin < 25:
        res_line = f'День {day_num}. Утро.\nИз окна открывается вид на окружающую замок местность.\n\nВ данный момент ' \
                   f'даже стадо овец без труда минует "грозную" оборону форпоста. Впереди ещё очень много работы.\n '
    elif fin < 50:
        res_line = f'День {day_num}. Утро.\nИз окна открывается вид на окружающую замок местность.\n\nЭто уже не тот ' \
                   f'хлипкий форт, в который вы въехали. Крепкие стены являются хорошим препятствием для слабых ' \
                   f'противников. Темпы строительства удовлетворительные.\n '
    elif fin < 75:
        res_line = f'День {day_num}. Утро.\nИз окна открывается вид на окружающую замок местность.\n\nСейчас форпост ' \
                   f'представляет из себя весьма добротное укрепление, которое, тем не менее, ещё нуждается в доработках\n '
    else:
        res_line = f'День {day_num}. Утро.\nИз окна открывается вид на окружающую замок местность.\n\nВы с гордостью ' \
                   f'можете сказать, что замок Феантул великолепен. Все запланированные работы завершены, заказчики ' \
                   f'довольны.\n '
    return res_line


def details(us_id):
    writing_only_text('Необходимо продержаться 20 дней, по истечению которых замок должен быть полностью построен, '
                      'население не менее 500.\nНаселение форпоста делится на четыре категории.\nКаждый день '
                      'вы выбираете, сколько поселенцев должно заниматься '
                      'определенным делом:', us_id)
    writing_only_text('КРЕСТЬЯНЕ - добывают еду для всех обитателей форпоста. Чем '
                      'больше крестьян - тем больше еды вы получаете каждый день. '
                      'Необходимо следить, чтобы еды всегда было больше чем голодных '
                      'ртов.\n\nРАБОЧИЕ - занимаются непосредственно возведением '
                      'форпоста и его стен. Чем больше рабочих - тем быстрее идет '
                      'строительство. Чем больше замок - тем больше его '
                      'защита.\n\nВЕРБОВЩИКИ - привлекают новых людей, тем самым, '
                      'увеличивая население форпоста. Чем больше вербовщиков - тем '
                      'больше рекрутов присоединяется к вам каждый день.\n\nСОЛДАТЫ - '
                      'несут караул в замке и по периметру, защищая территорию от '
                      'вражеских нападений. Чем больше у вас сегодня солдат - тем '
                      'выше атака и защита форпоста.', us_id)
    writing('Также к вашим услугам моя магия. Астральные предсказания туманны, '
            'но это лучше чем ничего.', us_id, keyboards.keyboard_12)


def numbers(us_id, pop):
    writing_only_text(f'Население твоего замка составляет {pop} человек. Нужно распределить население между '
                      f'четыремя категориями. \nВпиши через пробел 4 числа, которые будут отражать численность '
                      f'каждого вида юнитов в таком порядке:\n Крестьяне Рабочие Вербовщики Солдаты:', us_id)


def checker(txt, pop):
    wroom = txt.split(' ')
    try:
        if len(wroom) == 4 and int(wroom[0]) + int(wroom[1]) + int(wroom[2]) + int(wroom[3]) == pop:
            return True
        else:
            return False
    except ValueError:
        return False


def creating_enemy(fight_num, day_num):
    types = ['Гоблины', 'Огры', 'Орки', 'Тролли', 'Варги', 'Циклопы', 'Степной бегемот']
    var_4 = randint(0, 5)
    if fight_num == 1:
        var_4 = 0
        res_type = types[0]
    else:
        res_type = types[var_4]
    if randint(0, 100) == 1:
        res_type = types[6]
        var_4 = 6
    if var_4 == 0:
        en_num = int(randint(11, 15) * (1 + (day_num * 0.55)))
        en_at = float(randint(5, 10) / 3 * (1.3 + (day_num * 1.6)))
        en_def = float(randint(3, 5) * (1 + (day_num * 0.5)))
        en_hp = 2
    elif var_4 == 1:
        en_num = int(randint(4, 8) * (1.4 + (day_num * 0.4)))
        en_at = float(randint(5, 9) * (2 + (day_num * 0.4)))
        en_def = float(randint(10, 20) / 1.3 * (1.3 + day_num * 0.7))
        en_hp = 10
    elif var_4 == 2:
        en_num = int(randint(9, 14) * (1 + (day_num * 0.25)))
        en_at = float(randint(7, 14) * (1 + day_num * 0.5))
        en_def = float(randint(3, 6) * (1 + day_num * 0.5))
        en_hp = 5
    elif var_4 == 3:
        en_num = int(randint(8, 13) * (1.2 + (day_num * 0.25)))
        en_at = float(randint(5, 10) * (1.3 + (day_num * 0.6)))
        en_def = float(randint(10, 20) * (4 + day_num * 0.8))
        en_hp = 7
    elif var_4 == 4:
        en_num = int(randint(10, 18) * (0.7 + (day_num * 0.35)))
        en_at = float(randint(5, 10) * (1.4 + (day_num * 0.6)))
        en_def = float(randint(10, 16) * (0.3 + (day_num * 0.3)))
        en_hp = 5
    elif var_4 == 5:
        en_num = int(randint(3, 5) * ((day_num * 0.35) + 3))
        en_at = float(randint(30, 50) * (2 + (day_num * 0.2)))
        en_def = float(randint(20, 40) * (1 + (day_num * 0.2)))
        en_hp = 30
    else:
        en_num = int(1)
        en_at = float(randint(70, 120) * (1 + (day_num * 0.75)))
        en_def = float(randint(70, 120) * (1 + (day_num * 0.75)))
        en_hp = 100 * (day_num * 0.5)
    return res_type, en_num, en_at, en_def, en_hp


def distribution(txt):
    shortlist = txt.split(' ')
    return shortlist[0], shortlist[1], shortlist[2], float(shortlist[3])


list_of_players = []
players = []
counter_1 = 0
while True:
    counter_1 += 1
    if counter_1 % 1000 == 0:
        now_time = str(datetime.datetime.now())
        print(f"Проведено {counter_1} итераций - " + now_time)
    # time.sleep(3)
    try:
        now_time = str(datetime.datetime.now())
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            text = messages['items'][0]['last_message']['text']
            user_id = messages['items'][0]['last_message']['from_id']
            fullname = user_id
            if user_id not in list_of_players:
                if text.lower() == "начать":
                    print(str(fullname) + " начал")
                    writing("Вечером вы заходите в трактир. Незнакомец подходит к вашему столу. Одет он просто, "
                            "но со вкусом. Обедневший дворянин или просто аферист? \n- Добрый вечер, господин. "
                            "Позвольте обратиться к вам с выгодным предложением.", user_id, keyboards.keyboard_2)
                    list_of_players.append(user_id)
                    exec(f'player_{user_id} = Player(fullname, user_id)')
                    exec(f'players.append(player_{user_id})')
                else:
                    writing_only_text("Введи 'начать'", user_id)
            elif user_id in list_of_players:
                for player in players:
                    if player.us_id == user_id:
                        if text == 'X':
                            player.room = 0
                            player.part = 1
                            player.move = 1
                            player.day = 1
                            player.fin = 1
                            player.population = 50
                            player.food = 100
                            player.peasants = 0
                            player.workers = 0
                            player.recruiter = 0
                            player.soldiers = 0
                            player.chance = 0
                            player.defence = 0
                            player.attack = 0
                            player.fight_num = 1
                            player.enemy_attack = 0
                            player.enemy_type = 0
                            player.enemy_defence = 0
                            player.enemy_num = 0
                            player.hp = 7
                            player.enemy_hp = 0
                            player.before = 0
                            player.turn = 0
                        if player.part == 1:
                            if player.room == 'exit':
                                writing_only_text(
                                    'Квест окончен. Введи X (англ) для начала сначала. (Ты можешь сделать '
                                    'это в любой момент игры)', user_id)
                            elif player.room == 0:
                                print(str(fullname) + " начал заново")
                                writing("Вечером вы заходите в трактир. Незнакомец подходит к вашему столу. Одет он "
                                        "просто, но со вкусом. Обедневший дворянин или просто аферист? \n- Добрый "
                                        "вечер, господин. Позвольте обратиться к вам с выгодным предложением.",
                                        user_id, keyboards.keyboard_2)
                                player.room = 1
                            elif player.room == 1:
                                if text == "Выслушать":
                                    player.room = 'thinking'
                                    writing('- Меня зовут Джессо Вангрульт. Я являюсь агентом Имперского Торгового '
                                            'Союза.\n- И чего вы от меня хотите?\n- Мы ищем достойную кандидатуру для '
                                            'выполнения одного задания. В качестве вознаграждения вы получите 5000 '
                                            'золотых. Что скажете?', user_id, keyboards.keyboard_4)

                                elif text == "Отказать":
                                    Player.room = 'exit'
                                    writing('Стоп! - останавливаете вы его одним жестом. - Сегодня у меня в планах еще '
                                            'один эль и мягкая постель. Не в моих правилах идти на сделки с '
                                            'незнакомцами в тавернах.\n- Тогда, прошу прощения. Значит, '
                                            'мы снова ошиблись в выборе, - откланявшись, мужчина оставляет вас '
                                            'наедине с выпивкой. ', user_id,
                                            keyboards.keyboard_3)
                                else:
                                    writing('Некорректно значение, попробуй ещё раз', user_id, keyboards.keyboard_2)
                            elif player.room == 'thinking':
                                if text == "Презрительно отказать":
                                    writing(
                                        '- Семьсот золотых, значит? - с насмешкой говорите вы. - Идите, и купите на '
                                        'ярмарке полторы сотни скелетов, которые будут там ишачить за эти медяки. '
                                        'Нет, это не для меня, - одним глотком вы допиваете эль и со стуком опускаете '
                                        'кружку на стол.\n- Восемь сотен, - задумчиво, '
                                        'но твёрдо произносит торговец.', user_id, keyboards.keyboard_5)
                                    player.room = 'thinking2'
                                elif text == 'Согласиться':
                                    writing_only_text("- Хорошо, согласен. Я не в том положении, чтобы отказываться. "
                                                      "Что надо делать?\n- Завтра вы получите карту, "
                                                      "на которой помечено место. Там вас встретит наш агент, "
                                                      "который посвятит в подробности.", user_id)
                                    writing("С утра у порога вы видите человека с дорожной сумкой и плащом. Рядом "
                                            "стоит конь, явно предназначающийся для вас. Уточнив маршрут по карте, "
                                            "вы отправляетесь в путь.", user_id, keyboards.keyboard_7)
                                    player.room = 'accepting'
                                else:
                                    writing('Некорректно значение, попробуй ещё раз', user_id, keyboards.keyboard_4)
                            elif player.room == 'thinking2':
                                if text == 'Уйти':
                                    writing('- Кажется, мы друг друга не поняли, - с разочарованием кидаете вы, '
                                            'оставляете серебряный за эль и направляетесь к двери трактира. Сзади '
                                            'что-то пытается сказать торговец, но вы не можете расслышать.', user_id,
                                            keyboards.keyboard_6)
                                    player.room = 'thinking3'
                                elif text == 'Согласиться':
                                    writing_only_text(
                                        '- Хорошо, вы меня убедили.\n- Вот и ладно, тогда по рукам. Завтра с утра вы '
                                        'получите лошадь и карту, на которой помечено место строительства. Там вас '
                                        'встретит наш человек, который посвятит в подробности дела и будет помогать '
                                        'вам на протяжении строительства.\n', user_id)
                                    writing(
                                        'С утра у порога вы видите человека с дорожной сумкой и плащом. Рядом с ним '
                                        'стоит хороший породистый конь, явно предназначающийся для вас. Уточнив '
                                        'маршрут по карте, вы отправляетесь в путь.', user_id,
                                        keyboards.keyboard_7)
                                    player.room = 'accepting'
                                else:
                                    writing('Некорректно значение, попробуй ещё раз', user_id, keyboards.keyboard_5)
                            elif player.room == 'thinking3':
                                if text == 'Выйти из трактира':
                                    writing_only_text(
                                        'Вы выходите на улицу. Однако '
                                        'не успеваете пройти и трёх десятков шагов, как вслед за вами выбегает '
                                        'торговец.\n- Стойте, вы меня убедили! - кричит он, догоняя вас. Тысяча '
                                        'золотых. \n- Вот и по рукам! - довольно говорите Вы.', user_id)
                                    writing(
                                        'С утра у порога вы видите человека с дорожной сумкой и плащом. Рядом с ним '
                                        'стоит хороший породистый конь, явно предназначающийся для вас. Уточнив '
                                        'маршрут по карте, вы отправляетесь в путь.', user_id,
                                        keyboards.keyboard_7)
                                    player.room = 'accepting'
                                elif text == 'Передумать и вернуться':
                                    writing_only_text(
                                        'Несмотря на решительность, с которой вы покидали стол, вы успеваете '
                                        'затормозить у двери. Обдумав ситуацию, вы возвращаетесь назад. Кажется, '
                                        'торговец насмехается.\n- Ладно, - вы опускаетесь обратно на стул. - Но '
                                        'восемьсот пятьдесят золотых и ни медяком не меньше.', user_id)
                                    writing(
                                        'С утра у порога вы видите человека с дорожной сумкой и плащом. Рядом с ним '
                                        'стоит хороший породистый конь, явно предназначающийся для вас. Уточнив '
                                        'маршрут по карте, вы отправляетесь в путь в.', user_id,
                                        keyboards.keyboard_7)
                                    player.room = 'accepting'
                                else:
                                    writing('Некорректно значение, попробуй ещё раз', user_id, keyboards.keyboard_6)
                            elif player.room == 'accepting':
                                if text == 'В путь':
                                    writing('После долгой дороги вы сверяетесь с картой. Кажется, почти на месте. '
                                            'Между двух расползающихся горных хребтов на возвышении виднеется '
                                            'какое-то поселение. Приглядевшись, вы замечаете, что это одна огромная '
                                            'стройплощадка, в центре которой - деревянный форт.', user_id,
                                            keyboards.keyboard_8)
                                    player.room = 2
                                else:
                                    writing('Некорректно значение, попробуй ещё раз', user_id, keyboards.keyboard_7)
                            elif player.room == 2:
                                if text == 'Направиться к стройплощадке':
                                    writing_only_text("Вас встречает ранее упомянутый агент: высокий и худой маг, "
                                                      "седой старик.\n- Приветствую вас. Позвольте представиться - "
                                                      "Матиус, маг и советник Союза.", user_id)
                                    writing('- И так, к делу! Вы должны возвести замок и набрать для него ополчение. '
                                            'Срок - пятнадцать дней. Если не успеете - Торговый Союз пришлет нового '
                                            'руководителя, а вам не заплатят. Если же успеете – вас наградят. Все '
                                            'приказы можете передавать через меня. Но это еще не всё. Строительство '
                                            'предстоит вести под угрозой постоянных набегов.\nГотовы ли вы взяться за '
                                            'это задание?', user_id,
                                            keyboards.keyboard_9)
                                    player.room = 3
                                else:
                                    writing('Некорректно значение, попробуй ещё раз', user_id, keyboards.keyboard_8)
                            elif player.room == 3:
                                if text == 'Согласиться':
                                    writing('- Теперь – к сути задания: за 20 дней вам необходимо возвести замок и '
                                            'набрать не менее 500 человек. Опасайтесь нападений с диких земель! '
                                            'Торговый Союз прислал обоз провианта, хватит ненадолго. Также имеется '
                                            'банда оборванцев. Для начала – уже не плохо! Ваша задача обеспечить '
                                            'добычу пищи, защиту и вербовку новых ополченцев.', user_id,
                                            keyboards.keyboard_0)
                                    player.room = 4
                                elif text == 'Отказаться от возложенной миссии':
                                    player.room = 'exit'
                                    writing(
                                        '- Я - герой. И мое призвание - это воевать, а не кирпичи подсчитывать. Ищите '
                                        'другого, Матиус.\nС этими словами вы разворачиваетесь, и, не попрощавшись, '
                                        'гордо покидаете строительный участок.\nОстается только повторить то же самое '
                                        'лично для вашего нанимателя и навсегда, наверное, разорвать связи с этим '
                                        'трёклятым Союзом. Но груз ответственности больше не давит на ваши плечи, '
                                        'а значит, можно не волноваться за этот клочок земли. В конце концов, '
                                        'пусть лучше имперским ворам будет хоть какая-нибудь прибыль в их нелёгком '
                                        'труде.', user_id, keyboards.keyboard_0)
                                else:
                                    writing('Некорректно значение, попробуй ещё раз', user_id, keyboards.keyboard_9)
                            elif player.room == 4:
                                if text == 'Дальше':
                                    writing_only_text('Население форпоста делится на четыре категории.\nКаждый день '
                                                      'вы выбираете, сколько поселенцев должно заниматься '
                                                      'определенным делом:', user_id)
                                    writing('КРЕСТЬЯНЕ - добывают еду для всех обитателей '
                                            'форпоста.\n\nРАБОЧИЕ – строят замок.\n\nВЕРБОВЩИКИ - привлекают '
                                            'новых людей, которых можно распределять на '
                                            'категории.\n\nСОЛДАТЫ - отбивают атаки врагов, от их количества зависит '
                                            'боевой птенциал замка.\n\n- А теперь прошу следовать за '
                                            'мной. Я покажу вам вашу палатку.', user_id,
                                            keyboards.keyboard_10)
                                    player.room = 1
                                    player.part = 2
                        elif player.part == 2:
                            if player.room == 'reading numbers':
                                if checker(text, player.population):
                                    player.peasants, player.workers, player.recruiter, player.soldiers = distribution(
                                        text)
                                    player.room = 3
                                else:
                                    writing_only_text('Некорректно значение, попробуй ещё раз', user_id)
                            elif player.room == 1:
                                if text == 'Назад' or text == 'Начало нового дня' or text == 'Спать до утра':
                                    writing(line(player.day, player.fin), user_id,
                                            keyboards.keyboard_11)
                                    vilage(player.day, user_id, keyboards.keyboard_11, player.fin,
                                           player.population, player.food, player.peasants, player.workers,
                                           player.recruiter, player.soldiers, player.chance)
                                    player.room = "day"
                                else:
                                    writing('Некорректно значение, попробуй ещё раз', user_id, keyboards.keyboard_10)
                            elif player.room == "day":
                                if text == 'Выслушать детали задания':
                                    details(user_id)
                                    player.room = 1
                                elif text == 'Заняться распределением':
                                    numbers(user_id, player.population)
                                    player.room = 'reading numbers'
                                elif text == 'Текущий день':
                                    writing(line(player.day, player.fin), user_id,
                                            keyboards.keyboard_11)
                                    vilage(player.day, user_id, keyboards.keyboard_11, player.fin,
                                           player.population, player.food, player.peasants, player.workers,
                                           player.recruiter, player.soldiers, player.chance)
                                else:
                                    writing('Некорректно значение, попробуй ещё раз', user_id, keyboards.keyboard_11)
                            elif player.room == 3:
                                writing('Все жильцы крепости получили указания и приступили к работе. \nУже совсем '
                                        'скоро результат их трудов станет виден', user_id, keyboards.keyboard_13)
                                vilage(player.day, user_id, keyboards.keyboard_13, player.fin,
                                       player.population, player.food, player.peasants, player.workers,
                                       player.recruiter, player.soldiers, player.chance)
                                player.room = 4
                            elif player.room == 4:
                                if text == 'Прошёл день':
                                    writing_only_text('Конец рабочей смены.\nМастера и архитекторы отчитываются в '
                                                      'проделанной работе магу. Крестьяне, рабочие и вербовщики '
                                                      'отправляются на заслуженный отдых. Только солдаты остаются на '
                                                      'постах, готовые в случае опасности поднять тревогу.', user_id)
                                    var_3 = (int(player.peasants) * 3) - player.population
                                    player.food += var_3
                                    var_2 = round(int(player.recruiter) / 2)
                                    player.population += var_2
                                    var_1 = int(player.workers) / 3
                                    player.fin += int(var_1)
                                    vilage(player.day, user_id, keyboards.keyboard_14, player.fin,
                                           player.population, player.food, player.peasants, player.workers,
                                           player.recruiter, player.soldiers, player.chance)
                                    if player.food <= 0:
                                        writing('Население замка столкнулось с голодом. Продолжение строительства '
                                                'невозможно в связи снесоблюдением прав рабочих. Вас вышвыривают на '
                                                'улицу без выплаты золота.', user_id, keyboards.keyboard_16)
                                        player.part = 1
                                        player.room = 'exit'
                                    else:
                                        player.room = 5
                                else:
                                    writing('Некорректно значение, попробуй ещё раз', user_id, keyboards.keyboard_13)
                            elif player.room == 5:
                                if text == 'Прошёл вечер':
                                    chance = player.chance
                                    if player.chance < 30:
                                        chance = 0
                                    elif player.chance > 85:
                                        chance = 100
                                    if randint(0, 100) < chance:
                                        writing('Трубит рог на главной башне!\nДозорные заметили приближение врага. '
                                                'Вы спешите к крепостной стене, чтобы '
                                                'управлять ходом сражением.', user_id, keyboards.keyboard_17)
                                        player.part = 'fight'
                                        player.chance = int(player.chance / 2)
                                        memory = player.soldiers
                                    else:
                                        writing_only_text(f'Позади еще один тяжелый день. Вы ложитесь спать с '
                                                          f'чувством выполненного долга и мыслями о том, что осталось '
                                                          f'всего {20 - player.day} суток.\n\nОТЧЕТ:\n\nГотовность '
                                                          f'замка: '
                                                          f'{int(player.fin)} ({int(var_1)}).\nНаселение: '
                                                          f'{int(player.population)} ({var_2}).\nЕда: {player.food} ('
                                                          f'{var_3}).', user_id)
                                        vilage(player.day, user_id, keyboards.keyboard_15, player.fin,
                                               player.population, player.food, player.peasants, player.workers,
                                               player.recruiter, player.soldiers, player.chance)
                                        player.day += 1
                                        player.chance = int(100 - ((100 - player.chance) / 1.5))
                                        if player.day == 2:
                                            player.chance = 50
                                        if player.population > 500 and player.fin > 100:
                                            writing_only_text('Строительство наконец окончено, гарнизон набран. Теперь '
                                                              'эта крепость станет оплотом цивилизации на восточной '
                                                              'границе Империи. Вы успешно справились с поставленной '
                                                              'задачей, можете получить вознаграждание и медаль за '
                                                              'выполнение поручения.', user_id)
                                            with open("winners.txt", "a", encoding="utf-8") as co:
                                                co.write(str(user_id) + '\n')
                                        elif player.day < 21:
                                            player.room = 1
                                        else:
                                            writing_only_text('К сожалению выделенное на работы время подошло к '
                                                              'концу. Вы неплохо старались, но требуемого результата '
                                                              'не достигли. Работодатели прощаются с вами без выплаты '
                                                              'денег.\n\nДля повторного прохождения введи X.', user_id)
                                            player.room = 'exit'

                                else:
                                    writing('Некорректно значение, попробуй ещё раз', user_id, keyboards.keyboard_14)
                            elif player.room == 6:
                                if text == "Ура!":
                                    var_5 = randint(0, 10)
                                    player.food += var_5
                                    writing_only_text(f'Победа! Враг разбит!\n\nНаграда нашла героя:\n+{var_5} еды.\n'
                                                      f'Позади еще один тяжелый день. В'
                                                      f' сражении погибли {int(player.before - player.population)} '
                                                      f'солдат, но атака отбита. Вы ложитесь спать с чувством '
                                                      f'выполненного долга и мыслями о том, что осталось всего '
                                                      f'{20 - player.day} суток.\n\nОТЧЕТ:\n\nГотовность замка: '
                                                      f'{int(player.fin)}.\nНаселение: '
                                                      f'{int(player.population)}.\nЕда: {player.food}.', user_id)
                                    vilage(player.day, user_id, keyboards.keyboard_15, player.fin,
                                           player.population, player.food, player.peasants, player.workers,
                                           player.recruiter, player.soldiers, player.chance)
                                    player.day += 1
                                    if player.population > 500 and player.fin > 100:
                                        writing_only_text('Строительство наконец окончено, гарнизон набран. Теперь '
                                                          'эта крепость станет оплотом цивилизации на восточной '
                                                          'границе Империи. Вы успешно справились с поставленной '
                                                          'задачей, можете получить вознаграждание и медаль за '
                                                          'выполнение поручения.', user_id)
                                    elif player.day < 21:
                                        player.room = 1
                                    else:
                                        writing_only_text('К сожалению выделенное на работы время подошло к '
                                                          'концу. Вы неплохо старались, но требуемого результата '
                                                          'не достигли. Работодатели прощаются с вами без выплаты '
                                                          'денег.\n\nДля повторного прохождения введи X.', user_id)
                                        player.room = 'exit'
                                else:
                                    writing('Некорректно значение, попробуй ещё раз', user_id, keyboards.keyboard_19)
                        elif player.part == 'fight':
                            if player.move == 1:
                                player.enemy_type, player.enemy_num, player.enemy_attack, player.enemy_defence, \
                                player.enemy_hp = creating_enemy(player.fight_num, player.day)
                                if text == 'Руководить обороной':
                                    player.before = player.population
                                    player.attack = float(player.soldiers) * 0.75 + float(player.fin) * 0.25
                                    player.defence = float(player.soldiers) * 0.20 + float(player.fin) * 0.80
                                    writing(f'Гарнизон: {int(player.soldiers)} солдат\nАтака {int(player.attack)}\nЗ'
                                            f'ащита {int(player.defence)}\nЗамок {int(player.fin)}\n\nVS {player.enemy_type} '
                                            f'{player.enemy_num}\nАтака {int(player.enemy_attack)}\nЗащита '
                                            f'{int(player.enemy_defence)}\n\nАтаковать\nГарнизон занимает '
                                            f'преимущественно '
                                            f'атакующую позицию.\n\nЗащищать\nГарнизон занимает преимущественно '
                                            f'защитную позицию. Выбирающие такой подход стремятся не уничтожить '
                                            f'врага, а сохранить больше человеческих жизней.', user_id,
                                            keyboards.keyboard_18)
                                    player.move = 2
                                else:
                                    writing('Некорректно значение, попробуй ещё раз', user_id, keyboards.keyboard_17)
                            elif player.move == 2:
                                if text == 'Атаковать':
                                    pl_damage = float(player.soldiers) * (
                                            0.5 + 0.5 * (player.attack / player.enemy_defence))
                                    en_damage = float(player.enemy_num) * (
                                            0.5 + 0.5 * (player.enemy_attack / player.defence))
                                    player.enemy_num = (float(player.enemy_num * player.enemy_hp) - pl_damage) / float(
                                        player.enemy_hp)
                                    player.soldiers = (float(player.soldiers * player.hp) - en_damage) / float(
                                        player.hp)
                                    player.turn += 1

                                elif text == 'Защищать':
                                    pl_damage = 0.7 * float(player.soldiers) * (
                                            0.5 + 0.5 * (player.attack / player.enemy_defence))
                                    en_damage = float(player.enemy_num) * (
                                            0.5 + 0.5 * (player.enemy_attack / (player.defence * 1.4)))
                                    player.enemy_num = (float(player.enemy_num * player.enemy_hp) - pl_damage) / float(
                                        player.enemy_hp)
                                    player.soldiers = (float(player.soldiers * player.hp) - (en_damage * 0.6)) / float(
                                        player.hp)
                                    var_6 = (en_damage * 0.06)
                                    player.fin = int(float(player.fin) - var_6)
                                    player.turn += 1

                                if int(player.enemy_num) <= 0 or (player.turn == 10 and int(player.soldiers) > 0):
                                    if player.turn == 10:
                                        writing('Победа! Враги не смогли прорвать в крепость и решили отступить.',
                                                user_id, keyboards.keyboard_19)
                                    else:
                                        writing('Победа! Все враги побеждены.',
                                                user_id, keyboards.keyboard_19)
                                    player.population = player.population - (int(memory) - int(player.soldiers))
                                    player.part = 2
                                    player.fight_num += 1
                                    player.move = 1
                                    player.room = 6
                                    player.turn = 0
                                elif int(player.soldiers) <= 0:
                                    writing('Поражение. Отряд врагов перебил всех солдат и прорвался в замок. Вам '
                                            'удалось спастись бегством, но ни о какой выплате за работу уже не идёт и '
                                            'речи. \n\nЗа ваши ошибки на вас накладывается штраф в размере .... Это '
                                            'золото пойдёт на выплаты семмьям погибших жителей.', user_id,
                                            keyboards.keyboard_21)
                                    player.part = 1
                                    player.room = 'exit'
                                else:
                                    writing(
                                        f'Гарнизон: {int(player.soldiers)} солдат\nАтака {int(player.attack)}\nЗ'
                                        f'ащита {int(player.defence)}\nЗамок {int(player.fin)}\n\nVS \n{player.enemy_type} '
                                        f'{int(player.enemy_num)}\nАтака {int(player.enemy_attack)}\nЗащита '
                                        f'{int(player.enemy_defence)}', user_id,
                                        keyboards.keyboard_18)
                        else:
                            pass
    except vk_api.exceptions.ApiError or ConnectionError or vk_api.exceptions.ApiHttpError:
        pass
