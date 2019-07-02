import pygame
from pygame.locals import *


class Game:

    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 480
    X = 10
    Y = 10

    def __init__(self):
        self._running = True
        self._display_surf = None

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT),
                                                     pygame.HWSURFACE)
        self._running = True

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        pass

    @staticmethod
    def on_cleanup():
        pygame.quit()

    def on_execute(self):
        if not self.on_init():
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    gameInstance = Game()
    gameInstance.on_execute()
