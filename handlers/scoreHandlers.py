def incramentScore(pygame, config, score):
 if score + 1 > config.MAXIMUM_SCORE: return score
 score = score + 1
 pygame.display.set_caption("{} points Quizzr".format(score))
 return score

def decrementScore(pygame, config, score):
 if score - 1 < config.MINIMUM_SCORE: return score
 score = score - 1
 pygame.display.set_caption("{} points Quizzr".format(score))
 return score

def resetScore(pygame, config):
 score = config.STARTING_SCORE
 pygame.display.set_caption("{} points Quizzr".format(score))
 return score