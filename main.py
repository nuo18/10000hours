import customtkinter
import os

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")

        self.word_label = customtkinter.CTkLabel(self, text="Enter a word:")
        self.word_label.pack(pady=10)

        self.word_entry = customtkinter.CTkEntry(self)
        self.word_entry.pack()

        self.create_button = customtkinter.CTkButton(self, text="Create Button", command=self.create_word_button)
        self.create_button.pack(pady=10)

        self.load_buttons()

    def create_word_button(self):
        word = self.word_entry.get()
        if word:
            word_button = customtkinter.CTkButton(self, text=word, command=lambda: self.button_click(word))
            word_button.pack(pady=10)
            self.save_button(word)

    def button_click(self, word):
        print(f"Button '{word}' clicked!")

    def save_button(self, word):
        with open("button_data.txt", "a") as f:
            f.write(word + "\n")

    def load_buttons(self):
        if os.path.exists("button_data.txt"):
            with open("button_data.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    word = line.strip()
                    word_button = customtkinter.CTkButton(self, text=word, command=lambda w=word: self.button_click(w))
                    word_button.pack(pady=10)


app = App()
app.mainloop()
