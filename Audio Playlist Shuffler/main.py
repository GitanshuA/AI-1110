import numpy as np
from tkinter import *
from PIL import Image, ImageTk
import pygame

is_playing = False
current = 0
counter = 0
arr = [i+1 for i in range(20)]
mylist = []
np.random.shuffle(arr)
mylist.extend(arr)
pygame.mixer.init()

inter = Tk()
inter.title('Playlist Shuffler')
inter.geometry("420x300")
play_image = ImageTk.PhotoImage(Image.open("icons/play.png").resize((70,70)))
pause_image = ImageTk.PhotoImage(Image.open("icons/pause.png").resize((70,70)))
next_image = ImageTk.PhotoImage(Image.open("icons/forward.png").resize((70,70)))
prev_image = ImageTk.PhotoImage(Image.open("icons/rewind.png").resize((70,70)))

label = Label(
    text="Click Button to Play",
    font=("Arial", 13),
    fg="white",
    bg="black",
    width=60,
    height=8
)
label.pack()


def play_pause():
    global counter, is_playing
    if counter == 0:
        counter = counter+1
        pygame.mixer.music.load('audio_plist/'+str(mylist[current])+'.mp3')
        pygame.mixer.music.play()
        is_playing = True
        play_pause_btn.config(image=pause_image)
        play_pause_btn.image = pause_image
        label.config(text="Playing Song "+str(mylist[current]))
    else:
        if not is_playing:
            pygame.mixer.music.unpause()
            is_playing = True
            play_pause_btn.config(image=pause_image)
            play_pause_btn.image = pause_image
        else:
            pygame.mixer.music.pause()
            is_playing = False
            play_pause_btn.config(image=play_image)
            play_pause_btn.image = play_image

def play_next():
    global counter, current, arr, is_playing
    if counter%20==0:
        np.random.shuffle(arr)
        mylist.extend(arr)
    counter = counter+1
    current = current+1
    pygame.mixer.music.load('audio_plist/' + str(mylist[current]) + '.mp3')
    pygame.mixer.music.play()
    is_playing = True
    play_pause_btn.config(image=pause_image)
    play_pause_btn.image = pause_image
    label.config(text="Playing Song " + str(mylist[current]))
def prev():
    global current, is_playing
    if current >= 1:
        current = current-1
        pygame.mixer.music.load('audio_plist/' + str(mylist[current]) + '.mp3')
        pygame.mixer.music.play()
        is_playing = True
        play_pause_btn.config(image=pause_image)
        play_pause_btn.image = pause_image
        label.config(text="Playing Song " + str(mylist[current]))


control_frame = Frame(inter)
control_frame.pack()

play_pause_btn = Button(control_frame, image=play_image, borderwidth=0, command=play_pause)
next_btn = Button(control_frame, image=next_image, borderwidth=0, command=play_next)
prev_btn = Button(control_frame, image=prev_image, borderwidth=0, command=prev)

prev_btn.grid(row=0, column=0, padx=7, pady=10)
play_pause_btn.grid(row=0, column=1, padx=7, pady=10)
next_btn.grid(row=0, column=2, padx=7, pady=10)
inter.mainloop()




