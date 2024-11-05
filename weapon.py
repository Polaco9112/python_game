import pygame

class Weapon():
  def __init__(self, image):
    self.image_original = image
    self.angle = 0
    self.image = pygame.transform.rotate(self.image_original, self.angle)
    self.shape = self.image.get_rect()

  def update(self, player):
    self.shape.center = player.shape.center
    self.shape.x = self.shape.x + player.shape.width / 2

  def draw_weapon(self, screen): 
    screen.blit(self.image, self.shape)