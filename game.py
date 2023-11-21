import pyxel

class Jeu:
    def __init__(self):

        # taille de la fenetre 128x128 pixels
        # ne pas modifier
        self.width = 128
        self.height = 128
        pyxel.init(self.width, self.height, title="Space Invader")

        # position initiale du vaisseau
        # (origine des positions : coin haut gauche)
        self.vaisseau_x = self.width//2
        self.vaisseau_y = self.height -8
        self.bullet_x = None
        self.bullet_y = None

        pyxel.run(self.update, self.draw)

    def ship_shoot(self):
        if pyxel.btn(pyxel.KEY_SPACE) :
            self.bullet_x = self.vaisseau_x+4
            self.bullet_y = self.vaisseau_y

    def bullet_move(self):
        if self.bullet_x is not None :
            print(self.bullet_y)
            self.bullet_y -= 1
            if self.bullet_y < -4 :
              self.bullet_x = None
              self.bullet_y = None

    def vaisseau_deplacement(self):
        """déplacement avec les touches de directions"""

        if pyxel.btn(pyxel.KEY_RIGHT) and self.vaisseau_x<self.width-8:
            self.vaisseau_x += 2
        if pyxel.btn(pyxel.KEY_LEFT) and self.vaisseau_x>0:
            self.vaisseau_x += -2


    # =====================================================
    # == UPDATE
    # =====================================================
    def update(self):
        """mise à jour des variables (30 fois par seconde)"""

        # deplacement du vaisseau
        self.vaisseau_deplacement()
        self.bullet_move()
        self.ship_shoot()


    # =====================================================
    # == DRAW
    # =====================================================
    def draw(self):
        """création et positionnement des objets (30 fois par seconde)"""

        # vide la fenetre
        pyxel.cls(0)

        # vaisseau (carre 8x8)
        pyxel.rect(self.vaisseau_x, self.vaisseau_y, 8, 8, 7)

        # bullet 
        if self.bullet_x is not None :
            pyxel.rect(self.bullet_x, self.bullet_y, 2, 4, 7)

Jeu()