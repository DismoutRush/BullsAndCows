import pygame
import time
import config as c
from algorithm import generate_secret_number, compare_nums
from button import Button
from game import Game
from text_object import TextObject
from game_object import GameObject
import colors

class Bulls_And_Cows(Game):
    def __init__(self):
        Game.__init__(self, 'Bulls & Cows', c.screen_width, c.screen_height, c.background_light, c.frame_rate)
        self.background_theme = 'light'
        self.menu_buttons = []
        self.game_buttons = []
        self.user_input = []
        self.user_input_object = []
        self.user_guesses = []
        self.user_guesses_objects = []
        self.max_len = 0
        self.secret_num = 0
        self.user_attempts = 0
        self.is_game_running = False
        self.create_objects()

    def create_menu(self):

        def on_play(button):
            self.objects.clear()

            self.mouse_handlers.clear()

            self.choose_difficulty()

        def on_settings(button):
            self.objects.clear()

            self.mouse_handlers.clear()

            self.create_settings_menu()

        title = TextObject(c.title_offset_x, c.title_offset_y, lambda: 'BULLS  &  COWS', colors.EERIE_BLACK, 90)
        b_on_play = Button(c.menu_offset_x, c.menu_offset_y, c.menu_button_w, c.menu_button_h, 'Играть', c.text_color_light, 60, on_play, padding_x=12.5, padding_y=8)
        b_on_settings = Button(c.menu_offset_x, c.menu_offset_y + 150, c.menu_button_w, c.menu_button_h, 'Настройки', c.text_color_light, 60, on_settings, padding_x=12.5,
                               padding_y=10)

        if self.background_theme == 'dark':
            title = TextObject(c.title_offset_x, c.title_offset_y, lambda: 'BULLS  &  COWS', colors.PUMICE, 90)
            b_on_play = Button(c.menu_offset_x, c.menu_offset_y, c.menu_button_w, c.menu_button_h, 'Играть', c.text_color_dark, 60, on_play, padding_x=12.5, padding_y=8,
                               theme='dark')
            b_on_settings = Button(c.menu_offset_x, c.menu_offset_y + 150, c.menu_button_w, c.menu_button_h, 'Настройки', c.text_color_dark, 60, on_settings, padding_x=12.5,
                                   padding_y=10, theme='dark')

        self.objects.append(title)

        self.objects.append(b_on_play)
        self.objects.append(b_on_settings)

        self.mouse_handlers.append(b_on_play.handle_mouse_event)
        self.mouse_handlers.append(b_on_settings.handle_mouse_event)

    def create_settings_menu(self):

        def sound_on(button):
            self.play_sound = True
            self.show_message('Звук включён')

        def sound_off(button):
            self.play_sound = False
            self.show_message('Звук выключён')

        def dark_theme(button):
            self.background_theme = 'dark'
            self.background_image = pygame.image.load(c.background_dark)
            self.surface.blit(self.background_image, (0, 0))
            self.objects.clear()
            self.mouse_handlers.clear()
            self.create_settings_menu()
            self.show_message('Тёмная тема применена')

        def light_theme(button):
            self.background_theme = 'light'
            self.background_image = pygame.image.load(c.background_light)
            self.surface.blit(self.background_image, (0, 0))
            self.objects.clear()
            self.mouse_handlers.clear()
            self.create_settings_menu()
            self.show_message('Светлая тема применена')

        def back_to_menu(button):
            self.objects.clear()

            self.mouse_handlers.clear()

            self.create_menu()

        title = TextObject(c.title_offset_x, c.title_offset_y, lambda: 'BULLS  &  COWS', colors.EERIE_BLACK, 90)

        b_sound_on = Button(c.settings_offset_x, c.settings_offset_y, c.settings_button_w, c.settings_button_h, 'Вкл. звук', c.text_color_light, 40, sound_on, padding_x=10)
        b_sound_off = Button(c.settings_offset_x + 250, c.settings_offset_y, c.settings_button_w, c.settings_button_h, 'Выкл. звук', c.text_color_light, 40, sound_off,
                             padding_x=10)
        b_light_theme = Button(c.settings_offset_x - 50, c.settings_offset_y + 100, c.settings_button_w + 52, c.settings_button_h, '     Светлая тема', c.text_color_light, 40,
                               light_theme, padding_x=10, padding_y=5)
        b_dark_theme = Button(c.settings_offset_x + 250, c.settings_offset_y + 100, c.settings_button_w + 50, c.settings_button_h, '     Тёмная тема', c.text_color_light, 40,
                              dark_theme, padding_x=10, padding_y=4)
        b_back_to_menu = Button(20, 720, c.settings_button_w, c.settings_button_h, 'Назад', c.text_color_light, 40, back_to_menu, padding_x=10)

        if self.background_theme == 'dark':
            title = TextObject(c.title_offset_x, c.title_offset_y, lambda: 'BULLS  &  COWS', colors.PUMICE, 90)

            b_sound_on = Button(c.settings_offset_x, c.settings_offset_y, c.settings_button_w, c.settings_button_h, 'Вкл. звук', c.text_color_dark, 40, sound_on, padding_x=10,
                                theme='dark')
            b_sound_off = Button(c.settings_offset_x + 250, c.settings_offset_y, c.settings_button_w, c.settings_button_h, 'Выкл. звук', c.text_color_dark, 40, sound_off,
                                 padding_x=10, theme='dark')
            b_light_theme = Button(c.settings_offset_x - 50, c.settings_offset_y + 100, c.settings_button_w + 52, c.settings_button_h, '     Светлая тема', c.text_color_dark, 40,
                                   light_theme, padding_x=10, padding_y=5, theme='dark')
            b_dark_theme = Button(c.settings_offset_x + 250, c.settings_offset_y + 100, c.settings_button_w + 50, c.settings_button_h, '     Тёмная тема', c.text_color_dark, 40,
                                  dark_theme, padding_x=10, padding_y=4, theme='dark')
            b_back_to_menu = Button(20, 720, c.settings_button_w, c.settings_button_h, 'Назад', c.text_color_dark, 40, back_to_menu, padding_x=10, theme='dark')

        self.objects.append(title)

        self.objects.append(b_sound_on)
        self.objects.append(b_sound_off)
        self.objects.append(b_light_theme)
        self.objects.append(b_dark_theme)
        self.objects.append(b_back_to_menu)

        self.mouse_handlers.append(b_sound_on.handle_mouse_event)
        self.mouse_handlers.append(b_sound_off.handle_mouse_event)
        self.mouse_handlers.append(b_light_theme.handle_mouse_event)
        self.mouse_handlers.append(b_dark_theme.handle_mouse_event)
        self.mouse_handlers.append(b_back_to_menu.handle_mouse_event)

    def choose_difficulty(self):

        def easy(button):
            self.objects.clear()
            self.mouse_handlers.clear()
            self.max_len = 4
            self.secret_num = generate_secret_number(self.max_len)
            self.game_field()

        def medium(button):
            self.objects.clear()
            self.mouse_handlers.clear()
            self.max_len = 6
            self.secret_num = generate_secret_number(self.max_len)
            self.game_field()

        def hard(button):
            self.objects.clear()
            self.mouse_handlers.clear()
            self.max_len = 8
            self.secret_num = generate_secret_number(self.max_len)
            self.game_field()

        def back_to_menu(button):
            self.objects.clear()

            self.mouse_handlers.clear()

            self.create_menu()

        title = TextObject(c.title_offset_x, c.title_offset_y - 100, lambda: 'ВЫБЕРИТЕ СЛОЖНОСТЬ', colors.EERIE_BLACK, 60)

        b_easy = Button(125, 200, 350, 100, 'Лёгкий', c.text_color_light, 75, easy, padding_x=13)
        b_medium = Button(125, 350, 350, 100, 'Средний', c.text_color_light, 75, medium, padding_x=13.2, padding_y=-10, difficulty='medium')
        b_hard = Button(125, 500, 350, 100, 'Тяжёлый', c.text_color_light, 75, hard, padding_x=13.4, difficulty='hard')
        b_back_to_menu = Button(20, 720, c.settings_button_w, c.settings_button_h, 'Назад', c.text_color_light, 40, back_to_menu, padding_x=10)

        if self.background_theme == 'dark':
            title = TextObject(c.title_offset_x, c.title_offset_y - 100, lambda: 'ВЫБЕРИТЕ СЛОЖНОСТЬ', colors.PUMICE, 60)

            b_easy = Button(125, 200, 350, 100, 'Лёгкий', c.text_color_dark, 75, easy, padding_x=13, theme='dark')
            b_medium = Button(125, 350, 350, 100, 'Средний', c.text_color_dark, 75, medium, padding_x=13.2, padding_y=-10, theme='dark', difficulty='medium')
            b_hard = Button(125, 500, 350, 100, 'Тяжёлый', c.text_color_dark, 75, hard, padding_x=13.4, theme='dark', difficulty='hard')
            b_back_to_menu = Button(20, 720, c.settings_button_w, c.settings_button_h, 'Назад', c.text_color_dark, 40, back_to_menu, padding_x=10, theme='dark')

        self.objects.append(title)

        self.objects.append(b_easy)
        self.objects.append(b_medium)
        self.objects.append(b_hard)
        self.objects.append(b_back_to_menu)

        self.mouse_handlers.append(b_easy.handle_mouse_event)
        self.mouse_handlers.append(b_medium.handle_mouse_event)
        self.mouse_handlers.append(b_hard.handle_mouse_event)
        self.mouse_handlers.append(b_back_to_menu.handle_mouse_event)

    def game_field(self):
        self.user_attempts = 0

        def on_digit(button: Button):
            digit = button.get_text()
            self.user_input.append(digit)
            if len(self.user_input) > self.max_len:
                self.user_input.pop()
                self.show_message(f'Максимальная длина числа {self.max_len}', y=c.screen_height // 2 - 70,color=(255, 0, 213), font_size=45, sleep=1)
                return
            padding = len(self.user_input) - 1
            reverse_list_user_input = self.user_input[::-1]
            if self.max_len == 4:
                self.user_input_object.append(TextObject(230 + 50 * padding, 407, lambda: reverse_list_user_input[0], colors.BLACK, 40))
            elif self.max_len == 6:
                self.user_input_object.append(TextObject(180 + 50 * padding, 407, lambda: reverse_list_user_input[0], colors.BLACK, 40))
            elif self.max_len == 8:
                self.user_input_object.append(TextObject(110 + 50 * padding, 407, lambda: reverse_list_user_input[0], colors.BLACK, 40))
            reverse_list_user_input_object = self.user_input_object[::-1]
            self.objects.append(reverse_list_user_input_object[0])

        def on_confirm(button):
            self.user_attempts += 1
            if len(self.user_input) < self.max_len:
                self.show_message(f'Длина числа должна быть не меньше {self.max_len}', y=c.screen_height // 2 - 65, color=(255,0,213), font_size=35, sleep=1.5)
                return
            user_num = ''
            for d in self.user_input:
                user_num += d
            self.user_guesses.append(user_num)
            self.user_input.clear()
            for o in self.user_input_object:
                self.objects.remove(o)
            self.user_input_object.clear()
            padding = len(self.user_guesses) - 1
            padding_x = 0
            if self.max_len >= 6:
                padding_x = 40
            print(self.secret_num)
            bulls, cows = compare_nums(self.max_len, self.secret_num, user_num)
            if bulls == self.max_len:
                self.win_sound_play = True
                self.objects.clear()
                self.mouse_handlers.clear()
                self.user_guesses.clear()
                self.win()
                return
            to_hint = TextObject(100, 30 + 35 * padding, lambda: f'{user_num} - {bulls} б,{cows} к', c.text_color_light, 20)
            if 8 < len(self.user_guesses) <= 16:
                to_hint = TextObject(245 + padding_x, 30 + 35 * (padding - 8), lambda: f'{user_num} - {bulls} б,{cows} к', c.text_color_light, 20)
            elif 16 < len(self.user_guesses) <= 24:
                to_hint = TextObject(385 + padding_x * 2, 30 + 35 * (padding - 16), lambda: f'{user_num} - {bulls} б,{cows} к', c.text_color_light, 20)
            if self.max_len >=6 and len(self.user_guesses) > 24:
                last_guess = TextObject(100, 30, lambda: f'{user_num} - {bulls} б,{cows} к', c.text_color_light, 20)
                self.user_guesses.clear()
                for o in self.user_guesses_objects:
                    self.objects.remove(o)
                self.user_guesses_objects.clear()
                self.user_guesses_objects.append(last_guess)
                self.user_guesses.append(user_num)
                self.objects.append(last_guess)
                return
            elif 24 < len(self.user_guesses) <= 32:
                to_hint = TextObject(520 + padding_x, 30 + 35 * (padding - 24), lambda: f'{user_num} - {bulls} б,{cows} к', c.text_color_light, 20)
            elif len(self.user_guesses) > 32:
                last_guess = TextObject(90 + padding_x, 30, lambda: f'{user_num} - {bulls} б,{cows} к', c.text_color_light, 20)
                self.user_guesses.clear()
                for o in self.user_guesses_objects:
                    self.objects.remove(o)
                self.user_guesses_objects.clear()
                self.user_guesses_objects.append(last_guess)
                self.user_guesses.append(user_num)
                self.objects.append(last_guess)
                return
            self.user_guesses_objects.append(to_hint)
            self.objects.append(to_hint)

        def on_delete(button):
            if self.user_input:
                self.user_input.pop()
                to_delete = self.user_input_object.pop()
                self.objects.remove(to_delete)


        def on_quit(button):

            def on_yes(button):
                self.objects.clear()
                self.mouse_handlers.clear()
                self.user_guesses.clear()
                self.user_guesses_objects.clear()
                self.user_input.clear()
                self.user_input_object.clear()
                self.user_attempts = 0

                self.create_menu()

            quit_text = TextObject(320, 260, lambda: 'Вы действительно', c.text_color_light, 50)
            quit_text_1 = TextObject(320, 310, lambda: 'хотите покинуть', c.text_color_light, 50)
            quit_text_2 = TextObject(320, 360, lambda: 'текущую игру?', c.text_color_light, 50)


            quit_border = GameObject(12, 240, 576, 320, colors.BLACK)
            quit_field = GameObject(15, 245, 570, 310, colors.PUMICE)


            self.objects.append(quit_border)
            self.objects.append(quit_field)


            self.objects.append(quit_text)
            self.objects.append(quit_text_1)
            self.objects.append(quit_text_2)

            def on_no(button):
                self.objects.remove(quit_border)
                self.objects.remove(quit_field)
                self.objects.remove(quit_text)
                self.objects.remove(quit_text_1)
                self.objects.remove(quit_text_2)
                self.objects.remove(b_yes)
                self.objects.remove(b_no)
                self.mouse_handlers.remove(b_yes.handle_mouse_event)
                self.mouse_handlers.remove(b_no.handle_mouse_event)

            b_yes = Button(35, 461, 210, 60, 'Да', c.text_color_light, 45, on_yes, padding_x=10.4)
            b_no = Button(347, 461, 210, 60, 'Нет', c.text_color_light, 45, on_no, padding_x=10.4)

            self.objects.append(b_yes)
            self.objects.append(b_no)

            self.mouse_handlers.append(b_yes.handle_mouse_event)
            self.mouse_handlers.append(b_no.handle_mouse_event)

        counter = 0
        if self.background_theme == 'light':
            for i, (text, func_on_click) in enumerate((('0', on_digit), ('1', on_digit), ('2', on_digit), ('3', on_digit), ('4', on_digit), ('5', on_digit), ('6', on_digit),
                                                       ('7', on_digit), ('8', on_digit), ('9', on_digit))):
                if i < 5:
                    b = Button(c.game_offset_x + (c.game_button_width + 55) * i, c.game_offset_y, c.game_button_width, c.game_button_height, text, c.text_color_light, 45,
                               func_on_click, padding_x=5.4, border_radius=20, game_mode=True)
                else:
                    b = Button(c.game_offset_x + (c.game_button_width + 55) * counter, c.game_offset_y + 81, c.game_button_width, c.game_button_height, text, c.text_color_light,
                               45,
                               func_on_click, padding_x=5.4, border_radius=20, game_mode=True)
                    counter += 1

                self.objects.append(b)
                self.game_buttons.append(b)
                self.mouse_handlers.append(b.handle_mouse_event)

        elif self.background_theme == 'dark':
            for i, (text, func_on_click) in enumerate((('0', on_digit), ('1', on_digit), ('2', on_digit), ('3', on_digit), ('4', on_digit), ('5', on_digit), ('6', on_digit),
                                                       ('7', on_digit), ('8', on_digit), ('9', on_digit))):
                if i < 5:
                    b = Button(c.game_offset_x + (c.game_button_width + 55) * i, c.game_offset_y, c.game_button_width, c.game_button_height, text, c.text_color_dark, 45,
                               func_on_click, padding_x=5.4, theme='dark', border_radius=20, game_mode=True)
                else:
                    b = Button(c.game_offset_x + (c.game_button_width + 55) * counter, c.game_offset_y + 81, c.game_button_width, c.game_button_height, text, c.text_color_dark, 45,
                               func_on_click, padding_x=5.4, theme='dark', border_radius=20, game_mode=True)
                    counter += 1

                self.objects.append(b)

                self.mouse_handlers.append(b.handle_mouse_event)


        input_field_border = GameObject(127, 395, 360, 72, colors.BLACK)
        input_field = GameObject(130, 400, 354, 62)
        if self.max_len == 8:
            input_field_border = GameObject(87, 395, 400, 72, colors.BLACK)
            input_field = GameObject(90, 400, 394, 62)

        self.objects.append(input_field_border)
        self.objects.append(input_field)

        b_confirm = Button(497, 403, 56, 55, 'V', c.text_color_light, 45, on_confirm, padding_x=5.4, border_radius=50)
        if self.background_theme == 'dark':
            b_confirm = Button(497, 403, 56, 55, 'V', c.text_color_dark, 45, on_confirm, padding_x=5.4, border_radius=50, theme='dark')

        self.objects.append(b_confirm)

        self.mouse_handlers.append(b_confirm.handle_mouse_event)

        arrow_1 = TextObject(285, 460, lambda: '<', c.text_color_light, 80)
        arrow_2 = TextObject(300, 463, lambda: '-', c.text_color_light, 80)
        arrow_3 = TextObject(315, 463, lambda: '-', c.text_color_light, 80)
        arrow_4 = TextObject(330, 463, lambda: '-', c.text_color_light, 80)
        b_delete = Button(222, 489, 172, 60, '', c.text_color_light, 80, on_delete, border_radius=15, delete_mode=True)
        if self.background_theme == 'dark':
            b_delete = Button(222, 489, 172, 60, '', c.text_color_light, 80, on_delete, border_radius=15, delete_mode=True, theme='dark')

        self.objects.append(b_delete)
        self.objects.append(arrow_1)
        self.objects.append(arrow_2)
        self.objects.append(arrow_3)
        self.objects.append(arrow_4)

        self.mouse_handlers.append(b_delete.handle_mouse_event)

        hints_field_border = GameObject(12, 10, 576, 320, colors.BLACK)
        hints_field = GameObject(15, 15, 570, 310, colors.WHITE)
        if self.background_theme == 'dark':
            hints_field = GameObject(15, 15, 570, 310, colors.PUMICE)

        self.objects.append(hints_field_border)
        self.objects.append(hints_field)

        b_quit = Button(5, 735, 590, 50, 'Завершить игру', c.text_color_light, 32, on_quit, padding_x=17.5, quit_mode=True)

        self.objects.append(b_quit)
        self.mouse_handlers.append(b_quit.handle_mouse_event)


    def win(self):

        def back_to_menu(button):
            self.objects.clear()

            self.mouse_handlers.clear()

            self.create_menu()

        def new_game(button):
            self.objects.clear()
            self.mouse_handlers.clear()
            self.secret_num = generate_secret_number(self.max_len)
            self.game_field()

        win_message = TextObject(300, 45, lambda: 'ВЫ ПОБЕДИЛИ', c.text_color_light, 50)
        attempts_amount = TextObject(300, 150, lambda: f'Количество попыток: {self.user_attempts}', c.text_color_light, 45)
        secret_number_text = TextObject(300, 250, lambda: 'Загаданное число:', c.text_color_light, 45)
        secret_number = TextObject(300, 400, lambda: f'{self.secret_num}', c.text_color_light, 100)
        b_back_to_menu = Button(70, 640, c.settings_button_w, c.settings_button_h + 50, 'Меню', c.text_color_light, 60, back_to_menu, padding_x=10.2, padding_y=14)
        b_new_game = Button(330, 640, c.settings_button_w, c.settings_button_h + 50, 'Новая игра', c.text_color_light, 40, new_game, padding_x=10.2, padding_y=30)

        if self.background_theme == 'dark':
            win_message = TextObject(300, 45, lambda: 'ВЫ ПОБЕДИЛИ', c.text_color_dark, 50)
            attempts_amount = TextObject(300, 150, lambda: f'Количество попыток: {self.user_attempts}', c.text_color_dark, 45)
            secret_number_text = TextObject(300, 250, lambda: 'Загаданное число:', c.text_color_dark, 45)
            secret_number = TextObject(300, 400, lambda: f'{self.secret_num}', c.text_color_dark, 100)
            b_back_to_menu = Button(70, 640, c.settings_button_w, c.settings_button_h + 50, 'Меню', c.text_color_dark, 60, back_to_menu, padding_x=10.2, padding_y=14, theme='dark')
            b_new_game = Button(330, 640, c.settings_button_w, c.settings_button_h + 50, 'Новая игра', c.text_color_dark, 40, new_game, padding_x=10.2, padding_y=30, theme='dark')


        self.objects.append(win_message)
        self.objects.append(attempts_amount)
        self.objects.append(secret_number_text)
        self.objects.append(secret_number)
        self.objects.append(b_back_to_menu)
        self.objects.append(b_new_game)

        self.mouse_handlers.append(b_back_to_menu.handle_mouse_event)
        self.mouse_handlers.append(b_new_game.handle_mouse_event)


    def create_objects(self):
        self.create_menu()

    def create_labels(self):
        pass

    def update(self):
        if not self.is_game_running:
            return



    def show_message(self, text, x=c.screen_width // 2, y=c.screen_height // 2 - 350, color=(153, 153, 153), font_size=40, centralized=True, sleep=c.message_duration):
        message = TextObject(x, y, lambda: text, color, font_size)
        self.draw()
        message.draw(self.surface, centralized)
        pygame.display.update()
        time.sleep(sleep)


def main():
    Bulls_And_Cows().run()


if __name__ == '__main__':
    main()
