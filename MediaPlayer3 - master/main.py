from PIL import Image
from tinytag import TinyTag
import tkinter
import customtkinter
import os
import pygame
import time
import easygui
customtkinter.set_appearance_mode("system") #System color 
customtkinter.set_default_color_theme("dark-blue") #Theme color green,blue,dark-blue

ft = False
ValueMusic = False
ValueInfinit = False

minute = 0

app = customtkinter.CTk()
app.geometry("300x255+100+100")
app.title('Mp3')
app.resizable(width=False,height=False)
nameSong = ''

time_start = time.time()
second = 0

pygame.mixer.init()

IMAGE_PATH_PLAY = 'img/play.png'
IMAGE_PATH_LEFT = 'img/play_left.png'
IMAGE_PATH_RIGHT = 'img/play_right.png'
IMAGE_PATH_LOGO = 'img/Lg.png'

image_play = customtkinter.CTkImage(light_image=Image.open(os.path.join(IMAGE_PATH_PLAY)))
image_right = customtkinter.CTkImage(light_image=Image.open(os.path.join(IMAGE_PATH_LEFT)))
image_left = customtkinter.CTkImage(light_image=Image.open(os.path.join(IMAGE_PATH_RIGHT)))

image_logo = customtkinter.CTkImage(light_image=Image.open(os.path.join(IMAGE_PATH_LOGO)), size=(100 , 100))

def OpenFinder():
    global nameSong,InfoMusic
    nameSong = easygui.fileopenbox(filetypes=["*.mp3","*.wav"])
    print(nameSong)
    InfoMusic = TinyTag.get(nameSong)
    pygame.mixer.music.load(nameSong)
    LabelName.configure(text=f'{InfoMusic.title} - {InfoMusic.artist}')
    sc.configure(to=int(InfoMusic.duration), number_of_steps=int(InfoMusic.duration))
    app.title(InfoMusic.title)

    button.configure(state=customtkinter.NORMAL)
    button_left.configure(state=customtkinter.NORMAL)
    button_right.configure(state=customtkinter.NORMAL)

    sc.configure(state=customtkinter.NORMAL)
def PlayMusic():
    global ft,p,ValueMusic
    if ft == False:
        start()
        if ValueMusic:
            pygame.mixer.music.unpause()
        else:
            infinity_loop()
            ValueMusic = True
        IMAGE_PATH_PLAY = 'img/pause.png'
        image_play.configure(light_image=Image.open(os.path.join(IMAGE_PATH_PLAY)))
        ft = True
        print('PlayMusic')
    elif ft == True:
        stop()
        pygame.mixer.music.pause()
        IMAGE_PATH_PLAY = 'img/play.png'
        image_play.configure(light_image=Image.open(os.path.join(IMAGE_PATH_PLAY)))
        ft = False 
        print('PauseMusic')
def ArrowLeft():
    sc.set(second - 5)
def ArrowRight():
    sc.set(second + 5)

def MusicStop():
    global ft,p,ValueMusic,ValueInfinit
    stop()
    pygame.mixer.music.pause()
    IMAGE_PATH_PLAY = 'img/play.png'
    image_play.configure(light_image=Image.open(os.path.join(IMAGE_PATH_PLAY)))
    ft = False 
    ValueInfinit = False
    ValueInfinit = False
    sc.set(0)

def infinity_loop():
    global second,ValueMusic,ValueInfinit
    LabelTime.configure(text=f'{int(sc.get())}')
    if ValueInfinit:
        if int(sc.get()) >= int(InfoMusic.duration) - 3:
            MusicStop()
        else:
            second = int(sc.get())
            print(second)
            sc.set(second + 1)
            pygame.mixer.music.play(-1,sc.get())
    else:
        print('stop')
    app.after(1000, infinity_loop)

def start():
    global ValueInfinit
    ValueInfinit = True
def stop():
    global ValueInfinit
    ValueInfinit = False

button = customtkinter.CTkButton(master=app, width=50, height = 45, text="", image=image_play, command=PlayMusic, state=customtkinter.DISABLED)
button_left = customtkinter.CTkButton(master=app, width=50, height = 45, text="", image=image_left, command=ArrowLeft, state=customtkinter.DISABLED)
button_right = customtkinter.CTkButton(master=app, width=50, height = 45, text="", image=image_right, command=ArrowRight, state=customtkinter.DISABLED)
button_open = customtkinter.CTkButton(master=app,width=50, height = 25,text='Open',text_color='#000' , command=OpenFinder)

LabelLogo = customtkinter.CTkLabel(master=app, width=100, height = 100,text="", image=image_logo)
LabelName = customtkinter.CTkLabel(master=app, text=f'')

sc = customtkinter.CTkSlider(master=app,width=250, from_=0, to=1, number_of_steps=1,state=customtkinter.DISABLED)
sc.set(0)

LabelTime = customtkinter.CTkLabel(master=app,height = 4,text_color='#808080', text=f'{sc.get()}')
#Place
#Button
button.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)
button_left.place(relx=0.3, rely=0.85, anchor=tkinter.CENTER)
button_right.place(relx=0.7, rely=0.85, anchor=tkinter.CENTER)
button_open.place(relx=0.9, rely=0.1, anchor=tkinter.CENTER)
#Sc
sc.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
#Label
LabelLogo.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
LabelName.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
LabelTime.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)

app.mainloop()