# coding=utf-8
import sys
import thread
import time
import Commands
import Leap
import HandGesture
from Tkinter import *
import os
import Tkinter as TK
from gtts import gTTS
from Leap import CircleGesture, SwipeGesture, KeyTapGesture, ScreenTapGesture

# global variables
frame_counter = 0  # int that counts the frame that have passed since a letter hasn't change
last_object = "null"  # string that contains the letter returned from the previous identification
nx_counter = 0  # int that counts the times that a "x" has been after a "n" to recognize the letter "ñ"
saved_flag = False  # boolean that indicates if a word or double letter is still in the "cache" (that keeps sending the same)
sentence = []  # array of the words detected to make a phrase
command_executed = False


status_canvas = Canvas()
Text_received = Text()
Text_comparing = Text()
Text_wrongComparing = Text()
Text_chat = Text()
Text_word = Text()
main_screen = Tk()



class LeapMotionListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bones_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def on_init(self, controller):
        print "initialized"

    def on_connect(self, controller):
        print "Motion Sensor Connected!"

        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        print "Motion Sensor Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        frame = controller.frame()

        global frame_counter, last_object, nx_counter, saved_flag, sentence

        if len(frame.hands) != 0:
            returnValue = "null"
            if frame.hands[0].palm_position.y > 500:
                province = HandGesture.farAwayGestures(frame)
                if province != "null":
                    print " Recorded: " + province
                    sentence.append(province)
                    frame_counter = 0
            elif len(frame.hands) == 1:
                if frame.hands[0].is_left:
                    returnValue = HandGesture.leftHandAnalysis(frame)
                else:
                    returnValue = HandGesture.rightHandAnalysis(frame)
            elif len(frame.hands) == 2 and not command_executed:
                frame_counter += 1
                if frame_counter == 200:
                    sentence = Commands.analyzer(frame.hands, sentence)
                    frame_counter = 0

            # print returnValue
            # Validates object during a frame of time
            if not returnValue == "null":
                if last_object != returnValue:  # Doubtful method of detecting ñ
                    if nx_counter == 3:
                        returnValue = "ñ"
                        nx_counter = 0
                        if not saved_flag:
                            print ("Recorded: " + returnValue)
                            sentence.append(returnValue)
                            saved_flag = True
                    elif returnValue == "n" and last_object == "x" and frame.hands[0].palm_position.y < 500:
                        nx_counter += 1
                    elif returnValue == "Puntarenas" or returnValue == "adios" or returnValue == "despacio" \
                        or returnValue == "llamar":
                        print ("Recorded: " + returnValue)
                        sentence.append(returnValue)
                        saved_flag = True
                    else:
                        print returnValue

                    last_object = returnValue
                    frame_counter = 0
                    saved_flag = False

                else:

                    if last_object == "j":
                        frame_counter += 10
                    elif returnValue == ("10" or "llamar" or "Guanacaste"):
                        frame_counter = 200
                    elif returnValue == "t":
                        frame_counter += 5
                    else:
                        frame_counter += 1

                    if frame_counter > 180:
                        frame_counter = 0
                        if not saved_flag:
                            print ("Recorded: " + returnValue)
                            sentence.append(returnValue)
                            saved_flag = True



        # Test code

        """
        print "Frame ID = " + str(frame.id) \
              + " Timestamp: " + str(frame.timestamp) \
              + " # of Hands: " + str(len(frame.hands)) \
              + " # of Fingers: " + str(len(frame.fingers)) \
              + " # of Tools: " + str(len(frame.tools)) \
              + " # of Gestures: " + str(len(frame.gestures()))

        for hand in frame.hands:
            handType = "Left Hand" if hand.is_left else "Right Hand"

            print handType + " Hand ID: " + str(hand.id) + " Palm Position: " + str(hand.palm_position)

            normal = hand.palm_normal
            direction = hand.direction

            print "Pitch: " + str(direction.pitch * Leap.RAD_TO_DEG) + " Roll: " + str(normal.roll * Leap.RAD_TO_DEG) \
                  + " Yaw: " + str(direction.yaw * Leap.RAD_TO_DEG)

            for finger in hand.fingers:
                print "Type: " + self.finger_names[finger.type] + " ID: " + str(finger.id) \
                      + " Direction: " + str(finger.direction) + " Is extended: " + str(finger.is_extended)

                for b in range(0, 4):
                    bone = finger.bone(b)
                    print "Bone: " + self.bones_names[bone.type] + " Start: " + str(bone.prev_joint) \
                          + " End: " + str(bone.next_joint) + " Direction: " + str(bone.direction)
        """
        """
        for gesture in frame.gestures():
            if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                circle = CircleGesture(gesture)

                if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI / 2:
                    clockwiseness = "clockwise"
                else:
                    clockwiseness = "counter-clockwise"

                swept_angle = 0
                if circle.state != Leap.Gesture.STATE_START:
                    previous = CircleGesture(controller.frame(1).gesture(circle.id))
                    swept_angle = (circle.progress - previous.progress) * 2 * Leap.PI

                print "Type: Circle ID: " + str(circle.id) + " Progress: " + str(circle.progress) \
                      + " Radius (mm): " + str(circle.radius) + " Swept Angle: " + str(swept_angle * Leap.RAD_TO_DEG) \
                      + " " + clockwiseness

            if gesture.type == Leap.Gesture.TYPE_SWIPE:
                swipe = SwipeGesture(gesture)
                print "Type: Swipe ID: " + str(swipe.id) + " State: " + self.state_names[gesture.state] \
                      + " Position: " + str(swipe.position) + " Direction: " + str(swipe.direction) \
                      + " Speed (mm/s): " + str(swipe.speed)

            if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
                print "Type: Screen Tap"

            if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
                print "Type: Key Tap"
                """



def main():
    global  main_screen
    listener = LeapMotionListener()
    controller = Leap.Controller()

    controller.add_listener(listener)
    GUIstart()
    main_screen.mainloop()
    print "Press enter to quit"
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)

# Load/Get image
def loadImage(name):
    ruta = os.path.join("C:\Users\ProgramInterface\Documents\MyWorkspace\LESCO_Tracking\wallpaper", name)
    imagen = PhotoImage(file=ruta)
    return imagen


# Muestra la palabra final en su textbox
def showWord(word):
    global Text_word
    Text_word.config(state=NORMAL)
    Text_word.delete(0.0, 'end')
    Text_word.insert(0.0, word)
    Text_word.config(state=DISABLED)

# Muestra el vector del gesto realizado por el usuario
def showCurrentVector(word):
    global Text_received
    Text_received.config(state=NORMAL)
    Text_received.delete(0.0, 'end')
    Text_received.insert(0.0, word)
    Text_received.config(state=DISABLED)

# Muestra el vector contra el que se esta comparando
def showVectorRegistered(word):
    global  Text_comparing
    Text_comparing.config(state=NORMAL)
    Text_comparing.delete(0.0, 'end')
    Text_comparing.insert(0.0, word)
    Text_comparing.config(state=DISABLED)

# Agrega la letra a la lista de comparaciones fallidas
def addToOldComparaciones(word):
    global Text_wrongComparing
    Text_wrongComparing.config(state=NORMAL)
    Text_wrongComparing.insert(0.0, " " + word)
    Text_wrongComparing.config(state=DISABLED)

# Resetea el textbox usado para mostrar antiguas comparaciones
def resetOldComparaciones():
    global Text_wrongComparing
    Text_wrongComparing.config(state=NORMAL)
    Text_wrongComparing.delete(0.0, 'end')
    Text_wrongComparing.config(state=DISABLED)

# Agrega la palabra al registro de la conversacion
def addToChat(word):
    global Text_chat
    Text_chat.config(state=NORMAL)
    Text_chat.insert(0.0, "\n" + word)
    Text_chat.config(state=DISABLED)

# Reproduce sonido en windows
def speakWINDOWS(word):
    try:
        if (isinstance(word, str) or isinstance(word, int)):
            tts = gTTS(text=word, lang='es', slow=False)
            showWord(word)
            tts.save("speech.mp3")
            os.startfile("speech.mp3")
    except Exception:
        raise

# Reproduce sonido en mac
def speakMAC(word):
    try:
        if (isinstance(word, str) or isinstance(word, int)):
            tts = gTTS(text=word, lang='es', slow=False)
            showWord(word)
            tts.save("speech.mp3")
            os.system("afplay speech.mp3")
    except Exception:
        raise

# Recibe la lista con las letras y procesa esto para su interpretacion
def procesar(lista):
    global  main_screen
    if (lista != []):
        size = len(lista)
        aux = 0
        word = ''
        while (aux < size):
            word += str(lista[0])
            lista = lista[1:]
            aux += 1
        showWord(word)
        addToChat(word)
        #main_screen.mainloop()
        speakWINDOWS(word)
    else:
        print("empty list")

# Indicador de similitud en el vector recibido
def showSame():
    status_canvas.config(bg='#006600')

# Indicador de diferencia en el vector recibido
def showDiferent():
    status_canvas.config(bg='#BB0000')

# Reset del indicador visual
def showReset():
    status_canvas.config(bg='#000000')


# GUI start
def GUIstart():
    global status_canvas, Text_chat, Text_comparing, Text_received, Text_word, Text_wrongComparing, main_screen

    main_screen.title('LescoTalk')
    main_screen.minsize(1350, 600)
    main_screen.resizable(width=NO, height=NO)

    main_canvas = Canvas(main_screen, width=1370, height=620, bg='#0078D7', highlightthickness=0, borderwidth=0)
    main_canvas.place(x=-10, y=-10)

    status_canvas = Canvas(main_canvas, width=180, height=30, bg='#000000', highlightthickness=0, borderwidth=0)
    status_canvas.place(x=40, y=545)

    Label_VectorRecibido = Label(main_canvas, text='Vector recibido', font='Helvetica 16', bg='#0078D7', fg="#FFFFFF")
    Label_VectorRecibido.place(x=40, y=220)

    Label_VectorComparando = Label(main_canvas, text='Vector en registro', font='Helvetica 16', bg='#0078D7', fg="#FFFFFF")
    Label_VectorComparando.place(x=15, y=485)

    Label_Status = Label(main_canvas, text='Estado', font='Helvetica 20', bg='#0078D7', fg="#FFFFFF")
    Label_Status.place(x=85, y=580)

    Label_FinalWord = Label(main_canvas, text='Frase/Palabra', font='Helvetica 20', bg='#0078D7', fg="#FFFFFF")
    Label_FinalWord.place(x=645, y=565)

    Label_WrongWords1 = Label(main_canvas, text='Comparaciones', font='Helvetica 17', bg='#0078D7', fg="#FFFFFF")
    Label_WrongWords1.place(x=1195, y=220)

    Label_WrongWords2 = Label(main_canvas, text='efectuadas', font='Helvetica 18', bg='#0078D7', fg="#FFFFFF")
    Label_WrongWords2.place(x=1235, y=247)

    Label_Chat = Label(main_canvas, text='Chat', font='Helvetica 18', bg='#0078D7', fg="#FFFFFF")
    Label_Chat.place(x=1290, y=520)

    wallpaper = loadImage("image.gif")
    wallpaper_label = Label(main_canvas, bg='#FFFFFF', highlightthickness=0, borderwidth=0)
    wallpaper_label.place(x=195, y=0)

    Text_received = Text(main_canvas, width=25, height=11, wrap=WORD, bg='#666666', font='Helvetica 13', state=DISABLED)
    Text_received.place(x=15, y=15)

    Text_comparing = Text(main_canvas, width=25, height=11, wrap=WORD, bg='#666666', font='Helvetica 13', state=DISABLED)
    Text_comparing.place(x=15, y=280)

    Text_wrongComparing = Text(main_canvas, width=25, height=10, wrap=WORD, bg='#666666', font='Helvetica 13', state=DISABLED)
    Text_wrongComparing.place(x=1123, y=15)

    Text_chat = Text(main_canvas, width=25, height=12, wrap=WORD, bg='#666666', font='Helvetica 13', state=DISABLED)
    Text_chat.place(x=1123, y=280)

    Text_word = Text(main_canvas, width=25, height=1, wrap=WORD, bg='#336666', font='Helvetica 36', fg="#FFFFFF", state=DISABLED)
    Text_word.place(x=350, y=510)

    main_screen.mainloop()

    '''
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
        Text_chat.insert(0.0, "" + word)
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
    '''


if __name__ == "__main__":
    main()
    # TODO: validate number or letter after a few seconds (maybe 2 seconds or so)

