import random
import json


class RandomChineseWord:
    def __init__(self, canvas):
        self.canvas = canvas
        self.result = self.pick_random_word()
        self.hanzi = self.result["Simplified"]
        self.pinyin = self.result['Pinyin']
        self.meaning = self.result['Meaning']


        print(f"This is hanzi and the meaning: {self.hanzi, self.meaning}")

    def pick_random_word(self):

        try:
            with open("mandarin.json", encoding="utf-8") as datafile:

                data = json.load(datafile)
                self.word = random.choice(data)
                hanzi = self.word['Simplified']
                pinyin = self.word["Pinyin"]
                meaning = self.word["Meaning"]
                print(self.word)
                return self.word
        except FileNotFoundError:
            print("The file mandarin.json was not found.")
            return {"Hanzi": "汉字", "Pinyin": "hànzì", "Meaning": "Chinese character"}
        except json.JSONDecodeError:
            print("Error decoding JSON from the file.")
            return {"Hanzi": "汉字", "Pinyin": "hànzì", "Meaning": "Chinese character"}
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"Hanzi": "汉字", "Pinyin": "hànzì", "Meaning": "Chinese character"}

    def question(self):
        self.canvas.create_text(400, 150, text="Chinese", font=("Arial", 30, "bold"), fill='black')
        self.canvas.create_text(400, 263, text=self.hanzi, font=("Arial", 60, "bold"), fill='black')
        self.canvas.create_text(400, 400, text=self.pinyin, font=("Arial", 60, "normal"), fill='black')

    def answer(self):
        self.canvas.create_text(400, 150, text="English", font=("Arial", 30, "bold"), fill='white')
        self.canvas.create_text(400, 263, text=self.meaning, font=("Arial", 21, "normal"), fill='white')
