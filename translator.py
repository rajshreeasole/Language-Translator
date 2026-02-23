from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
import tkinter.messagebox as msg
#from gtts import gTTS
import os

# Function to Read Text in Selected Language
#def read_text_in_language(language_name, text):
    #tts = gTTS(text, lang=language_name)
    #tts.save("temp.mp3")
   # os.system("start temp.mp3")

# Function to Translate Text
def translate_text():
    user_input = text_input.get(1.0, END).strip()
    source_lang = source_language.get()
    convert_lang = convert_language.get()
    code_lang = code_language.get()

    if user_input and source_lang != convert_lang:
        translator = Translator()
        translated_text = translator.translate(user_input, src=source_lang, dest=convert_lang)

        output_txt.delete(1.0, END)
        output_txt.insert(END, translated_text.text)
        read_text_in_language(code_lang, translated_text.text)
    else:
        output_txt.delete(1.0, END)
        msg.showerror("Translation Error", "Cannot translate text to the same language. Choose a different language.")

# Create Main Window
root = Tk()
root.title("Google Translator")
root.geometry("1400x1200")
root.config(bg="skyblue")

# Labels
Label(root, text="Language Translator", font=("Times New Roman", 27, "bold", "underline"), foreground="black", bg="skyblue").place(x=450, y=10)
Label(root, text="Enter Text", font=("Times New Roman", 20, "bold"), foreground="black", bg="skyblue").place(x=325, y=150)

# Text Input
text_input = Text(root, font=("Times New Roman", 20, "bold"), foreground="black")
text_input.place(x=200, y=220, height=150, width=400)

# Source Language Dropdown
Label(root, text="Source Language", font=("Times New Roman", 20, "bold"), foreground="black", bg="skyblue").place(x=270, y=400)
source_language = ttk.Combobox(root, font=("Times New Roman", 15, "bold"), foreground="black", values=list(LANGUAGES.values()))
source_language.place(x=270, y=450)
source_language.set("english")

# Convert Language Dropdown
Label(root, text="Convert Language", font=("Times New Roman", 20, "bold"), foreground="black", bg="skyblue").place(x=670, y=400)
convert_language = ttk.Combobox(root, font=("Times New Roman", 15, "bold"), foreground="black", values=list(LANGUAGES.values()))
convert_language.place(x=670, y=450)
convert_language.set("hindi")

# Code Language Dropdown
Label(root, text="Code Language", font=("Times New Roman", 20, "bold"), foreground="black", bg="skyblue").place(x=1000, y=400)
code_language = ttk.Combobox(root, font=("Times New Roman", 15, "bold"), foreground="black", values=list(LANGUAGES.keys()))
code_language.place(x=1000, y=450, width=100)
code_language.set("hi")

# Translated Text Output
Label(root, text="Translated Text", font=("Times New Roman", 20, "bold"), foreground="black", bg="skyblue").place(x=790, y=150)
output_txt = Text(root, font=("Times New Roman", 20, "bold"), foreground="black")
output_txt.place(x=700, y=220, height=150, width=400)

# Translate Button
Button(root, text="Translate", font=("Times New Roman", 20, "bold"), foreground="white", bg="green", command=translate_text).place(x=700, y=550)

# Clear Function
def clear_text():
    text_input.delete(1.0, END)
    output_txt.delete(1.0, END)

# Clear Button
Button(root, text="Clear", font=("Times New Roman", 20, "bold"), foreground="white", bg="red", command=clear_text).place(x=450, y=550, width=150)

# Exit Function
def exit_app():
    root.destroy()

# Exit Button
Button(root, text="Exit", font=("Times New Roman", 20, "bold"), foreground="white", bg="blue", command=exit_app).place(x=575, y=700, width=150)

# Run the Application
root.mainloop()
