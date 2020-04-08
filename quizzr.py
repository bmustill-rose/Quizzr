import pygame
from pygame.locals import (
 K_UP,
 K_DOWN,
 K_r,
 K_m
)

import config
from handlers import scoreHandlers, musicHandlers

score = config.STARTING_SCORE
clock = pygame.time.Clock()
pygame.display.init()
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("{} points Quizzr".format(score))

active = True
while active:
 for event in pygame.event.get():
  if event.type == pygame.QUIT: active = False
  if event.type == pygame.KEYUP:
   if event.key == K_UP: score = scoreHandlers.incramentScore(config, score)
   elif event.key == K_DOWN: score = scoreHandlers.decrementScore(config, score)
   elif event.key == K_r: score = scoreHandlers.resetScore(config)
   elif event.key == K_m: musicHandlers.toggleMusic()
 pygame.display.flip()
 clock.tick(40)

pygame.quit()