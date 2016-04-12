import sys
import requests
from time import sleep
from gpiozero import LED

LOCK = LED(17)


def argsValid():
  return len(sys.argv) == 3

def unlockDoor():
  print("unlocking door")
  LOCK.off()
  sleep(1)

def lockDoor():
  print("locking door")
  LOCK.on()


if (argsValid() is False):
  print("bad command line args")
  sys.exit(1)
else:
  payload  = {'userId' : sys.argv[2]}
  response = requests.post(sys.argv[1], data = payload)
  
  if (response.status_code == 200):
    unlockDoor()
  
  lockDoor()
  sys.exit(0)
