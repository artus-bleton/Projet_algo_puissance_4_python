import numpy as np
from Module.joueur import joueur
import pygame
red_color=1
yellow_color=-1
red_score=4
yellow_score=-4

class terrain:
    
    def __init__(self):
       
        self.board=np.zeros((6,7))
        self.pion=49
        self.red_color=1
        self.yellow_color=-1
        self.red_score=4
        self.yellow_score=-4
 
        
    def poser_pion(self,joueur,column):
        
           # On a enlever take pose par 

        if( column>7 or column <0) and self.pion>0:
            
            print('Erreur: Les coordonnees ne sont pas conformes a la grille ou il y a plus de pion')  # changer le if
        
        for x in range(5,-1,-1):
            
            if self.board[x][column]==0 and  joueur.color=='R':
                self.board[x][column]=red_color
                self.pion-=self.pion
                break
            
            elif self.board[x][column]==0 and  joueur.color=='J':
                 self.board[x][column]=yellow_color
                 self.pion-=self.pion

                 break
    
            
    def test_horizontale(self):
            winner = ""
            # variable utilisee pour la boucle while
            
            # variable qui sert a arret si on trouve le winner
            stop = False
            # raisonnement similaire, plus performant qu'un parcours traditionnel
            # on boucle tant qu'on n'a pas atteint (la line) 0 et que l'on a pas de winner
            # le while nous permet de nous deplacer dans les lines de bas en haut (line 5 --> line 0)
            for line in range(5,0,-1):
                
                 for column in range(4):  # ca nous permet deplacer dans les columns
                    # pourquoi 4 ? 4 possibilites de gagner dans une line
                    # on determine le winner en fonction des valeurs definies dans les 4 columns (que l'on decale grace a la variable column) que l'on regarde pour la line donnee i
                    if self.board[line][column] + self.board[line][column + 1] + self.board[line][column + 2] +  self.board[line][column + 3] ==red_score:  # gamer jaune gagne
                        # on affecte le winner (car on a nom nombre de points)
                        winner = "rouge"
                    if self.board[line][column] + self.board[line][column + 1] + self.board[line][column + 2] +self.board[line][column + 3] == yellow_score:  # gamer rouge gagne
                        winner = "jaune"
                        
                      
                # on remonte la line
            
            # retourne la variable winner
            return winner

    def test_vertical(self):
            winner = ""
            # on regarde chaque column
            for column in range(7):
                # on descend les lines pour la column concernee, pour verifier s'il y a un winner
                # tant que la line est strictement superieur a 2
                # 5 YELLOW_WINNER 3 en baissant de -1 (3eme parametre du for)
                # c'est plus concis que ce qu'on a au-dessous
                for line in range(5, 2, -1):
                    if self.board[line][column] + self.board[line - 1][column] + self.board[line - 2][column] + self.board[line - 3][column] == yellow_score:
                        winner = "jaune"
                    if self.board[line][column] + self.board[line - 1][column] + self.board[line - 2][column] + self.board[line - 3][column] ==red_score:
                        winner = "rouge"
            return winner

    def test_diagonal(self):
            
            winner = ""
            # on va diagonale d'en haut a gauche vers en bas a droite
            # on avance dans les lines
            for line in range(3):
                # on avance dans les columns
                for column in range(4):
                    # vu que c'est en meme on avance en diagonale
                    if self.board[line][column] + self.board[line + 1][column + 1] + self.board[line + 2][column + 2] + self.board[line + 3][column + 3] ==red_score:
                        winner = "rouge"
                    if self.board[line][column] + self.board[line + 1][column + 1] + self.board[line + 2][column + 2] + self.board[line + 3][column + 3] == yellow_score:
                        winner = "jaune"
            # on va diagonale d'en haut a droite vers en bas a gauche
            for line in range(3):
                # 0 1 2 3, la line a laquelle on commence
                for column in range(3, 7):
                    # 3 4 5 6, on commence a la column 3 pour aller vers la 6
                    if self.board[line][column] + self.board[line + 1][column - 1] + self.board[line + 2][column - 2] +self.board[line + 3][column - 3] == yellow_score:
                        winner = "jaune"
                    if self.board[line][column] + self.board[line + 1][column - 1] + self.board[line + 2][column - 2] + self.board[line + 3][column - 3] == red_score:
                        winner = "rouge"
            return winner


    def test_vainqueur(self):
      
       if self.test_diagonal()=='rouge' or self.test_horizontale()=='rouge' or self.test_vertical()=='rouge': 
             mbappé=pygame.image.load('image/th.jpg')
             dim= mbappé.get_size()
             ecran=pygame.display.set_mode(dim)
             ecran.blit(mbappé,(0,0))   
             pygame.display.set_caption('Le joueur Rouge a Gagné',)
               
               

               
               
              
               
       if self.test_diagonal()=='jaune' or self.test_horizontale()=='jaune' or self.test_vertical()=='jaune':  #faire une fonction ici
             print('LE JOUEUR JAUNE A GAGNE')
             pygame.quit()
             

 
             

 


   

              
         

            

        
