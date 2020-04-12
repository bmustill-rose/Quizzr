def createSounds(mixer, dictOfSounds):
 sounds = {}
 for sound in dictOfSounds:
  if fileExists(dictOfSounds[sound]):
   sounds[sound] = createSound(mixer, dictOfSounds[sound])
 return sounds

def __createSound(mixer, fName):
 return mixer.Sound(fName)

def __fileExists(fName):
 from os import path
 if path.exists(fName):
  return True
 else:
  return False