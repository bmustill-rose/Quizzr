def createSounds(mixer, dictOfSounds):
 sounds = {}
 for sound in dictOfSounds:
  if _fileExists(dictOfSounds[sound]):
   sounds[sound] = _createSound(mixer, dictOfSounds[sound])
 return sounds

def _fileExists(fName):
 from os import path
 if path.exists(fName):
  return True
 else:
  return False

def _createSound(mixer, fName):
 return mixer.Sound(fName)
