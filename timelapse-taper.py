import pygame
import pygame.camera
from pygame.locals import *
import sys
from time import sleep
from datetime import datetime
import os

# full screen: size = (1440,900)
size = (640,480)

pygame.init()
pygame.camera.init()
screen = pygame.display.set_mode(size, pygame.RESIZABLE)

clist = pygame.camera.list_cameras()
if not clist:
    raise ValueError("Sorry, no cameras detected.")
cam = pygame.camera.Camera(clist[0], size)
cam.start()
snapshot = pygame.surface.Surface(size, 0, screen)

carryOn = True
clock=pygame.time.Clock()
GAME_FONT = pygame.font.SysFont("Arial", 24)

def getTimestamp():
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    return now.strftime("%Y-%m-%d_%H-%M-%S")

recording = False

path = 'capture/{0}'.format(getTimestamp())
os.makedirs(path)
os.chdir(path)

imgCount = 0
framesPerSecond = 1

try:
    while carryOn:
        imgCount = imgCount + 1
        ts = getTimestamp()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                print("quitting...")
                carryOn=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    print("quitting...")
                    carryOn=False
                if event.key==pygame.K_r:
                    recording = not recording
        
        # screen.fill((0,0,0))
        if cam.query_image():
            snapshot = cam.get_image(snapshot)
            screen.blit(snapshot, (0,0))
        timesurface = GAME_FONT.render(ts, False, (255, 255, 255))
        screen.blit(timesurface,(0,0))
        if recording:
            recordingsurface = GAME_FONT.render('recording', False, (255, 0, 0))
            screen.blit(recordingsurface,(240,0))
            pygame.image.save(screen, 'img-%s.jpg' % str(imgCount).zfill(6))
        pygame.display.flip()
        #Number of frames per secong e.g. 60
        clock.tick(framesPerSecond)
except:
    e = sys.exc_info()[1]
    print(e)
finally:
    pygame.quit()
    cam.stop()
