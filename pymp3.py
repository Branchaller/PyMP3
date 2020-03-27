# MP3 Player by Branchaller

import pygame
from tkinter import *
from tkinter import filedialog

pygame.mixer.pre_init(44100, -16, 2, 2048) 
root = Tk()

audio_file_name = ''
def open_masker():
    global audio_file_name
    audio_file_name = filedialog.askopenfilename(filetypes=(("Audio Files", ".mp3"),   ("All Files", "*.*")))
def masker_screen():  
    global m_screen, audio_file_name

    m_screen = Toplevel(root)
    m_screen.geometry('50x50')
    m_screen.transient(root) 
    m_label = Label(m_screen, text = "Playing...")
    m_label.pack(anchor = CENTER)

    if audio_file_name: 
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file_name)
        pygame.mixer.music.play(+1)
               
root.title('PyMP3')

b1 = Button(root, text = 'Open file',command = open_masker)
b1.pack(anchor=CENTER)

Button(root, text = 'Play!', command = masker_screen).pack(anchor = E)

root.mainloop()
