import pygame
import constants


class Player(): 
  def __init__(self, x, y, animations):
    
    self.flip = False
    self.animations = animations

    #Imagen de la animación que se esta mostrando
    self.frame_index = 0
    self.update_time = pygame.time.get_ticks()
    self.image = animations[self.frame_index]
    self.shape = pygame.Rect(0, 0, constants.WIDTH_PLAYER, constants.HEIGHT_PLAYER)
    self.shape.center = (x, y)

  def move_player(self, delta_x, delta_y):
    if delta_x < 0: 
      self.flip = True
    if delta_x > 0 :
      self.flip = False

    self.shape.x = self.shape.x + delta_x
    self.shape.y = self.shape.y + delta_y


  def draw(self, screen):
    imagen_flip = pygame.transform.flip(self.image, self.flip, False)
    screen.blit(imagen_flip, self.shape)


  def update(self): 
    cooldown_animation = 100
    self.image = self.animations[self.frame_index]
    if pygame.time.get_ticks() - self.update_time >= cooldown_animation:
      self.frame_index = self.frame_index + 1
      self.update_time = pygame.time.get_ticks()
    
    if self.frame_index >= len(self.animations):
      self.frame_index = 0
