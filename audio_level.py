#download the sounddevice and playsound library
import sounddevice as sd
import random
import numpy as np
import random as rad
import os
from playsound import playsound

loops = 0
silence_counter = 0
sound_counter = 0

os.system('clear')

def reportFiller(indata, outdata, frames, time):
    global loops
    global silence_counter
    global sound_counter
    loops = loops+1
    volume_norm = np.linalg.norm(indata)*10
    #only play this when the last 2.5 seconds were silent
    #one second is around 150 loops
    
    if(volume_norm<5):
        silence_counter +=1
    if(volume_norm>6):
        silence_counter = 0
    if(silence_counter == 350):
        #play sound
        silence_counter = 300
        numm = rad.randint(1,6)
        os.system('clear')
        print("---------------------Filling Report Pause----------------------")
        playsound("6_report.mp3")
    print("|"*int(volume_norm))

def examProctor(indata, outdata, frames, time):
    global loops
    global silence_counter
    global sound_counter
    loops = loops+1
    volume_norm = np.linalg.norm(indata)*10
    #only play this when the last 2.5 seconds were silent
    #one second is around 150 loops
    
    if(volume_norm>5):
        sound_counter +=1
    if(volume_norm<2):
        sound_counter = 0
    if(sound_counter == 3):
        #play sound
        sound_counter = 0
        os.system("clear")
        print("---------------------Exam Proctor is Mad----------------------")
        numm = rad.randint(1,2)
        playsound(str(numm)+"_exam.mp3")
    print("|"*int(volume_norm))

def librarian(indata, outdata, frames, time):
    global loops
    global silence_counter
    global sound_counter
    loops = loops+1
    volume_norm = np.linalg.norm(indata)*10
    #only play this when the last 2.5 seconds were silent
    #one second is around 150 loops
    
    if(volume_norm>5):
        sound_counter +=1
    if(sound_counter == 200):
        #play sound
        sound_counter = 0
        os.system("clear")
        print("---------------------Librarian is Mad----------------------")
        numm = rad.randint(1,2)
        playsound(str(numm)+"_librarian.mp3")
    print("|"*int(volume_norm))

def defKid(indata, outdata, frames, time):
    global loops
    global silence_counter
    global sound_counter
    loops = loops+1
    volume_norm = np.linalg.norm(indata)*10
    #only play this when the last 2.5 seconds were silent
    #one second is around 150 loops
    
    if(volume_norm>5):
        sound_counter +=1
    if(volume_norm<2):
        sound_counter = 0
    if(sound_counter == 20):
        #play sound
        sound_counter = 10
        os.system("clear")
        print("---------------------Kid is being unreasonable----------------------")
        numm = rad.randint(1,4)
        playsound(str(numm)+"_kid.mp3")
    print("|"*int(volume_norm))

print("Choose Mode: \n 1. Report Filler | 2. Librarian | 3. Defensive Five Year Old | 4. Examination Proctor")
x = int(input())
if(x==1):
    with sd.InputStream(callback=reportFiller):
        sd.sleep(100000)
elif(x==4):
    with sd.InputStream(callback=examProctor):
        sd.sleep(100000)
elif(x==2):
    with sd.InputStream(callback=librarian):
        sd.sleep(100000)
elif(x==3):
    with sd.InputStream(callback=defKid):
        sd.sleep(100000)
