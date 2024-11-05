import pygame, sys
import constants
from player import Player

pygame.init()

gameScreen = pygame.display.set_mode((constants.WIDTH_SCREEN, constants.HEIGHT_SCREEN))
gameCaption = pygame.display.set_caption('Juego #1')

def img_scale(image, scale):
  w = image.get_width()
  h = image.get_height()
  new_image = pygame.transform.scale(image, (w * scale, h * scale))
  return new_image

animations = []
for i in range(7):
  img = pygame.image.load(f"assets//images//characters//player//Player_{i}.png")
  img = img_scale(img, constants.PLAYER_SCALE)
  animations.append(img)


jugador = Player(50, 50, animations)

width = 1200
height = 800


#Se definen las variables de movimiento 
move_up = False
move_down = False
move_left = False
move_rigth = False

clock = pygame.time.Clock()


while True:

  gameScreen.fill(constants.BG_COLOR)

  clock.tick(constants.FPS)

 
  #Calcular el movimiento del Player
  delta_x = 0
  delta_y = 0

  if move_rigth == True : 
    delta_x = constants.SPEED
  
  if move_left == True: 
    delta_x = -constants.SPEED
  
  if move_up == True:
    delta_y = -constants.SPEED

  if move_down == True:
    delta_y = constants.SPEED

  #Llamamos a la funcion que mueve el personaje 
  jugador.move_player(delta_x, delta_y)

  jugador.update()


  jugador.draw(gameScreen)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_a:
        move_left = True

      if event.key == pygame.K_d:
       move_rigth = True
      
      if event.key == pygame.K_w:
        move_up = True
      
      if event.key == pygame.K_s:
        move_down = True

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_a:
        move_left = False

      if event.key == pygame.K_d:
       move_rigth = False
      
      if event.key == pygame.K_w:
        move_up = False
      
      if event.key == pygame.K_s:
        move_down = False




  pygame.display.update()


pygame.quit()