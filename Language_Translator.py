import tkinter as tk
from tkinter import *
from tkinter import ttk
from googletrans import LANGUAGES
from deep_translator import GoogleTranslator

root = Tk()
root.geometry('1080x400')
root.resizable(0, 0)
root.config(bg='ghost white')

root.title("Language Translator")

Label(root, text="LANGUAGE TRANSLATOR", font="arial 20 bold", bg='white smoke').pack()

Label(root, text="!! Language bridges human connection !!", font='arial 15 bold', bg='white smoke', width='50').pack(side='bottom')

Label(root, text="Enter Text", font='arial 13 bold', bg='white smoke').place(x=200, y=60)
Input_text = Text(root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
Input_text.place(x=30, y=100)

Label(root, text="Output", font='arial 13 bold', bg='white smoke').place(x=780, y=60)
Output_text = Text(root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
Output_text.place(x=600, y=100)

language = list(LANGUAGES.values())
src_lang = ttk.Combobox(root, values=language, width=22)
src_lang.place(x=20, y=60)
src_lang.set('choose input language')

dest_lang = ttk.Combobox(root, values=language, width=22)
dest_lang.place(x=890, y=60)
dest_lang.set('choose output language')

def Translate():
    src_language = src_lang.get()
    dest_language = dest_lang.get()

    # Find the language code by matching the language name with LANGUAGES
    src_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(src_language)]
    dest_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(dest_language)]

    translator = GoogleTranslator(source=src_code, target=dest_code)
    translated = translator.translate(Input_text.get(1.0, END))

    Output_text.delete(1.0, END)
    Output_text.insert(END, translated)

trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5, command=Translate, bg='royal blue1', activebackground='sky blue')
trans_btn.place(x=490, y=180)

root.mainloop()
