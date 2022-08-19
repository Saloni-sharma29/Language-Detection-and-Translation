from langdetect import *
from tkinter import *
from iso639 import languages
from googletrans import Translator, LANGUAGES  #pip install googletrans==3.1.0a0
from tkinter import messagebox
from tkinter import ttk

root = Tk()
# Set the background colour of GUI window 
#root.configure(background = 'gray') 
# Set the configuration of GUI window (WidthxHeight) 
root.geometry("800x1500") 
# set the name of tkinter GUI window 
root.title("language Ditector")

def lang_detect():
    text=t1.get('1.0', 'end-1c')
    lang_code= languages.get(alpha2=detect(text))
    l_d.config(text='Succesfully Detected: '+ lang_code.name)

#input text
t1=Text(root, height= 11, width=60)
t1.place(x=100, y=100)
t1.pack()
l_d= Label(root, text=' Enter Text in any Language ')
l_d.pack(pady=10)
#button for Detecting language
Button(root, text='Detect', command=lang_detect).pack(pady=10)

#translation Work
trns_txt= Text(root, height=11,  width= 60)
trns_txt.place(x=300, y=300)
trns_txt.pack()


#comboBox listing of languages
language= list(LANGUAGES.values())

dst_lang=ttk.Combobox(root, values= language, width=22)
dst_lang.place(x=320, y=320)
dst_lang.set('Translate Into?')
dst_lang.pack()

def Translate():
    translator= Translator()
    translated= translator.translate(text=t1.get(1.0, END) , dest=dst_lang.get())

    trns_txt.delete(1.0,END)
    trns_txt.insert(END, translated.text)


trans_btn= Button(root, text='Translate', command=Translate, )
trans_btn.place(x=340, y=320 )
trans_btn.pack()


root.mainloop()

#root.mainloop()


