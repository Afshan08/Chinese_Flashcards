from tkinter import *
from flash_cards import FlashCard

BACKGROUND_COLOR = "#B1DDC6"
FLIP_COUNT = 0
FLIP_COUNTs = 50

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flash_cards = FlashCard(window)
# Initially show the front of the first card and start the flipping process
flash_cards.flash_card_front()
window.after(3000, flash_cards.flip_card)
window.mainloop()
