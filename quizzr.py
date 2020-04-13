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
from factories import soundsFactory

score = config.SCORING['STARTING_SCORE']
clock = pygame.time.Clock()
pygame.mixer.init()
sounds = soundsFactory.createSounds(pygame.mixer, config.ASSETS['ASSET_DIRECTORY_NAME'], config.AUDIO_ASSETS)
pygame.display.init()
screen = pygame.display.set_mode((config.DIMENSIONS['WIDTH'], config.DIMENSIONS['HEIGHT']))
pygame.display.set_caption("{} points Quizzr".format(score))

active = True
while active:
 for event in pygame.event.get():
  if event.type == pygame.QUIT: active = False
  if event.type == pygame.KEYUP:
   if event.key == K_UP: score = scoreHandlers.incramentScore(pygame, config.SCORING, sounds['INCRAMENT_SCORE_SOUND'], score)
   elif event.key == K_DOWN: score = scoreHandlers.decrementScore(pygame, config.SCORING, sounds['DECREMENT_SCORE_SOUND'], score)
   elif event.key == K_r: score = scoreHandlers.resetScore(pygame, config.SCORING, sounds['RESET_SCORE_SOUND'])
   elif event.key == K_m: musicHandlers.toggleMusic(pygame.mixer.music, config.ASSETS['ASSET_DIRECTORY_NAME'], config.AUDIO_ASSETS['MUSIC'])
   elif event.key == K_q: active = False
 pygame.display.flip()
 clock.tick(40)

pygame.quit()