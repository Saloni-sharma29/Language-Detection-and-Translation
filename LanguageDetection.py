from langdetect import *
from tkinter import *
from iso639 import languages
from googletrans import Translator, LANGUAGES  #pip install googletrans==3.1.0a0
#from tkinter import messagebox
from tkinter import ttk
from langdetect import DetectorFactory #enforce consistent result, if ambiguity found in text
DetectorFactory.seed=0

root = Tk()
# Set the background colour of GUI window 
#root.configure(background = 'gray') 
# Set the configuration of GUI window (WidthxHeight) 
root.geometry("800x900") 
# set the name of tkinter GUI window 
root.title("Language Detector & Translator")
root.configure(bg='ghost white')
Label(root, text='Language Detector & Translator', fg='pale violet red' ,font='arial 12 bold').pack(pady=10)

def lang_detect():
    text=t1.get('1.0', 'end-1c')
    lang_code= languages.get(alpha2=detect(text)) #alpha2:2 letter code iso639-1
    lang_detect.from_lang_ = lang_code.name
    l_d.config(text='Succesfully Detected: '+ lang_code.name, bg='white smoke')

#input text
t1=Text(root, height= 11, width=60)
#t1.place(x=100, y=100)
t1.pack()
l_d= Label(root, text=' Enter Text in any Language ', bg='white smoke')
l_d.pack(pady=10)
#button for Detecting language
Button(root, text='Detect', command=lang_detect,font='arial 10 bold').pack(pady=10)

#translation Work
trns_txt= Text(root, height=11,  width= 60)
trns_txt.place(x=300, y=300)
trns_txt.pack()


#comboBox listing of languages
language= list(LANGUAGES.values())

dst_lang=ttk.Combobox(root, values= language, width=22)
#dst_lang.place(x=320, y=320)
dst_lang.set('Translate Into?')
dst_lang.pack()

def Translate():
    translator= Translator()
    #print("Source ",lang_detect.from_lang_)
    translated= translator.translate(text= t1.get(1.0, END) , src = lang_detect.from_lang_, dest = dst_lang.get())
    trns_txt.delete(1.0,END)
    trns_txt.insert(END, translated.text)


trans_btn= Button(root, text='Translate', command=Translate, font='arial 10 bold').pack(pady=10)
#trans_btn.place(x=340, y=320 )
#trans_btn.pack()


root.mainloop()

#root.mainloop()


