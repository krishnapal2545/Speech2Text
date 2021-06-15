from tkinter import *
from tkinter import messagebox , ttk
import speech_recognition as sr
from googletrans import Translator , LANGUAGES

a=''

class App(object):


    def __init__(self,root):
        self.root = root
        Label(root, text = "Speech Text TRANSLATOR", font = "arial 20 bold", bg='white smoke').pack()
        Label(root,text ="Input Text", font = 'arial 13 bold', bg ='white smoke').place(x=100,y=90)
        self.Input_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady=5, width = 60)
        self.Input_text.place(x=30,y = 130)
        Label(root,text ="Translated Text", font = 'arial 13 bold', bg ='white smoke').place(x=780,y=90)
        self.Output_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady= 5, width =60)
        self.Output_text.place(x = 600 , y = 130)
        self.language = list(LANGUAGES.values())
        self.src_lang = ttk.Combobox(root, values= self.language, width =22)
        self.src_lang.place(x=25,y=60)
        self.src_lang.set('English')
        self.dest_lang = ttk.Combobox(root, values= self.language, width =22)
        self.dest_lang.place(x=870,y=60)
        self.dest_lang.set('English')
        self.btn = Button(self.root,text="Start Saying",command=self.record,font = (("Times New Roman"),15),bg = "#6CD300", fg = "black",cursor="hand2",border="0")
        self.btn.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
        self.btn.place(x=475, y=90)
        self.trans_btn = Button(root, text = 'Translate',font = 'arial 12 bold',pady = 5,command = self.Translate , bg = 'royal blue1', activebackground = 'sky blue')
        self.trans_btn.place(x = 490, y = 180)
        
        
    def record(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
          audio = r.listen(source) 
        try:
          a=(r.recognize_google(audio))
          print (a)
          self.Input_text.delete('1.0',END)
          self.Input_text.insert(END, a)
          self.Translate()
          
        except sr.UnknownValueError:                            
          b="Your Are Not Audible"
          messagebox.showwarning("Failed", b)
        

    def Translate(self):
          translator = Translator()
          translated=translator.translate(text= self.Input_text.get(1.0,END) ,src = self.src_lang.get(),dest = self.dest_lang.get())
          self.Output_text.delete('1.0',END)
          self.Output_text.insert(END, translated.text)


root = Tk()
root.title("Speech to text Translater")
root.geometry('1080x400')
app = App(root)
root.mainloop()