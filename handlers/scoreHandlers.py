def incramentScore(pygame, SCORING, sound, score):
 return _changeScore(pygame, SCORING, sound, score, score+1, 'incrament')

def decrementScore(pygame, SCORING, sound, score):
 return _changeScore(pygame, SCORING, sound, score, score-1, 'decrement')

def resetScore(pygame, scoring, sound):
 return _changeScore(pygame, scoring, sound, scoring['MAXIMUM_SCORE']-1, scoring['STARTING_SCORE'], 'incrament')

def _shouldScoreBeChanged(scoring, score, direction):
 if direction == 'decrement' and score == scoring['MINIMUM_SCORE']:
  return False
 elif score == scoring['MAXIMUM_SCORE']:
  return False
 else:
  return True

def _acknowledgeChangedScore(pygame, sound, score):
 try:
  pygame.mixer.Sound.play(sound)
 except:
  pass
 pygame.display.set_caption("{} points Quizzr".format(score))

def _changeScore(pygame, SCORING, sound, score, newScore, direction):
 if _shouldScoreBeChanged(SCORING, score, direction):
  _acknowledgeChangedScore(pygame, sound, newScore)
  return newScore
 else:
  return score