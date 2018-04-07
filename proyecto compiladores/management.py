from tkinter import *
import os
import tkinter as TK
from gtts import gTTS

#Load/Get image
def loadImage(name):
    ruta = os.path.join('pictures', name)
    imagen = PhotoImage (file = ruta)
    return imagen

def showWord(word):
    Text_word.config(state=NORMAL)
    Text_word.delete(0.0, 'end')
    Text_word.insert(0.0, word)
    Text_word.config(state=DISABLED)

def addToOldComparaciones(word):
    Text_wrongComparing.config(state=NORMAL)
    Text_wrongComparing.insert(0.0, " " + word)
    Text_wrongComparing.config(state=DISABLED)

def addToChat(word):
    Text_chat.config(state=NORMAL)
    Text_chat.insert(0.0, "\n" + word)
    Text_chat.config(state=DISABLED)

def speakWINDOWS(word):
    try:
        if (isinstance(word,str) or isinstance(word,int)):
            tts = gTTS(text=word, lang='es', slow=False)
            showWord(word)
            tts.save("speech.mp3")
            os.startfile("speech.mp3")
    except Exception:
        raise

def speakMAC(word):
    try:
        if (isinstance(word,str) or isinstance(word,int)):
            tts = gTTS(text=word, lang='es', slow=False)
            showWord(word)
            tts.save("speech.mp3")
            os.system("afplay speech.mp3")
    except Exception:
        raise

def procesar(lista):
    if(lista!=[]):
        size= len(lista)
        aux= 0
        word = ''
        while(aux<size):
            word+=str(lista[0])
            lista=lista[1:]
            aux+=1
        showWord(word)
        addToChat(word)
        speakWINDOWS(word)
    else:
        print("empty list")
    
def showSame():
    status_canvas.config(bg='#006600')
    
def showDiferent():
    status_canvas.config(bg='#BB0000')

def showReset():
    status_canvas.config(bg='#000000')

#GUI start
main_screen = Tk()
main_screen.title('LescoTalk')
main_screen.minsize(1350,600)
main_screen.resizable(width=NO, height=NO)

main_canvas = Canvas(main_screen, width=1370, height=620, bg='#0078D7',highlightthickness= 0, borderwidth= 0)
main_canvas.place(x=-10, y=-10)

status_canvas = Canvas(main_canvas, width=180, height=30, bg='#000000',highlightthickness= 0, borderwidth= 0)
status_canvas.place(x=40, y=545)

Label_VectorRecibido = Label(main_canvas, text= 'Vector recibido', font= 'Helvetica 20', bg='#0078D7', fg= "#FFFFFF")
Label_VectorRecibido.place(x=40, y=220)

Label_VectorComparando = Label(main_canvas, text= 'Vector en registro', font= 'Helvetica 20', bg='#0078D7', fg= "#FFFFFF")
Label_VectorComparando.place(x=35, y=485)

Label_Status = Label(main_canvas, text= 'Estado', font= 'Helvetica 20', bg='#0078D7', fg= "#FFFFFF")
Label_Status.place(x=85, y=580)

Label_FinalWord = Label(main_canvas, text= 'Frase/Palabra', font= 'Helvetica 20', bg='#0078D7', fg= "#FFFFFF")
Label_FinalWord.place(x=645, y=565)

Label_WrongWords1 = Label(main_canvas, text= 'Comparaciones', font= 'Helvetica 20', bg='#0078D7', fg= "#FFFFFF")
Label_WrongWords1.place(x=1195, y=220)

Label_WrongWords2 = Label(main_canvas, text= 'efectuadas', font= 'Helvetica 20', bg='#0078D7', fg= "#FFFFFF")
Label_WrongWords2.place(x=1235, y=247)

Label_Chat = Label(main_canvas, text= 'Chat', font= 'Helvetica 20', bg='#0078D7', fg= "#FFFFFF")
Label_Chat.place(x=1290, y=520)

wallpaper = loadImage('bg.gif')
wallpaper_label = Label(main_canvas, image=wallpaper, bg = '#FFFFFF', highlightthickness= 0, borderwidth= 0)
wallpaper_label.place(x=195, y=0)

Text_received = Text(main_canvas, width= 37, height=18, wrap= WORD, bg= '#666666', font= 'Helvetica 10', state=DISABLED)
Text_received.place(x=15, y=15)

Text_comparing = Text(main_canvas, width= 37, height=18, wrap= WORD, bg= '#666666', font= 'Helvetica 10', state=DISABLED)
Text_comparing.place(x=15, y=280)

Text_wrongComparing = Text(main_canvas, width= 28, height=11, wrap= WORD, bg= '#666666', font= 'Helvetica 15', state=DISABLED)
Text_wrongComparing.place(x=1123, y=15)

Text_chat = Text(main_canvas, width= 37, height=17, wrap= WORD, bg= '#666666', font= 'Helvetica 11', state=DISABLED)
Text_chat.place(x=1123, y=280)

Text_word = Text(main_canvas, width= 35, height=1, wrap= WORD, bg= '#336666', font= 'Helvetica 36', fg= "#FFFFFF", state=DISABLED)
Text_word.place(x=350, y=510)

