def incramentScore(pygame, config, sound, score):
 if score + 1 > config.MAXIMUM_SCORE: return score
 score = score + 1
 pygame.mixer.Sound.play(sound)
 pygame.display.set_caption("{} points Quizzr".format(score))
 return score

def decrementScore(pygame, config, sound, score):
 if score - 1 < config.MINIMUM_SCORE: return score
 score = score - 1
 pygame.mixer.Sound.play(sound)
 pygame.display.set_caption("{} points Quizzr".format(score))
 return score

def resetScore(pygame, config, sound):
 score = config.STARTING_SCORE
 pygame.mixer.Sound.play(sound)
 pygame.display.set_caption("{} points Quizzr".format(score))
 return score