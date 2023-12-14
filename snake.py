import pygame
pygame.init()
pygame.display.set_caption("snake")

#paramètres du jeu

taille_ecran=600
nombre_carreaux=20                      #nombre pair
vitesse=2
width=taille_ecran
height=taille_ecran 
taille_carreau= taille_ecran/nombre_carreaux
couleur_serpent=(250,105,105)
couleur_fruit=(250,105,250)
couleur1_damier=(155, 245, 165)
couleur2_damier=(155, 230, 190)
                     


#fonctions générales

def listeaddition(l1,l2):
    l3=[]
    for i in range(len(l1)):
        l3.append(l1[i]+l2[i])
    return(l3)

def convpixel(pos):                        #effectue la conversion d'une position en carreaux [c1,c2] en pixels sur l'écran [x,y]
    L=[]
    for j in pos:
        L.append(j*taille_carreau,)
    return(L)

#fonctions d'affichage


def afficher_carreau(position:list,couleur:tuple,taille:int):       #affiche un carré 
    rect2=pygame.Rect(position[0],position[1],taille,taille)
    pygame.draw.rect(screen,couleur,rect2)
    pygame.display.update()


def afficher_damier():
    screen.fill( couleur1_damier )                             
    for j in range(nombre_carreaux):                                         #construction du damier 
        y=taille_carreau*j
        for i in range(nombre_carreaux//2):
            x=2*taille_carreau*i +taille_carreau*(j%2)
            rect = pygame.Rect(x, y, taille_carreau, taille_carreau)
            pygame.draw.rect(screen, couleur2_damier, rect)

        



clock = pygame.time.Clock()
screen = pygame.display.set_mode( (width, height) )




class snake():
    def __init__(self):
        self.vitesse=[[0,1],[1,0],[-1,0],[0,-1]]      #haut:0 droite:1 gauche:2 bas:3 
        self.size=3
        self.direction='right'
        self.body=[[8,10],[9,10],[10,10]]
    def directionconv(self,direction):
        if direction=='right':
            return 1
        if direction=='left':
            return 2
        if direction=='up':
            return 0
        if direction=='down':
            return 3
    def update(self):
        self.body.append(listeaddition(self.body[-1],self.vitesse[self.directionconv(self.direction)]))
        self.body.pop(0)
    def display(self):
        for l in range(self.size):
            afficher_carreau(convpixel(self.body[l]),couleur_serpent,taille_carreau)

            

serpent=snake()




while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                if not direction=='right':
                    direction='left'
            if event.key == pygame.K_d:
                if not direction=='left':
                    direction='right'
            if event.key == pygame.K_s:
                if not direction=='up':
                    direction='down'
            if event.key == pygame.K_z:
                if not direction=='down':
                    direction='up'
        

        
        pass 
   
    clock.tick(vitesse)
    serpent.update()
    afficher_damier()
    serpent.display()

    


    pygame.display.update()


pygame.quit()

