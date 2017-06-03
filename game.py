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
        self.first_render()
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

class Resource(object):
    def __init__(self, name):
        self.name = name 
        self.color = rand_color()

class Grid(object):
    def __init__(self, n, m):
        self.grid = None
        self.resources = [
            Resource('Sigma'),
            Resource('Doorstep'),
            Resource('Minger'),
            Resource('Rainier'),
            Resource('Realsting'),
            Resource('Lolcat')
        ]
        self.n = n
        self.m = m
        self.init_grid()

    def rand_resource(self):
        i = random.randint(0, len(self.resources) - 1)
        return self.resources[i]

    def init_grid(self):
        self.grid = [
            [self.rand_resource() for j in xrange(self.m)] 
            for i in xrange(self.n)
        ]

    def get(self, i, j):
        return self.grid[i][j]

class Game(BaseGame):
    def __init__(self):
        super(Game, self).__init__()
        self.block_size = 10
        m, n = self.dim
        self.grid = Grid(n, m)

    def draw_grid(self):
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
                resource = self.grid.get(i, j)
                pygame.draw.rect(self.screen, resource.color, rect)

    def first_render(self):
        self.draw_grid()

    def render(self):
        left, mid, right = pygame.mouse.get_pressed()
        if left:
            w, h = pygame.mouse.get_pos()
            j = w / self.block_size
            i = h / self.block_size
            resource = self.grid.get(i, j)
            print resource.name


game = Game()
game.start()
