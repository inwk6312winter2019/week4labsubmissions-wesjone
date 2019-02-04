import os
import time
def run():
  d = input('name of directory')
  flist = []
  for x,y,z in os.walk(directory):
    if len(z)>0:
      flist.extend(z)
  print(directory)
  for x in flist:
    print(x)
    time.sleep(1)
run()
