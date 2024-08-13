import mpmath
import tkinter as tk
import pygame
import time

# Set precision for Pi
mpmath.mp.dps = 1000
pi_digits = str(mpmath.mp.pi)[2:]  # Get the digits of Pi after the decimal point

# Mapping digits to musical notes
note_map = {
    '0': 'C4', 
    '1': 'D4', 
    '2': 'E4', 
    '3': 'F4', 
    '4': 'G4',
    '5': 'A4', 
    '6': 'B4', 
    '7': 'C5', 
    '8': 'D5', 
    '9': 'E5'
}

# Function to play a note
def play_note(note):
    pygame.mixer.music.load(f'sounds/{note}.mp3')  # Load the note mp3 file
    pygame.mixer.music.play()  # Play the note

# Function to highlight the digit and show the note
def highlight_digit(index):
    digit = pi_digits[index]
    note = note_map[digit]
    label.config(text=f"Digit: {digit}\nNote: {note}")
    play_note(note)
    canvas.itemconfig(digit_ids[index], fill='green')
    root.update()
    time.sleep(0.25)  # Delay to make the music pleasant
    canvas.itemconfig(digit_ids[index], fill='black')

# Initialize pygame for sound playback
pygame.mixer.init()

# Create the GUI window
root = tk.Tk()
root.title("Pi Musical Representation")

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Display the first few digits of Pi in the GUI
digit_ids = []
for i, digit in enumerate(pi_digits[:100]):  # Showing the first 100 digits as an example
    x = (i % 10) * 50 + 25
    y = (i // 10) * 50 + 25
    digit_id = canvas.create_text(x, y, text=digit, font=('Helvetica', 24), fill='black')
    digit_ids.append(digit_id)

label = tk.Label(root, text="", font=('Helvetica', 16))
label.pack()

# Play the music and highlight the digits
for i in range(len(pi_digits)):
    highlight_digit(i)

root.mainloop()