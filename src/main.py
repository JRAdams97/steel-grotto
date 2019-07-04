import pygame
import yaml
from pygame.locals import *


class Game:

    def __init__(self):
        self._config = None
        self._display_surf = None
        self._running = True

    # -----------------------------------------------------------------
    # Property Access
    # -----------------------------------------------------------------
    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, n_config):
        self._config = n_config

    @property
    def display_surf(self):
        return self._display_surf

    @display_surf.setter
    def display_surf(self, n_display_surf):
        self._display_surf = n_display_surf

    @property
    def running(self):
        return self._running

    @running.setter
    def running(self, n_running):
        self._running = n_running

    # -----------------------------------------------------------------
    # Private Class Functions
    # -----------------------------------------------------------------
    def _on_init(self):
        pygame.init()

        self.config = self._load_configuration()
        self.display_surf = pygame.display.set_mode((self.config['game_window']['width'],
                                                     self.config['game_window']['height']))
        return self.display_surf

    @staticmethod
    def _load_configuration():
        with open("conf/grotto.yaml", 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    # -----------------------------------------------------------------
    # Public Class Functions
    # -----------------------------------------------------------------
    def on_event(self, event):
        if event.type == QUIT:
            self.running = False

    def on_loop(self):
        pass

    def on_render(self):
        pass

    @staticmethod
    def on_cleanup():
        pygame.quit()

    def on_execute(self):
        try:
            self._on_init()
        except pygame.error:
            self.running = False

        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

        self.on_cleanup()


if __name__ == "__main__":
    gameInstance = Game()
    gameInstance.on_execute()
