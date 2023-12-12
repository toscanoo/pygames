import pygame
pygame.init()
pygame.display.set_caption("snake")
width=600
height=600

def afficher_carreau(position,couleur,taille):
    rect2=pygame.Rect(position[0],position[1],taille,taille)
    pygame.draw.rect(screen,couleur,rect2)
    pygame.display.update()


couleur_serpent=(250,105,105)
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (width, height) )
screen.fill( (155, 245, 165) ) # Fill screen with green
tilescolor = (155, 230, 190) # blue
for j in range(20):
    y=30*j
    for i in range(10):
        x=60*i +30*(j%2)
        rect = pygame.Rect(x, y, 30, 30)
        pygame.draw.rect(screen, tilescolor,rect)

def convpixel(tuple):
    

afficher_carreau((300,300),couleur_serpent,20)
pygame.display.update()
class snake():
    def __init__():
        self.vitesse=[(0,1),(1,0),(-1,0),(0,-1)]      #haut:0 droite:1 gauche:2 bas:3 
        self.size=3
        self.dir='right'
        self.body=[(8,10),(9,10),(10,10)]
    def dirconv(dir):
        if dir=='right':
            return 1
        if dir=='left':
            return 2
        if dir=='up':
            return 0
        if dir=='down':
            return 3
    def uptdate():
        self.body.append(self.body[-1]+self.vitesse[self.dirconv(self.dir)])
        self.body.pop(0)
    def display():
        for l in range(self.size):
            afficher_carreau(convpixel(self.body[l]),couleur_serpent,30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                dir='left'
            if event.key == pygame.K_d:
                dir='right'
        

        
        pass # do nothing for the moment
    # Wait one second, starting from last display or now
    clock.tick(1)


pygame.quit()

