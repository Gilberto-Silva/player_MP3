from tkinter import *
import pygame
from tkinter import filedialog
root = Tk()
root.title('MP3 Player')
# root.iconbitmap('C:\Users\Gilberto-Silva\PycharmProjects\play_mp3\images')
root.geometry("500x300")

# Inicializa Pygame Mixer
pygame.mixer.init()

# Add song function
def add_song():
    song = filedialog.askopenfilename(inicialdir='audio/', title=('Chose a song'), filetype=('filename:'))

    # Strip out the directory info and .mp3 extension from the screen
    song = song.replace("C:/gui/audio/", "")
    song = song.replace(".mp3", "")

    # A song to listbox
    song_box.insert(END, song)


# Cria a Playlist Box
song_box = Listbox(root, bg="black", fg="green", width=60, selectbackground='gray', selectforeground='black')
song_box.pack(pady=20)

# Cria os Players Control Buttons
back_btn_img = PhotoImage(file='images/back.png')
forward_btn_img = PhotoImage(file='images/forward.png')
play_btn_img = PhotoImage(file='images/play.png')
pause_btn_img = PhotoImage(file='images/pause.png')
stop_btn_img = PhotoImage(file='images/stop.png')

# Cria o Player Control Frame
controls_frame = Frame(root)
controls_frame.pack()

# Cria o Player Control Button
back_btn = Button(controls_frame, image=back_btn_img, borderwidth=0)
forward_btn = Button(controls_frame, image=forward_btn_img, borderwidth=0)
play_btn = Button(controls_frame, image=play_btn_img, borderwidth=0)
pause_btn = Button(controls_frame, image=pause_btn_img, borderwidth=0)
stop_btn = Button(controls_frame, image=stop_btn_img, borderwidth=0)

back_btn.grid(row=0, column=0, padx=10)
forward_btn.grid(row=0, column=1, padx=10)
play_btn.grid(row=0, column=2, padx=10)
pause_btn.grid(row=0, column=3, padx=10)
stop_btn.grid(row=0, column=4, padx=10)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add Add Song Menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(Label="ADD one Song to Playlist", command=add_song)




root.mainloop()
