#!pip install pygame
import pygame
import time
import random

# Initialiser pygame
pygame.init()

# Dimensions de l'écran
largeur = 800
hauteur = 600

# Couleurs
noir = (0, 0, 0)
blanc = (255, 255, 255)
rouge = (213, 50, 80)
vert = (0, 255, 0)
bleu = (50, 153, 213)

# Taille du bloc et vitesse
taille_bloc = 20 #taille du carré en pixel à afficher
vitesse = 15

# Initialisation de l'écran
fenetre = pygame.display.set_mode((largeur, hauteur)) #création de la fenêtre
pygame.display.set_caption("Jeu du Serpent") #nom de la fenêtre

# Horloge pour contrôler la vitesse
horloge = pygame.time.Clock()

# Police pour le texte
police_style = pygame.font.SysFont("bahnschrift", 25)
police_score = pygame.font.SysFont("comicsansms", 35)

# Meilleur score (initialisé à 0)
meilleur_score = 0

def afficher_score(score, meilleur):
    valeur = police_score.render(f"Score: {score}", True, blanc)
    meilleur_valeur = police_score.render(f"Meilleur score: {meilleur}", True, blanc)
    fenetre.blit(valeur, [10, 10]) #affiche la valeur dans la fenêtre à la position [10, 10]
    fenetre.blit(meilleur_valeur, [largeur - 350, 10])

def notre_serpent(taille_bloc, liste_corps):
    for x in liste_corps:
        pygame.draw.rect(fenetre, vert, [x[0], x[1], taille_bloc, taille_bloc])

def message(msg, couleur):
    texte = police_style.render(msg, True, couleur)
    fenetre.blit(texte, [largeur / 6, hauteur / 3])

def jeu(meilleur_score):



    game_over = False #le joueu n'a pas perdu
    game_close = False

    #position initial du serpent. Placement au centre
    x1 = largeur / 2
    y1 = hauteur / 2

    #variation de la position du serpent sur la fenêtre
    x1_change = 0
    y1_change = 0

    liste_corps = []
    longueur_serpent = 1

    #position aléatoire de la nourriture sur la fenêtre
    nourriture_x = round(random.randrange(0, largeur - taille_bloc) / 20.0) * 20.0
    nourriture_y = round(random.randrange(0, hauteur - taille_bloc) / 20.0) * 20.0

    while not game_over:

        while game_close:
            fenetre.fill(noir)
            message("Perdu! Appuyez sur C pour rejouer ou Q pour quitter", rouge)
            afficher_score(longueur_serpent - 1, meilleur_score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  #Appuyer sur la touche Q pour quitter le jeu
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c: #Appuyer sur la touche C pour continuer à jouer
                        jeu(meilleur_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            #Appuyer les flèches de déplacement pour déplacer le serpent
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -taille_bloc
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = taille_bloc
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -taille_bloc
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = taille_bloc
                    x1_change = 0

        if x1 >= largeur or x1 < 0 or y1 >= hauteur or y1 < 0:
            game_close = True #le serpent sort de la fenêtre, GAME OVER !
        x1 += x1_change
        y1 += y1_change
        fenetre.fill(bleu)
        #déssine la nourriture sur la fenêtre
        pygame.draw.rect(fenetre, rouge, [nourriture_x, nourriture_y, taille_bloc, taille_bloc])

        tete = []
        tete.append(x1)
        tete.append(y1)
        liste_corps.append(tete)
        if len(liste_corps) > longueur_serpent:
            del liste_corps[0]

        for bloc in liste_corps[:-1]:
            if bloc == tete:
                game_close = True # Si le serpent touche son corps, GAME OVER !

        notre_serpent(taille_bloc, liste_corps)
        afficher_score(longueur_serpent - 1, meilleur_score)

        pygame.display.update()

        if x1 == nourriture_x and y1 == nourriture_y:
            #Si le serpent mange la nourriture, ajoute un aléatoire une autre sur la fenêtre
            nourriture_x = round(random.randrange(0, largeur - taille_bloc) / 20.0) * 20.0
            nourriture_y = round(random.randrange(0, hauteur - taille_bloc) / 20.0) * 20.0
            longueur_serpent += 1

            if longueur_serpent - 1 > meilleur_score:
                meilleur_score = longueur_serpent - 1

        horloge.tick(vitesse)

    pygame.quit()
    quit()

jeu(meilleur_score)
