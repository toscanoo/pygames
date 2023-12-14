import pygame

pygame.init()
pygame.display.set_caption("snake")

# paramètres du jeu

SIZE_ecran = 600
SQUARE_NUMBER = 20  # nombre pair
speed = 2
width = SIZE_ecran
height = SIZE_ecran
SQUARE_SIZE = SIZE_ecran / SQUARE_NUMBER
SNAKE_COLOR = (250, 105, 105)
FRUIT_COLOR = (250, 105, 250)
GRID_COLOR1 = (155, 245, 165)
GRID_COLOR2 = (155, 230, 190)


# fonctions générales


def list_sum(l1, l2):
    l3 = []
    for i in range(len(l1)):
        l3.append(l1[i] + l2[i])
    return l3


def convpixel(
    pos,
):  # effectue la conversion d'une position en carreaux [c1,c2] en pixels sur l'écran [x,y]
    L = []
    for j in pos:
        L.append(
            j * SQUARE_SIZE,
        )
    return L


# fonctions d'affichage


def display_square(position: list, color: tuple, SIZE: int):  # affiche un carré
    rect2 = pygame.Rect(position[0], position[1], SIZE, SIZE)
    pygame.draw.rect(screen, color, rect2)
    pygame.display.update()


def display_grid():
    screen.fill(GRID_COLOR1)
    for j in range(SQUARE_NUMBER):  # construction du damier
        y = SQUARE_SIZE * j
        for i in range(SQUARE_NUMBER // 2):
            x = 2 * SQUARE_SIZE * i + SQUARE_SIZE * (j % 2)
            rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, GRID_COLOR2, rect)


clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))


class snake:
    def __init__(self):
        self.speed = [
            [0, 1],
            [1, 0],
            [-1, 0],
            [0, -1],
        ]  # haut:0 droite:1 gauche:2 bas:3
        self.size = 3
        self.direction = "right"
        self.body = [[8, 10], [9, 10], [10, 10]]

    def directionconv(self, direction):
        if direction == "right":
            return 1
        if direction == "left":
            return 2
        if direction == "up":
            return 0
        if direction == "down":
            return 3

    def update(self):
        self.body.append(
            list_sum(self.body[-1], self.speed[self.directionconv(self.direction)])
        )
        self.body.pop(0)

    def display(self):
        for l in range(self.size):
            display_square(convpixel(self.body[l]), SNAKE_COLOR, SQUARE_SIZE)


snake = snake()


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                if not direction == "right":
                    direction = "left"
            if event.key == pygame.K_d:
                if not direction == "left":
                    direction = "right"
            if event.key == pygame.K_s:
                if not direction == "up":
                    direction = "down"
            if event.key == pygame.K_z:
                if not direction == "down":
                    direction = "up"

        pass

    clock.tick(speed)
    snake.update()
    display_grid()
    snake.display()

    pygame.display.update()


pygame.quit()
