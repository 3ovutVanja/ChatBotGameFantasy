from vk_api.keyboard import VkKeyboard, VkKeyboardColor


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
