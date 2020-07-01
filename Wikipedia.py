from tkinter import *
from tkinter import scrolledtext
import wikipedia

root = Tk()
root.iconbitmap('c:/wikipedia.ico')
root.title('Wikipedia')
root.resizable(False, False)

languages = [
    "English",
    "Hindi",
    "Spanish",
    "Russian",
    "Bengali",
    "Portugese",
    "German",
    "French",
    "Japanese",
    "Urdu",
    "Korean",
    "Telugu",
    "Tamil",
    "Vietnamese",
    "Turkish"
]
dict = {"English": 'en',
        "Hindi": 'hi',
        "Spanish": 'es',
        "Russian": 'ru',
        "Bengali": '',
        "Portugese": 'pt',
        "German": 'de',
        "French": 'fr',
        "Japanese": 'ja',
        "Urdu": 'ur',
        "Korean": 'ko',
        "Telugu": 'te',
        "Tamil": 'ta',
        "Vietnamese": 'vi',
        "Turkish": 'tr'
        }

def search():
    global textbox
    textbox.grid_forget()
    textbox = scrolledtext.ScrolledText(search_frame, height=30, width=100, wrap=WORD, font = ("Calibri", fontsize.get()))
    global la
    la = lang.get()
    wikipedia.set_lang(dict[la])
    text = inputBox.get()
    textbox.configure(state='normal')
    try:
        w = wikipedia.summary(str(text))
        text_lst = []
        textbox.delete('1.0', END)

        for i in str(w).strip().split('. '):
            text_lst.append(i)

        for i in text_lst:
            textbox.insert(END, '\t-> ')
            textbox.insert(END, str(i))
            textbox.insert(END, '.')
            textbox.insert(END, '\n')
        textbox.configure(state='disabled')
        textbox.grid(row=2, column=0, columnspan=3, pady=15)
    except Exception as e:
        textbox.configure(state='normal')
        textbox.delete('1.0', END)
        textbox.insert(END, str(e) + '\n\nSearch for any one of the above particular words')
        textbox.grid(row=2, column=0, columnspan=3, pady=15)

search_frame = LabelFrame(root, text='Search', padx=10, pady=10)
search_frame.grid(row=0, column=0, padx=20, pady=20)

font_size = [10,11,12,13,14,15,16,17,18,19,20]
fontsize = IntVar()
fontsize.set(font_size[2])
drop_down = OptionMenu(search_frame, fontsize, *font_size)
drop_down.grid(row = 1, column=2)
drop_down.config(width=10, fg='white', bg='black')


global textbox
textbox = scrolledtext.ScrolledText(search_frame, height=30, width=100, wrap=WORD, font = ("Calibri", fontsize.get()))
textbox.configure(state='normal')
textbox.grid(row=2, column=0, columnspan=3, pady=15)

inputBox = Entry(search_frame, width=50,  borderwidth=3)
inputBox.grid(row=0, column=0, columnspan=3, pady=15)
searchBtn = Button(search_frame, width = 10, text='Search', command=search)
searchBtn.grid(row=1, column=0, columnspan=3)
inputBox.focus()
lang = StringVar()
lang.set(languages[0])
drop_down = OptionMenu(search_frame, lang, *languages)
drop_down.grid(row = 0, column=2)
drop_down.config(width=10, fg='white', bg='black')

root.mainloop()
