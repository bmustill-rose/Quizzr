def createSounds(mixer, directory, dictOfSounds):
 sounds = {}
 for sound in dictOfSounds:
  if _fileExists(directory+"/"+dictOfSounds[sound]):
   sounds[sound] = _createSound(mixer, directory+"/"+dictOfSounds[sound])
  else:
   sounds[sound] = None
 return sounds

def _fileExists(fName):
 from os import path
 if path.exists(fName):
  return True
 else:
  return False

def _createSound(mixer, fName):
 return mixer.Sound(fName)
