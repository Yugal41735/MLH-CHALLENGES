from pygame import init, mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__ == '__main__':
    # musiconloop("D:\\CODING\\Learning\\Python\\testing\\water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()

    watersecs = 4
    exsecs = 4
    eyessecs = 3

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking Time. Enter 'drank' to stop the alarm.")
            musiconloop("D:\\CODING\\Learning\\Python\\testing\\water.mp3", "drank")
            init_water = time()
            log_now("Drank water at")
        
        if time() - init_eyes > eyessecs:
            print("Eyes relaxing Time. Enter 'doneeyes' to stop the alarm.")
            musiconloop("D:\\CODING\\Learning\\Python\\testing\\eyes.mp3", "doneeyes")
            init_eye = time()
            log_now("Eyes relaxed at")
        
        if time() - init_exercise > exsecs:
            print("Physical Exercise Time. Enter 'donephy' to stop the alarm.")
            musiconloop("D:\\CODING\\Learning\\Python\\testing\\physical.mp3", "donephy")
            init_exercise = time()
            log_now("Physical Exercise done at")