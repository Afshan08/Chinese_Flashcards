from tkinter import *
from buttons import Buttons
from chinese_word import RandomChineseWord
import json

BACKGROUND_COLOR = "#B1DDC6"


class FlashCard:
    def __init__(self, master, flip_limit=50):
        self.master = master
        self.canvas = Canvas(width=800, height=528, bg=BACKGROUND_COLOR)
        self.flash_card_front_image = PhotoImage(file="images/card_front.png")
        self.flash_card_back_image = PhotoImage(file="images/card_back.png")
        self.word_instance = RandomChineseWord(self.canvas)
        self.flip_count = 0  # Instance variable for current flip count
        self.flip_limit = flip_limit  # Flip count limit
        self.timer = None  # Variable to keep track of the timer

        self.button = Buttons(master)
        self.button.wrong_button(command=self.wrong_button)
        self.button.right_button(command=self.right_button)

    def flash_card_front(self):
        self.canvas.create_image(400, 263, image=self.flash_card_front_image)
        self.word_instance.question()
        self.canvas.config(highlightthickness=0)
        self.canvas.grid(column=1, row=2, columnspan=2)

    def flash_card_back(self):
        self.canvas.create_image(400, 263, image=self.flash_card_back_image)
        self.word_instance.answer()
        self.canvas.config(highlightthickness=0)
        self.canvas.grid(column=1, row=2, columnspan=2)

    def flip_card(self):
        if self.flip_count < self.flip_limit:
            self.flash_card_back()
            self.timer = self.master.after(3000, self.wrong_button)
        else:
            self.wrong_button()

    def wrong_button(self):
        if self.flip_count < self.flip_limit:
            if self.timer:
                self.master.after_cancel(self.timer)
            self.word_instance = RandomChineseWord(self.canvas)
            self.flash_card_front()
            self.timer = self.master.after(3000, self.flip_card)
            self.flip_count += 1

    def right_button(self):
        try:
            # Load the current list of learned words
            try:
                with open("learned_words.json", "r", encoding='utf-8') as learned_data:
                    learned_words = json.load(learned_data)
            except (FileNotFoundError, json.JSONDecodeError):
                # If the file doesn't exist or is corrupted, start with an empty list
                learned_words = []

            # Load the list of Mandarin words
            with open("mandarin.json", "r", encoding='utf-8') as mandarin_data:
                mandarin_words = json.load(mandarin_data)

            # The current word to move (assumed to be a dictionary with Simplified, Pinyin, and Meaning)
            current_word = self.word_instance.word

            # Check if the current word is in mandarin.json and not already in learned_words.json
            if current_word in mandarin_words and current_word not in learned_words:
                # Add the current word to learned_words.json
                learned_words.append(current_word)

                # Remove the word from mandarin.json
                mandarin_words.remove(current_word)

                # Write updated data back to mandarin.json
                with open("mandarin.json", "w", encoding='utf-8') as mandarin_data:
                    json.dump(mandarin_words, mandarin_data, indent=4)

                # Write updated data back to learned_words.json
                with open("learned_words.json", "w", encoding='utf-8') as learned_data:
                    json.dump(learned_words, learned_data, indent=4)

        except Exception as e:
            print(f"An error occurred: {e}")

        # Proceed to the next word if within the flip limit
        if self.flip_count < self.flip_limit:
            if self.timer:
                self.master.after_cancel(self.timer)
            self.word_instance = RandomChineseWord(self.canvas)
            self.flash_card_front()
            self.timer = self.master.after(3000, self.flip_card)
            self.flip_count += 1


    def start(self):
        self.wrong_button()

