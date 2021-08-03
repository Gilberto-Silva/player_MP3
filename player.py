from tkinter import *
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

image_path  = 'C:/Users/Gilberto-Silva/pictures/player/buttons/'
image_path1 = 'C:/Users/Gilberto-Silva/pictures/player/buttons1/'

root = Tk()
root.title('DJ_Marcos - MP3 Player')
# root.iconbitmap('python_94570.ico')
# root.iconbitmap('dj.ico')
root.iconbitmap('dj_black.ico')
root.geometry('700x500')

# Initialize Pygame Mixer
pygame.mixer.init()

#============================================================================

# Grab Song Lenght Time Info
def play_time():

    # Grab current song elapsed Time
    current_time = pygame.mixer.music.get_pos() / 1000

    # Convert Time to format
    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

    # Get currently playing song
    current_song = song_box.curselection()
    # Grab song title to playlist
    song = song_box.get(current_song)
    # Add directory structure and mp3 to song title
    song = f'C:/Users/Gilberto-Silva/Music/{song}.mp'
    # Load song length whit Mutagen
    song_mut = MP3(song)
    # Get song length
    global song_length
    song_length = song_mut.info.lenght
    # Convert to time format
    converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))

    # Output time to status bar
    status_bar.config(text=f'Time Elapsed: {converted_current_time} of {converted_song_length}  ')

    # Update time
    status_bar.after(1000, play_time)

# Add Song Function
def add_song():
    song = filedialog.askopenfilename(initialdir='audio', title="Chose a song", filetypes=(("mp3 Files", "*.mp3"),))
    
    #strip out the directory info and .mp3 extension from the song name
    song = song.replace("C:/Users/Gilberto-Silva/Music/", "")
    song = song.replace(".mp3", "")

    # Add song to listbox
    song_box.insert(END, song)

# Add many songs to playlist
def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='audio', title="Chose a song", filetypes=(("mp3 Files", "*.mp3"),))

    # Loop thru song list and replace directory info and mp3
    for song in songs:
        song = song.replace("C:/Users/Gilberto-Silva/Music/", "")
        song = song.replace(".mp3", "")
        # Insert into playlist
        song_box.insert(END, song)

# Play selected song
def play():
    song = song_box.get(ACTIVE)
    song = f'C:/Users/Gilberto-Silva/Music/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Call the play_time function to get song lenght
    play_time()

# Stop playing current song
def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

# Play the Next Song in the playlist
def next_song():
    # Get the current song tuple number
    next_one = song_box.curselection()
    # Add one the current song number
    next_one = next_one[0]+1
    # Grab song title from playlist
    song = song_box.get(next_one)
    # Add directory structure and mp3 to song title
    song = f'C:/Users/Gilberto-Silva/Music/{song}.mp3'
    # Load and play song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Clear active bar in playlist listbox
    song_box.selection_clear(0, END)
    
    # Activate new song bar
    song_box.activate(next_one)

    # Set active bar to next song
    song_box.selection_set(next_one, last=None)

def previous_song():
    # Get the current song tuple number
    next_one = song_box.curselection()
    # Sub one the current song number
    next_one = next_one[0]-1
    # Grab song title from playlist
    song = song_box.get(next_one)
    # Add directory structure and mp3 to song title
    song = f'C:/Users/Gilberto-Silva/Music/{song}.mp3'
    # Load and play song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Clear active bar in playlist listbox
    song_box.selection_clear(0, END)
    
    # Activate new song bar
    song_box.activate(next_one)

    # Set active bar to next song
    song_box.selection_set(next_one, last=None)

# Delete a song
def delete_song():
    # pygame.mixer.music.stop() # Stop the current song
    song_box.delete(ANCHOR)     # Delete selected song from playlist

# Delete all songs
def delete_all_songs():
    pygame.mixer.music.stop() # Stop the current song
    song_box.delete(0, END)   # Delete all songs from playlist

# Create Global pause variable
global paused
paused = FALSE

# Pause and Unpause the current song
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        # Unpause
        pygame.mixer.music.unpause()
        paused = FALSE
    else:
        # Pause
        pygame.mixer.music.pause()
        paused = TRUE    

# Create a slider function
def slide(x):
    slider_label.config(text=my_slider.get())

#============================================================================

# Create Playlist Box
song_box = Listbox(root, bg="black", fg="green", width=60, selectbackground="gray", selectforeground="black")
song_box.pack(pady=20)

# Define Player Control Buttons Images
back_btn_img    = PhotoImage(file=image_path1 + 'back.png')
forward_btn_img = PhotoImage(file=image_path1 + 'forward.png')
play_btn_img    = PhotoImage(file=image_path1 + 'play.png')
pause_btn_img   = PhotoImage(file=image_path1 + 'pause.png')
stop_btn_img    = PhotoImage(file=image_path1 + 'stop.png')

# Create player Control Frame
controls_frame = Frame(root)
controls_frame.pack()

# Create Player Control Buttons
back_button    = Button(controls_frame, image=back_btn_img, borderwidth=0, command=previous_song)
forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=0, command=next_song)
play_button    = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button   = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
stop_button    = Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add Add Song Menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song To Playlist", command=add_song)

# Add many songs to playlist
add_song_menu.add_command(label="Add Many Songs To Playlist", command=add_many_songs)

# Create Delete song menu
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete A Song From Playlist", command=delete_song)
remove_song_menu.add_command(label="Delete All Songs From Playlist", command=delete_all_songs)

# Create Status Bar
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

# Create music position slider
my_slider = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)
my_slider.pack(pady=30)

# Create Temporary Slider Label
slider_label = Label(root, text="0")
slider_label.pack(pady=10)

root.mainloop()