import pyxel
import time
import random

class Jeu:
    def __init__(self):

        # taille de la fenetre 224x256 pixels
        # ne pas modifier
        self.width = 224
        self.height = 256
        self.vaisseau = Vaisseau(self, Alien) # je passe le jeu au vaisseau 
        self.alien = Alien(self)
        pyxel.init(self.width, self.height, title="Space Invader", fps=60)
        pyxel.run(self.update, self.draw)
        self.aliens = self.create_aliens()


    def create_aliens(self):
        matrix =[]
        posy = 0
        for i in range(5):
            line = []
            posx = 0
            for j in range(11):
                new_alien = Alien(self)
                new_alien.x = posx
                posx += 10
                line.append(new_alien)   
            matrix.append(line)   
            posy += 10 
        print(matrix)
        return matrix
    def do_object_overlap(obj1, obj2)
        l1 = obj1.x
        r1 =         

    def do_overlap(l1, r1, l2, r2):
     
     # if rectangle has area 0, no overlap
        if l1[0] == r1[0] or l1[1] == r1[1] or r2[0] == l2[0] or l2[1] == r2[1]:
            return False
     
        # If one rectangle is on left side of other
        if l1[0] > r2[0] or l2[0] > r1[0]:
            return False
 
        # If one rectangle is above other
        if r1[1] > l2[1] or r2[1] > l1[1]:
            return False
 
        return True

    # =====================================================
    # == UPDATE
    # =====================================================
    def update(self):
        """mise à jour des variables (60 fois par seconde)"""

        # deplacement du vaisseau
        self.vaisseau.vaisseau_deplacement()
        self.vaisseau.bullet_move()
        self.vaisseau.ship_shoot()
        self.alien.alien_move()

        

    # =====================================================
    # == DRAW
    # =====================================================
    def draw(self):
        """création et positionnement des objets (30 fois par seconde)"""

        # vide la fenetre
        pyxel.cls(0)

        #vaisseau
        self.vaisseau.draw()

        # bullet 
        self.vaisseau.bullet_draw()

        #alien
        self.alien.alien_draw()



class Geometry(self):
    def __init__(self):
        self.x
        self.y
        
            

class Vaisseau:
    def __init__(self, jeu, alien) :
        self.jeu = jeu
        self.alien = alien
        # position initiale du vaisseau
        self.vaisseau_x = self.jeu.width//2
        self.vaisseau_y = self.jeu.height - 32 
        self.bullet_x = None
        self.bullet_y = None
    
    def vaisseau_deplacement(self):
        """déplacement avec les touches de directions"""

        if pyxel.btn(pyxel.KEY_RIGHT) and self.vaisseau_x<self.jeu.width-8:
            self.vaisseau_x += 2
        if pyxel.btn(pyxel.KEY_LEFT) and self.vaisseau_x>0:
            self.vaisseau_x += -2

    def ship_shoot(self):
        """ Fait tirer le vaisseau"""
        if pyxel.btn(pyxel.KEY_SPACE) and self.bullet_x == None:
            self.bullet_x = self.vaisseau_x+3
            self.bullet_y = self.vaisseau_y

    def bullet_move(self):
        """fait bouger les tirs"""
        if self.bullet_x is not None :
            self.bullet_y -= 3
            if self.bullet_y < -4 :
              self.bullet_x = None
              self.bullet_y = None

    def bullet_draw(self):
      if self.bullet_x is not None :
        pyxel.rect(self.bullet_x, self.bullet_y, 2, 4, 7)
    
    def bullet_hit(self):
        pass
    
    
    def draw(self):
        # vaisseau (carre 8x8)
        pyxel.rect(self.vaisseau_x, self.vaisseau_y, 8, 8, 7)

    def update(self):
        #vaisseau
        self.vaisseau_deplacement()
        self.bullet_move()
        self.ship_shoot()

class Alien:
    def __init__(self, jeu):
        self.jeu = jeu
        self.x = 0
        self.y = 0
        self.deathx = 0
        self.deathy = 0
        self.alien_destroyed = False

    def alien_draw(self):
        for g in range(20,170,30) :
            for i in range(20,240,30) :
                if self.alien_destroyed == False :
                    pyxel.rect(self.x + i, self.y + g, 8, 8, 8)

    def alien_move(self):
        if pyxel.frame_count%15 == 0 :
            if self.x > 0 :
                self.x -= 8
            elif self.x < self.jeu.width-8 :
                self.x += 8

        


    
jeu = Jeu() 