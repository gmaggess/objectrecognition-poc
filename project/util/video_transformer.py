import os, errno
from os.path import basename
import cv2

def create_directory(directory):
  if not os.path.exists(directory):
    try:
      os.makedirs(directory)
    except OSError as e:
      if e.errno != errno.EEXIST:
        raise

def get_filename(path):
  filename = os.path.splitext(path)[0]
  return basename(filename)

def video_to_image(path):
  vidcap = cv2.VideoCapture(path)
  success,image = vidcap.read()
  count = 0
  total = 1
  success = True
  clazz = get_filename(path)
  directory = 'images/' + clazz
  create_directory(directory)
  while success:
    success,image = vidcap.read()
    if (divmod(count,10)[1] == 0):
      cv2.imwrite(directory+"/"+str(clazz)+"_"+str(total)+".jpg", image)     # save frame as JPEG file
      print('Read frame '+ str(total)+': '+ str(success))
      total += 1
    count += 1

video_to_image('videos/newton.mp4')