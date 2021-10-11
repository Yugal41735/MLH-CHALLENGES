from pygame import mixer

from datetime import date, datetime, timedelta

def getdate():
    import datetime
    return datetime.datetime.now()

present_time = datetime.now()  
print(present_time)
  
#time formatting
'{:%H:%M:%S}'.format( present_time )    

updated_time = present_time + timedelta(hours=8)

print(updated_time)


print("-----------------------HEALTHY PROGRAMMER----------------------------------")

new_time = datetime.now()
print(new_time)
while (present_time != updated_time):
    while True:
        new_time = datetime.now()
        if new_time == present_time + timedelta(seconds=2):
            print("Hello")
            break
        
    if (new_time == present_time + timedelta(seconds=2)):
        print("hello world")

        mixer.init()
        
        mixer.music.load("D:\\CODING\\Learning\\Python\\testing\\water.mp3")
        
        mixer.music.set_volume(0.7)
        
        mixer.music.play()

        print("If you drank the water enter 'Drank' :) ")

        while True:
            a = input()
        
            if a == "Drank" :
                mixer.music.stop()
                x = getdate()
                print(x)

    if (present_time == present_time + timedelta(seconds=3)):

        mixer.init()
        
        mixer.music.load("D:\\CODING\\Learning\\Python\\testing\\eyes.mp3")
        
        mixer.music.set_volume(0.7)
        
        mixer.music.play()

        print("If you drank the water enter 'Eydone' :) ")
        b = input()
        
        if b == "Eydone" :
            mixer.music.stop()
            x = getdate()
            print(x)
    
    if (present_time == present_time + timedelta(seconds=4)):

        mixer.init()
        
        mixer.music.load("D:\\CODING\\Learning\\Python\\testing\\physical.mp3")
        
        mixer.music.set_volume(0.7)
        
        mixer.music.play()

        print("If you drank the water enter 'Exdone' :) ")
        c = input()
        
        if c == "Exdone" :
            mixer.music.stop()
            x = getdate()
            print(x)
    
    present_time = datetime.now()