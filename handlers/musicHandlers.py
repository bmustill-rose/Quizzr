def toggleMusic(music, dirName, fName):
 if _isMusicPlaying(music):
  _stopMusic(music)
 else:
  _startMusic(music, dirName+"/"+fName)

def _fileExists(fName):
 from os import path
 if path.exists(fName):
  return True
 else:
  return False

def _stopMusic(music):
 music.stop()

def _startMusic(music, fName):
 if _fileExists(fName):
  try:
   music.load(fName)
   music.play()
  except:
   pass

def _isMusicPlaying(music):
 if music.get_busy():
  return True
 else:
  return False