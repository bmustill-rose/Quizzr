import sys
import pygame

import config

pygame.display.init()

screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
active = True

while active:
 for event in pygame.event.get():
  if event.type == pygame.QUIT: active = False
 pygame.display.flip()

pygame.quit()