import pygame

from game_object import GameObject
from text_object import TextObject
import config as c


class Button(GameObject):
    def __init__(self, x, y, w, h, text, text_color, text_size, func_on_click=lambda x: None, padding_x=0, padding_y=0, theme='light', border_radius=10, game_mode=False,
                 delete_mode=False, win_mode=False, quit_mode=False, difficulty=None):
        super().__init__(x, y, w, h)
        self.func_on_click = func_on_click
        self.text_to_return = text
        self.text = TextObject(x + padding_x ** 2, y + padding_y, lambda: text, text_color, text_size)
        self.state = 'normal'
        self.theme = theme
        self.border_radius = border_radius
        self.game_mode = game_mode
        self.delete_mode = delete_mode
        self.win_mode = win_mode
        self.quit_mode = quit_mode
        self.difficulty = difficulty

    @property
    def back_color(self):
        if self.difficulty == 'medium':
            return dict(normal=c.button_medium_color,
                        hover=c.button_medium_color_hover,
                        pressed=c.button_medium_color_pressed)[self.state]
        elif self.difficulty == 'medium' and self.theme == 'dark':
            return dict(normal=c.button_medium_color_pressed,
                        hover=c.button_medium_color_hover,
                        pressed=c.button_medium_color)[self.state]
        elif self.difficulty == 'hard':
            return dict(normal=c.button_delete_color,
                        hover=c.button_delete_color_hover,
                        pressed=c.button_delete_color_pressed)[self.state]
        elif self.difficulty == 'hard' and self.theme == 'dark':
            return dict(normal=c.button_delete_color_pressed,
                        hover=c.button_delete_color_hover,
                        pressed=c.button_delete_color)[self.state]
        elif self.quit_mode:
            return dict(normal=c.button_quit_color,
                        hover=c.button_quit_color_hover,
                        pressed=c.button_quit_color_pressed)[self.state]
        elif self.delete_mode and self.theme == 'light':
            return dict(normal=c.button_delete_color,
                        hover=c.button_delete_color_hover,
                        pressed=c.button_delete_color_pressed
                        )[self.state]
        elif self.delete_mode and self.theme == 'dark':
            return dict(normal=c.button_delete_dark_color,
                        hover=c.button_delete_dark_color_hover,
                        pressed=c.button_delete_dark_color_pressed
                        )[self.state]
        elif self.game_mode and self.theme == 'light':
            return dict(normal=c.button_game_color,
                        hover=c.button_game_color_hover,
                        pressed=c.button_game_color_pressed
                        )[self.state]
        elif self.game_mode and self.theme == 'dark':
            return dict(normal=c.button_game_dark_color,
                        hover=c.button_game_dark_color_hover,
                        pressed=c.button_game_dark_color_pressed
                        )[self.state]
        elif self.theme == 'light':
            return dict(normal=c.button_menu_color,
                        hover=c.button_menu_color_hover,
                        pressed=c.button_menu_color_pressed
                        )[self.state]
        elif self.theme == 'dark':
            return dict(normal=c.button_menu_dark_color,
                        hover=c.button_menu_dark_color_hover,
                        pressed=c.button_menu_dark_color_pressed
                        )[self.state]

    def draw(self, surface):
        pygame.draw.rect(surface, self.back_color, self.bounds, border_radius=self.border_radius)
        self.text.draw(surface)

    def get_text(self):
        return self.text_to_return

    def handle_mouse_event(self, type, pos):
        if type == pygame.MOUSEMOTION:
            self.handle_mouse_move(pos)
        elif type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_down(pos)
        elif type == pygame.MOUSEBUTTONUP:
            self.handle_mouse_up(pos)

    def handle_mouse_move(self, pos):
        if self.bounds.collidepoint(pos):
            if self.state != 'pressed':
                self.state = 'hover'
        else:
            self.state = 'normal'

    def handle_mouse_down(self, pos):
        if self.bounds.collidepoint(pos):
            self.state = 'pressed'

    def handle_mouse_up(self, pos):
        if self.state == 'pressed':
            self.func_on_click(self)
            self.state = 'hover'

