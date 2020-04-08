import sys
import pygame

import config

score = config.STARTING_SCORE
clock = pygame.time.Clock()
pygame.display.init()
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("{} points Quizzr".format(score))

active = True
while active:
 for event in pygame.event.get():
  if event.type == pygame.QUIT: active = False
 pygame.display.flip()
 clock.tick(40)

pygame.quit()