def incramentScore(pygame, SCORING, sound, score):
 return _changeScore(pygame, SCORING, sound, score, score+1)

def decrementScore(pygame, SCORING, sound, score):
 return _changeScore(pygame, SCORING, sound, score, score-1)

def resetScore(pygame, scoring, sound):
 return _changeScore(pygame, scoring, sound, SCORING['MINIMUM_SCORE']+1, SCORING['STARTING_SCORE'])

def _shouldScoreBeChanged(scoring, score):
 if score + 1 > scoring['MAXIMUM_SCORE'] or score - 1 < scoring['MINIMUM_SCORE']:
  return True
 else:
  return False

def _acknowledgeChangedScore(pygame, sound, score):
 pygame.mixer.Sound.play(sound)
 pygame.display.set_caption("{} points Quizzr".format(score))

def _changeScore(pygame, SCORING, sound, score, newScore):
 if _shouldScoreBeChanged(SCORING, score):
  _acknowledgeChangedScore(pygame, sound, newScore)
  return newScore
 else:
  return score