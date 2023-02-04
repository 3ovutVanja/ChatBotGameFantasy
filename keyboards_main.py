from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def new_keyboard(list_1):
    work_board = VkKeyboard(one_time=False)
    lines = 1
    counter = 0
    for i in list_1:
        work_board.add_button(i, color=VkKeyboardColor.PRIMARY)
        if i == 'Меню':
            work_board.add_line()
        if counter < 4:
            counter += 1
        else:
            work_board.add_line()
            lines += 1
            counter = 0
            if lines == 3:
                break
    return work_board


keyboard_0 = VkKeyboard(one_time=False)
keyboard_0.add_button("Королевство", color=VkKeyboardColor.PRIMARY)
keyboard_0.add_button("Империя", color=VkKeyboardColor.PRIMARY)

keyboard_1 = VkKeyboard(one_time=False)
keyboard_1.add_button("Эльф", color=VkKeyboardColor.PRIMARY)
keyboard_1.add_button("Гном", color=VkKeyboardColor.PRIMARY)

keyboard_2 = VkKeyboard(one_time=False)
keyboard_2.add_button("Продолжить", color=VkKeyboardColor.PRIMARY)

keyboard_3 = VkKeyboard(one_time=False)
keyboard_3.add_button("Карта", color=VkKeyboardColor.PRIMARY)
keyboard_3.add_button("Инвентарь", color=VkKeyboardColor.PRIMARY)
keyboard_3.add_button("Магазин", color=VkKeyboardColor.PRIMARY)

keyboard_4 = VkKeyboard(one_time=False)
keyboard_4.add_button("Меню", color=VkKeyboardColor.PRIMARY)
keyboard_4.add_line()
keyboard_4.add_button("Оружие", color=VkKeyboardColor.PRIMARY)
keyboard_4.add_button("Свитки", color=VkKeyboardColor.PRIMARY)
keyboard_4.add_button("Транспорт", color=VkKeyboardColor.PRIMARY)
keyboard_4.add_button("Снадобья", color=VkKeyboardColor.PRIMARY)


keyboard_5 = VkKeyboard(one_time=False)
keyboard_5.add_button("Квест", color=VkKeyboardColor.PRIMARY)
keyboard_5.add_button("Меню", color=VkKeyboardColor.PRIMARY)

keyboard_6 = VkKeyboard(one_time=False)
keyboard_6.add_button("", color=VkKeyboardColor.PRIMARY)
keyboard_6.add_button("Меню", color=VkKeyboardColor.PRIMARY)