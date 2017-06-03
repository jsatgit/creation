import pygame
import random

class BaseGame(object):
    def __init__(self, dim=[500,500], fps=10):
        self.dim = dim
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.screen = None

    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.dim)
        is_running = True
        while is_running:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
            self.render()
            pygame.display.flip()
        pygame.quit()

def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

RED =   (255,   0,   0)

class Game(BaseGame):
    def __init__(self):
        super(Game, self).__init__()
        self.block_size = 10

    def render(self):
        width, height = self.dim
        n_blocks_wide = width / self.block_size 
        n_blocks_tall = height / self.block_size 

        for i in xrange(n_blocks_tall):
            for j in xrange(n_blocks_wide):
                rect = [
                    self.block_size * j,
                    self.block_size * i, 
                    self.block_size, 
                    self.block_size
                ]
                pygame.draw.rect(self.screen, rand_color(), rect)

game = Game()
game.start()
