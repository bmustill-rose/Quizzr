import pygame
from pygame.locals import (
 K_UP,
 K_DOWN,
 K_r,
 K_m,
 K_q
)

import config
from handlers import scoreHandlers, musicHandlers

score = config.SCORING['STARTING_SCORE']
clock = pygame.time.Clock()
pygame.mixer.init()
pygame.display.init()
screen = pygame.display.set_mode((config.DIMENSIONS['WIDTH'], config.DIMENSIONS['HEIGHT']))
pygame.display.set_caption("{} points Quizzr".format(score))

active = True
while active:
 for event in pygame.event.get():
  if event.type == pygame.QUIT: active = False
  if event.type == pygame.KEYUP:
   if event.key == K_UP: score = scoreHandlers.incramentScore(pygame, config, INCRAMENT_SCORE, score)
   elif event.key == K_DOWN: score = scoreHandlers.decrementScore(pygame, config, DECREMENT_SCORE, score)
   elif event.key == K_r: score = scoreHandlers.resetScore(pygame, config, RESET_SCORE)
   elif event.key == K_m: musicHandlers.toggleMusic(pygame)
   elif event.key == K_q: active = False
 pygame.display.flip()
 clock.tick(40)

pygame.quit()