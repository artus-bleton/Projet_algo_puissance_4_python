from Module.joueur import joueur
from Module.Terrain import terrain
import numpy as np
import pygame
pygame.init()
class jeu:
   

   
  def __init__(self):
    
   self.ecran_de_jeu=pygame.display.set_mode((692,590))
   self.arriere_plan=pygame.image.load('image/plateau.png').convert()
   self.pion_jaune=pygame.image.load('image/pion_jaune.png')
   self.pion_rouge=pygame.image.load('image/pion_rouge.png')
    

  def initialisation_fenetre_de_jeu(self):
     pygame.display.set_caption("Premiere fenetre")

     self.ecran_de_jeu.blit(self.arriere_plan,(0,0))
     pygame.display.flip()
 
  def commencer_jeu(self):
     
     J1=joueur()
     J1.color='R'
     T=terrain()

     
     boucle=True

     print(T.board)

     while boucle:
        
         
        for event in pygame.event.get():

            if event.type==pygame.MOUSEBUTTONUP:
                
                x,y=pygame.mouse.get_pos()
                print(x,y)
                column=x/100 
                T.poser_pion(J1,int(column))
                self.actualiser(T)
                print(T.board)
                T.test_vainqueur()
                changer_joueur(J1)
                pygame.display.flip()
            
               
            
            if event.type==pygame.QUIT:
               boucle=False
   
          
  def actualiser(self,terrain):
   
   self.ecran_de_jeu.fill((0, 0, 0))
   self.ecran_de_jeu.blit(self.arriere_plan, (0, 0))
   terrain_renverser=np.flipud(terrain.board)
      
   for i in range(6):
        
        for j in range(7):
           
           if terrain_renverser[i][j] == terrain.red_color:
                    # on place une image d'un pion jaune sur l'écran en fonction de la colonne ou l'on se situe
                    self.ecran_de_jeu.blit(self.pion_rouge, (16 + 97 * j, 13 - 97.5 * i + 486))
           pygame.display.flip()
                # cas du joueur rouge
           if terrain_renverser[i][j] == terrain.yellow_color:
                    # on place une image d'un pion rouge sur l'écran en fonction de la colonne ou l'on se situe
                    self.ecran_de_jeu.blit(self.pion_jaune, (16 + 97 * j, 13 - 97.5 * i + 486))
           pygame.display.flip()       
              
              
           
     
     

def changer_joueur(joueur):
      
   if joueur.color=='R':       # faire une fonction ici
         joueur.color='J'   
   else:
         joueur.color='R'
         

        

            
    