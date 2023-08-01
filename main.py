import webbrowser       #pip install webbrowser
import os               #pip install os
#import beepy
import math
import pyjokes as pyjokes
import wmi #to find the running apps        #pip instal wmi
import pyttsx3 #for voice       #pip install pyttsx3
import datetime                 #pip install DateTime
import speech_recognition as sr #for recognising speech     #pip install SpeechRecognition
import wikipedia #for wikipedia search    # pip install wikipedia
import turtle  #for snake graphics       #pip install PythonTurtle
import time        #pip install python-time
import random
import psutil   #pip install psutil
#import pyjokes #for jokes    #pip install pyjokes
import pyautogui #for taking screen shot   #pip install pyautogui
import winsound # for beep sound    #pip install winsound
import win32api # for beep sound    #pip install win32api
from win32con import * # for beep sound
import platform #for knowing about the system   #pip install lib-plartform
import wolframalpha #data set for exceptional questions and for calculations     #pip install wolframalpha
import subprocess # for getting wifi details

#advance
import os
import openai

#theraphy
import logging
import random
import re
from collections import namedtuple
from past.builtins import raw_input

#mouse controls
from imutils import face_utils
from utils import *
import numpy as np
import imutils
import dlib #https://github.com/jloh02/dlib/releases/download/v19.22/dlib-19.22.99-cp310-cp310-win_amd64.whl
import cv2 #pip install opencv-python
#multithreading
import _thread
import threading
#UI
import tkinter as tk
from PIL import Image, ImageTk

#SOS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#sound
from pydub import AudioSegment
from pydub.playback import play

# from openai.api_resources import completion
"""from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from natasha_ui import Ui_natash_ui"""
import sys

global drag #speed
drag=10


client = wolframalpha.Client('R2XLET-3TL6LJRWQ8')     #LRWJW6-436RP7LH87
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# global listen
# global user
# global said
# global threadui
# global copy1
# global dead
# global total_error
dead = True
copy1 = 0
threadui = 0
listen = ""
user = ""
said = ""
mouse_thread_flag = 0
total_error = False
def UI():
    global listen
    global user
    global said
    global copy1
    global total_error
    try:
        root = tk.Tk()
        root.geometry("780x880")
        root.title("NATASHA")
        button_frame = tk.Frame(root, bg="#080721")

        text_field3 = tk.Text(button_frame, height=1, width=70)
        text_field3.pack(side="top", pady=10)

        text_field1 = tk.Text(button_frame, height=2, width=70)
        text_field1.pack(side="top", pady=10)

        text_field2 = tk.Text(button_frame, height=18, width=78)
        text_field2.pack(side="bottom", pady=10)

        # Delete the text from the widget
        # text_field1.delete('1.0', tk.END)
        button_frame.pack(side="bottom", pady=0)

        gif = Image.open('ai.gif')
        tkimage = ImageTk.PhotoImage(gif.convert('RGBA'))

        label = tk.Label(root, image=tkimage)
        label.pack()
        button_frame.lift()

        def update_label(index):
            global copy1
            global threadui
            if threadui == 1:
                exit()
            elif total_error == True:
                exit()
            text_field1.delete("1.0", tk.END)
            text_field1.insert(tk.END, user)
            text_field3.delete("1.0", tk.END)
            text_field3.insert(tk.END, listen)
            if copy1 == 0:
                text_field2.delete("1.0", tk.END)
                text_field2.insert(tk.END, said)
            global tkimage
            gif.seek(index)
            tkimage = ImageTk.PhotoImage(gif.convert('RGBA'))
            label.config(image=tkimage)
            root.after(10, update_label, (index + 1) % gif.n_frames)

        root.after(0, update_label, 1)

        root.mainloop()
    except Exception:
        speak("reopen the application")
        exit(1)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('hi sir ,.., good morning')
    elif hour >= 12 and hour < 18:
        speak('hi sir ,.., good afternoon')
    else:
        speak('hi sir ,.., good evening')

    stime = datetime.datetime.now().strftime("%H:%M:%S")
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak('the current time is  '+str(stime))
    speak("the current date is  ,..,  "+str(day)+'  ,.., '+str(month)+' ,..,   '+str(year))
    speak('call my name,.., when you need my help ')


def takecommand():
    global listen
    global user
    global said
    # sound = AudioSegment.from_wav('beep-07a.wav')
    # play(sound)
    listen = "listening..."  # zz
    print(listen)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #beep(sound="ping")
        # winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        # winsound.Beep(28000, 100)
        winsound.PlaySound("beep-07a.wav",winsound.SND_FILENAME)
        r.pause_threshold = 1 #sethu
        audio = r.listen(source, timeout=10, phrase_time_limit=5)

    try:
        listen="wait for few moments..."#zz
        print(listen)
        query = ''
        query = r.recognize_google(audio, language='en-in')
        user="you said "+query
        print("user said", query)

    except Exception:
        #print(Exception)
        print("i didn't hear you") #zz
        listen="i didn't hear you"
    return query.lower()



def takerawcommand():
    global listen
    global user
    global said
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # sound = AudioSegment.from_wav('beep1.wav')
        # winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        #winsound.PlaySound("beep1.wav", winsound.SND_FILENAME)
        # winsound.Beep(28000, 100)
        winsound.PlaySound("beep-07a.wav", winsound.SND_FILENAME)
        #winsound.Beep(32767, 200)
        # play(sound)
        listen="listening..."
        print("listening...")#zz
        r.pause_threshold = 1
        audio = r.listen(source, timeout=10 , phrase_time_limit=5)

    try:
        listen="wait for few moments..."
        print("wait for few moments...")#zz
        query =''
        query = r.recognize_google(audio, language='en-in')
        user="you said: "+query
        print("user said", query)#zz

    except Exception:
        #print(Exception)
        listen="i didn't hear you"
        print("i didn't hear you")#zz
    return query

def cpu():
    usage = str(psutil.cpu_percent())
    speak('cpu   usage  is at'+usage+'%')
    battery = psutil.sensors_battery()
    speak('battery is at')
    b=str(battery)
    speak(str(b)+'%')
def system():
    global listen
    global user
    global said
    my_system = platform.uname()

    a=f"System: {my_system.system}"
    print(a)#zz
    #speak(a)
    b= f"Node Name: {my_system.node}"
    print(b)#zz
    #speak(b)
    c=f"Release: {my_system.release}"
    print(c)
    #speak(c)
    d=f"Version: {my_system.version}"
    print(d)
    #speak(d)
    e=f"Machine: {my_system.machine}"
    print(e)
    #speak(e)
    f=f"Processor: {my_system.processor}"
    print(f)
    #speak(f)
    said=a+"\n"+b+"\n"+c+"\n"+d+"\n"+e+"\n"+f

def system2():
    c = wmi.WMI()
    my_system = c.Win32_ComputerSystem()[0]

    a=f"Manufacturer: {my_system.Manufacturer}"
    print(a)
    #speak(a)
    b=f"Model: {my_system.Model}"
    print(b)
    #speak(b)
    c=f"Name: {my_system.Name}"
    print(c)
    #speak(c)
    d=f"NumberOfProcessors: {my_system.NumberOfProcessors}"
    print(d)
    #speak(d)
    e=f"SystemType: {my_system.SystemType}"
    print(e)
    #speak(e)
    f=f"SystemFamily: {my_system.SystemFamily}"
    print(f)
    #speak(f)
    print()

    print()
    #speak('and    sir   ')

def joke():
    speak(pyjokes.get_joke())

#mouse controls
def right_click():
    speak("clicked")
    pyautogui.rightClick()
def left_click():
    speak("clicked")
    pyautogui.leftClick()
def double_click():
    speak("clicked")
    pyautogui.doubleClick()
def hold():
    speak("you can drag now")
    pyautogui.mouseDown(button='left')
def release():
    speak("released")
    pyautogui.mouseUp(button='left')

def maximize_window():
    pyautogui.hotkey("win", "up")
    time.sleep(0.5)
    speak("Maximized")

def minimize_window():
    pyautogui.hotkey("win", "down")
    time.sleep(0.5)
    speak("Minimized")

def close_window():
    pyautogui.hotkey("alt", "f4")
    time.sleep(0.5)
    speak("Closed")

def type():
    global listen
    global user
    global said
    mapping = {
        "backspace": "backspace",
        "tab": "tab",
        "enter": "enter",
        "shift": "shift",
        "ctrl": "ctrl",
        "control": "ctrl",
        "alt": "alter",
        "alter": "alt",
        "pause": "pause",
        "caps lock": "capslock",
        "esc": "esc",
        "space": "space",
        "page up": "pageup",
        "page down": "pagedown",
        "end": "end",
        "home": "home",
        "left": "left",
        "up": "up",
        "right": "right",
        "down": "down",
        "insert": "insert",
        "delete": "delete",
        "command": "command",
        "f1": "f1",
        "f2": "f2",
        "f3": "f3",
        "f4": "f4",
        "f5": "f5",
        "f6": "f6",
        "f7": "f7",
        "f8": "f8",
        "f9": "f9",
        "f10": "f10",
        "f11": "f11",
        "f12": "f12",
        "print screen": "printscreen",
        "scroll lock": "scrolllock",
        "num lock": "numlock",
        "backquote": "`",
        "minus": "-",
        "equals": "=",
        "left square bracket": "[",
        "right square bracket": "]",
        "backslash": "\\",
        "semicolon": ";",
        "apostrophe": "'",
        "comma": ",",
        "period": ".",
        "slash": "/",
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "a": "a",
        "b": "b",
        "be": "b",
        "bee": "b",
        "see": "c",
        "sea": "c",
        "c": "c",
        "d": "d",
        "dee": "d",
        "de": "d",
        "di": "d",
        "e": "e",
        "f": "f",
        "ef": "f",
        "eff": "f",
        "yef": "f",
        "g": "g",
        "je": "g",
        "gi": "g",
        "ge": "g",
        "h": "h",
        "eh": "h",
        "i": "i",
        "ai": "i",
        "ei": "i",
        "yi": "i",
        "j": "j",
        "jey": "j",
        "jhey": "j",
        "k": "k",
        "kay": "k",
        "el": "l",
        "l": "l",
        "yel": "l",
        "em": "m",
        "m": "m",
        "yem": "m",
        "yum": "m",
        "n": "n",
        "en": "n",
        "enn": "n",
        "o": "o",
        "oo": "o",
        "oh": "o",
        "p": "p",
        "pee": "p",
        "q": "q",
        "qu": "q",
        "queue": "q",
        "que": "q",
        "r": "r",
        "ar": "r",
        "s": "s",
        "yes": "s",
        "es": "s",
        "t": "t",
        "tee": "t",
        "tea": "t",
        "u": "u",
        "you": "u",
        "v": "v",
        "we": "v",
        "vi": "v",
        "ve": "v",
        "w": "w",
        "double you": "w",
        "double u": "w",
        "double": "w",
        "x": "x",
        "ex": "x",
        "yex": "x",
        "y": "y",
        "why": "y",
        "z": "z",
        "ez": "z"

    }  # hello  how are you type hello how are you

    speak("key board access granted...")
    lkeys = []
    while True:
        try:
            user_input = takecommand().strip()
            key = mapping.get(user_input.lower())
            if key:
                pyautogui.press(key)
                pyautogui.keyUp(key)
                speak(key+" pressed")
            elif user_input.lower() == "copy":
                pyautogui.keyDown("ctrl")
                pyautogui.press("c")
                pyautogui.keyUp("ctrl")
                speak("copied...")
            elif user_input.lower() == "paste":
                pyautogui.keyDown("ctrl")
                pyautogui.press("v")
                pyautogui.keyUp("ctrl")
                speak("pasted...")
            elif user_input.lower() == "undo":
                pyautogui.keyDown("ctrl")
                pyautogui.press("z")
                pyautogui.keyUp("ctrl")
                speak("undone...")
            elif user_input.lower() == "select all":
                pyautogui.keyDown("ctrl")
                pyautogui.press("a")
                pyautogui.keyUp("ctrl")
                speak("selected")
            elif user_input.lower() == "left click":  # left click
                pyautogui.leftClick()
                speak("done")
            elif user_input.lower() == "right click":  # right click
                pyautogui.rightClick()
                speak("done")
            elif user_input.lower() == "double click":
                pyautogui.doubleClick()
                speak("done")
            elif user_input.lower() == "drag":
                pyautogui.mouseDown(button='left')
                speak("now you can drag ")
            elif user_input.lower() == "release":
                pyautogui.mouseUp(button='left')
                speak("released ")
            elif user_input.lower() == "maximize":
                pyautogui.hotkey("win", "up")
                time.sleep(0.5)
                speak("maximized")
            elif user_input.lower() == "minimise":
                pyautogui.hotkey("win", "down")
                time.sleep(0.5)
                speak("minimized")
            elif user_input.lower() == "close":
                pyautogui.hotkey("alt", "f4")
                time.sleep(0.5)
                speak("closed")
            elif "hold" in user_input.lower():
                if len(user_input.strip().split()) >= 2:
                    user_input = user_input.strip().split(" ")[-1]
                    key = mapping.get(user_input.lower())
                    pyautogui.keyDown(key)
                    lkeys.append(key)
                    speak(key+" is on hold ")
            elif "release" in user_input.lower():
                if len(user_input.strip().split()) >= 2:
                    user_input = user_input.strip().split(" ")[-1]
                    key = mapping.get(user_input.lower())
                    pyautogui.keyUp(key)
                    speak(key + " is released")
            elif "reset" in user_input.lower():
                for i in lkeys:
                    pyautogui.keyUp(i)
                speak("keyboard has been reset ")
                lkeys = []


            elif "deactivate" in user_input:  # sethu this is to end the loop
                speak("keyboard access deactivated")
                break
            elif "type" in user_input:
                user_input = user_input[5:]
                for i in user_input:
                    pyautogui.typewrite(i)  # string input
                pyautogui.typewrite(" ")
        except Exception:
            print("try again...")#zz
            said = "try again..."


def theraphy():
    # Fix Python2/Python3 incompatibility
    try:
        input = raw_input
    except NameError:
        pass

    log = logging.getLogger(__name__)

    class Key:
        def __init__(self, word, weight, decomps):
            self.word = word
            self.weight = weight
            self.decomps = decomps

    class Decomp:
        def __init__(self, parts, save, reasmbs):
            self.parts = parts
            self.save = save
            self.reasmbs = reasmbs
            self.next_reasmb_index = 0

    class Theraphy:
        def __init__(self):
            self.initials = []
            self.finals = []
            self.quits = []
            self.pres = {}
            self.posts = {}
            self.synons = {}
            self.keys = {}
            self.memory = []

        def load(self, path):
            key = None
            decomp = None
            with open(path) as file:
                for line in file:
                    if not line.strip():
                        continue
                    tag, content = [part.strip() for part in line.split(':')]
                    if tag == 'initial':
                        self.initials.append(content)
                    elif tag == 'final':
                        self.finals.append(content)
                    elif tag == 'quit':
                        self.quits.append(content)
                    elif tag == 'pre':
                        parts = content.split(' ')
                        self.pres[parts[0]] = parts[1:]
                    elif tag == 'post':
                        parts = content.split(' ')
                        self.posts[parts[0]] = parts[1:]
                    elif tag == 'synon':
                        parts = content.split(' ')
                        self.synons[parts[0]] = parts
                    elif tag == 'key':
                        parts = content.split(' ')
                        word = parts[0]
                        weight = int(parts[1]) if len(parts) > 1 else 1
                        key = Key(word, weight, [])
                        self.keys[word] = key
                    elif tag == 'decomp':
                        parts = content.split(' ')
                        save = False
                        if parts[0] == '$':
                            save = True
                            parts = parts[1:]
                        decomp = Decomp(parts, save, [])
                        key.decomps.append(decomp)
                    elif tag == 'reasmb':
                        parts = content.split(' ')
                        decomp.reasmbs.append(parts)

        def _match_decomp_r(self, parts, words, results):
            if not parts and not words:
                return True
            if not parts or (not words and parts != ['*']):
                return False
            if parts[0] == '*':
                for index in range(len(words), -1, -1):
                    results.append(words[:index])
                    if self._match_decomp_r(parts[1:], words[index:], results):
                        return True
                    results.pop()
                return False
            elif parts[0].startswith('@'):
                root = parts[0][1:]
                if not root in self.synons:
                    raise ValueError("Unknown synonym root {}".format(root))
                if not words[0].lower() in self.synons[root]:
                    return False
                results.append([words[0]])
                return self._match_decomp_r(parts[1:], words[1:], results)
            elif parts[0].lower() != words[0].lower():
                return False
            else:
                return self._match_decomp_r(parts[1:], words[1:], results)

        def _match_decomp(self, parts, words):
            results = []
            if self._match_decomp_r(parts, words, results):
                return results
            return None

        def _next_reasmb(self, decomp):
            index = decomp.next_reasmb_index
            result = decomp.reasmbs[index % len(decomp.reasmbs)]
            decomp.next_reasmb_index = index + 1
            return result

        def _reassemble(self, reasmb, results):
            output = []
            for reword in reasmb:
                if not reword:
                    continue
                if reword[0] == '(' and reword[-1] == ')':
                    index = int(reword[1:-1])
                    if index < 1 or index > len(results):
                        raise ValueError("Invalid result index {}".format(index))
                    insert = results[index - 1]
                    for punct in [',', '.', ';']:
                        if punct in insert:
                            insert = insert[:insert.index(punct)]
                    output.extend(insert)
                else:
                    output.append(reword)
            return output

        def _sub(self, words, sub):
            output = []
            for word in words:
                word_lower = word.lower()
                if word_lower in sub:
                    output.extend(sub[word_lower])
                else:
                    output.append(word)
            return output

        def _match_key(self, words, key):
            for decomp in key.decomps:
                results = self._match_decomp(decomp.parts, words)
                if results is None:
                    log.debug('Decomp did not match: %s', decomp.parts)
                    continue
                log.debug('Decomp matched: %s', decomp.parts)
                log.debug('Decomp results: %s', results)
                results = [self._sub(words, self.posts) for words in results]
                log.debug('Decomp results after posts: %s', results)
                reasmb = self._next_reasmb(decomp)
                log.debug('Using reassembly: %s', reasmb)
                if reasmb[0] == 'goto':
                    goto_key = reasmb[1]
                    if not goto_key in self.keys:
                        raise ValueError("Invalid goto key {}".format(goto_key))
                    log.debug('Goto key: %s', goto_key)
                    return self._match_key(words, self.keys[goto_key])
                output = self._reassemble(reasmb, results)
                if decomp.save:
                    self.memory.append(output)
                    log.debug('Saved to memory: %s', output)
                    continue
                return output
            return None

        def respond(self, text):
            if text.lower() in self.quits:
                return None

            text = re.sub(r'\s*\.+\s*', ' . ', text)
            text = re.sub(r'\s*,+\s*', ' , ', text)
            text = re.sub(r'\s*;+\s*', ' ; ', text)
            log.debug('After punctuation cleanup: %s', text)

            words = [w for w in text.split(' ') if w]
            log.debug('Input: %s', words)

            words = self._sub(words, self.pres)
            log.debug('After pre-substitution: %s', words)

            keys = [self.keys[w.lower()] for w in words if w.lower() in self.keys]
            keys = sorted(keys, key=lambda k: -k.weight)
            log.debug('Sorted keys: %s', [(k.word, k.weight) for k in keys])

            output = None

            for key in keys:
                output = self._match_key(words, key)
                if output:
                    log.debug('Output from key: %s', output)
                    break
            if not output:
                if self.memory:
                    index = random.randrange(len(self.memory))
                    output = self.memory.pop(index)
                    log.debug('Output from memory: %s', output)
                else:
                    output = self._next_reasmb(self.keys['xnone'].decomps[0])
                    log.debug('Output from xnone: %s', output)

            return " ".join(output)

        def initial(self):
            return random.choice(self.initials)

        def final(self):
            return random.choice(self.finals)

        def run(self):
            global said
            global user
            global listen
            print(self.initial())#zz
            said=self.initial()
            speak("i am your therapist")
            speak(self.initial())

            while True:
                sent = takecommand()  # sethu

                if sent == "deactivate":
                    print(self.final())#zz
                    said=self.final()
                    speak(self.final())
                    break
                elif sent != "":
                    output = self.respond(sent)
                    if output is None:
                        break

                    print(output)
                    said = output
                    speak(output)

    def main():
        theraphy = Theraphy()
        theraphy.load('theraphy.txt')
        theraphy.run()

    if __name__ == '__main__':
        logging.basicConfig()
        main()
def mouse_cursor_control():

    # Thresholds and consecutive frame length for triggering the mouse action.
    MOUTH_AR_THRESH = 0.6
    MOUTH_AR_CONSECUTIVE_FRAMES = 15
    EYE_AR_THRESH = 0.19
    EYE_AR_CONSECUTIVE_FRAMES = 15
    WINK_AR_DIFF_THRESH = 0.04
    WINK_AR_CLOSE_THRESH = 0.19
    WINK_CONSECUTIVE_FRAMES = 10

    # Initialize the frame counters for each action as well as
    # booleans used to indicate if action is performed or not
    MOUTH_COUNTER = 0
    EYE_COUNTER = 0
    WINK_COUNTER = 0
    INPUT_MODE = False
    EYE_CLICK = False
    LEFT_WINK = False
    RIGHT_WINK = False
    SCROLL_MODE = False
    ANCHOR_POINT = (0, 0)
    WHITE_COLOR = (255, 255, 255)
    YELLOW_COLOR = (0, 255, 255)
    RED_COLOR = (0, 0, 255)
    GREEN_COLOR = (0, 255, 0)
    BLUE_COLOR = (255, 0, 0)
    BLACK_COLOR = (0, 0, 0)

    # Initialize Dlib's face detector (HOG-based) and then create
    # the facial landmark predictor
    shape_predictor = "shape_predictor_68_face_landmarks.dat"
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(shape_predictor)

    # Grab the indexes of the facial landmarks for the left and
    # right eye, nose and mouth respectively
    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
    (nStart, nEnd) = face_utils.FACIAL_LANDMARKS_IDXS["nose"]
    (mStart, mEnd) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]

    # Video capture
    vid = cv2.VideoCapture(0)
    resolution_w = 1366
    resolution_h = 768
    cam_w = 640
    cam_h = 480
    unit_w = resolution_w / cam_w
    unit_h = resolution_h / cam_h
    a = 3
    global dead
    global drag
    while (not dead):
        try:
            # Grab the frame from the threaded video file stream, resize
            # it, and convert it to grayscale
            # channels)
            _, frame = vid.read()
            frame = cv2.flip(frame, 1)
            frame = imutils.resize(frame, width=cam_w, height=cam_h)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the grayscale frame
            rects = detector(gray, 0)

            # Loop over the face detections
            if len(rects) > 0:
                rect = rects[0]
            else:
                cv2.imshow("Frame", frame)
                key = cv2.waitKey(1) & 0xFF
                continue

            # Determine the facial landmarks for the face region, then
            # convert the facial landmark (x, y)-coordinates to a NumPy
            # array
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            # Extract the left and right eye coordinates, then use the
            # coordinates to compute the eye aspect ratio for both eyes
            mouth = shape[mStart:mEnd]
            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            nose = shape[nStart:nEnd]

            # Because I flipped the frame, left is right, right is left.
            temp = leftEye
            leftEye = rightEye
            rightEye = temp

            # Average the mouth aspect ratio together for both eyes
            mar = mouth_aspect_ratio(mouth)
            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)
            ear = (leftEAR + rightEAR) / 2.0
            diff_ear = np.abs(leftEAR - rightEAR)
            nose_point = (nose[3, 0], nose[3, 1])

            # Compute the convex hull for the left and right eye, then
            # visualize each of the eyes
            mouthHull = cv2.convexHull(mouth)
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame, [mouthHull], -1, YELLOW_COLOR, 1)
            cv2.drawContours(frame, [leftEyeHull], -1, YELLOW_COLOR, 1)
            cv2.drawContours(frame, [rightEyeHull], -1, YELLOW_COLOR, 1)

            for (x, y) in np.concatenate((mouth, leftEye, rightEye), axis=0):
                cv2.circle(frame, (x, y), 2, GREEN_COLOR, -1)

            # Check to see if the eye aspect ratio is below the blink
            # threshold, and if so, increment the blink frame counter
            if diff_ear > WINK_AR_DIFF_THRESH:

                if leftEAR < rightEAR:
                    if leftEAR < EYE_AR_THRESH:
                        WINK_COUNTER += 1

                        if WINK_COUNTER > WINK_CONSECUTIVE_FRAMES:
                            tempwink = 0  # pyauto click by wink can be added

                            WINK_COUNTER = 0

                elif leftEAR > rightEAR:
                    if rightEAR < EYE_AR_THRESH:
                        WINK_COUNTER += 1

                        if WINK_COUNTER > WINK_CONSECUTIVE_FRAMES:
                            tempwink = 1

                            WINK_COUNTER = 0
                else:
                    WINK_COUNTER = 0
            else:
                if ear <= EYE_AR_THRESH:
                    EYE_COUNTER += 1

                    if EYE_COUNTER > EYE_AR_CONSECUTIVE_FRAMES:
                        SCROLL_MODE = not SCROLL_MODE
                        # INPUT_MODE = not INPUT_MODE
                        EYE_COUNTER = 0

                        # nose point to draw a bounding box around it

                else:
                    EYE_COUNTER = 0
                    WINK_COUNTER = 0

            if a >= 3:
                # MOUTH_COUNTER += 1
                if a >= 3:
                    # if the alarm is not on, turn it on
                    INPUT_MODE = not INPUT_MODE
                    # SCROLL_MODE = not SCROLL_MODE
                    # MOUTH_COUNTER = 0
                    ANCHOR_POINT = (300, 230)
                    a = 0
            """if mar >= MOUTH_AR_THRESH:
                MOUTH_COUNTER += 1
                if MOUTH_COUNTER >= MOUTH_AR_CONSECUTIVE_FRAMES:
                    # if the alarm is not on, turn it on
                        INPUT_MODE = not INPUT_MODE
                    # SCROLL_MODE = not SCROLL_MODE
                        MOUTH_COUNTER = 0
                        ANCHOR_POINT = nose_point

            else:
                MOUTH_COUNTER = 0"""

            if INPUT_MODE:
                cv2.putText(frame, "READING INPUT!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED_COLOR, 2)
                x, y = ANCHOR_POINT
                nx, ny = nose_point
                w, h = 60, 35
                multiple = 1
                cv2.rectangle(frame, (x - w, y - h), (x + w, y + h), GREEN_COLOR, 2)
                cv2.line(frame, ANCHOR_POINT, nose_point, BLUE_COLOR, 2)
                dir = direction(nose_point, ANCHOR_POINT, w, h)
                cv2.putText(frame, dir.upper(), (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED_COLOR, 2)
                #drag = 10

                #if math.dist(ANCHOR_POINT, nose_point) < 110:
                  #  drag = 10
                    #print(math.dist(ANCHOR_POINT, nose_point))
               #if math.dist(ANCHOR_POINT, nose_point) >= 110:
                 #   drag = 50
                    #print(math.dist(ANCHOR_POINT, nose_point))
                if dir == 'right':
                    if math.dist(ANCHOR_POINT, nose_point) < 130:
                        drag = 10
                        pyautogui.moveRel(drag, 0)
                        # print(math.dist(ANCHOR_POINT, nose_point))
                    elif math.dist(ANCHOR_POINT, nose_point) >= 130:
                        drag = 50
                        pyautogui.moveRel(drag, 0)
                elif dir == 'left':
                    if math.dist(ANCHOR_POINT, nose_point) < 130:
                        drag = 10
                        pyautogui.moveRel(-drag, 0)
                        # print(math.dist(ANCHOR_POINT, nose_point))
                    elif math.dist(ANCHOR_POINT, nose_point) >= 130:
                        drag = 50
                        pyautogui.moveRel(-drag, 0)
                    # pyautogui.moveRel(-drag, 0)
                elif dir == 'up':
                    # if SCROLL_MODE:
                    # pyautogui.scroll(40)
                    # else:
                    if math.dist(ANCHOR_POINT, nose_point) < 100:
                        drag = 10
                        pyautogui.moveRel(0, -drag)
                        # print(math.dist(ANCHOR_POINT, nose_point))
                    elif math.dist(ANCHOR_POINT, nose_point) >= 110:
                        drag = 50
                        pyautogui.moveRel(0, -drag)
                    # pyautogui.moveRel(0, -drag)
                elif dir == 'down':
                    # if SCROLL_MODE:
                    #    pyautogui.scroll(-40)
                    # else:
                    if math.dist(ANCHOR_POINT, nose_point) < 100:
                        drag = 10
                        pyautogui.moveRel(0, drag)
                        # print(math.dist(ANCHOR_POINT, nose_point))
                    elif math.dist(ANCHOR_POINT, nose_point) >= 100:
                        drag = 50
                        pyautogui.moveRel(0, drag)
                # pyautogui.moveRel(0, drag)

            # if SCROLL_MODE:
            # cv2.putText(frame, 'SCROLL MODE IS ON!', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED_COLOR, 2)

            # cv2.putText(frame, "MAR: {:.2f}".format(mar), (500, 30),
            #             cv2.FONT_HERSHEY_SIMPLEX, 0.7, YELLOW_COLOR, 2)
            # cv2.putText(frame, "Right EAR: {:.2f}".format(rightEAR), (460, 80),
            #             cv2.FONT_HERSHEY_SIMPLEX, 0.7, YELLOW_COLOR, 2)
            # cv2.putText(frame, "Left EAR: {:.2f}".format(leftEAR), (460, 130),
            #             cv2.FONT_HERSHEY_SIMPLEX, 0.7, YELLOW_COLOR, 2)
            # cv2.putText(frame, "Diff EAR: {:.2f}".format(np.abs(leftEAR - rightEAR)), (460, 80),
            #             cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            # Show the frame
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1) & 0xFF

            # If the `Esc` key was pressed, break from the loop
            if key == 27:
                break
        except Exception:
            speak("please reopen the application")
            exit()
            #dead = True
            #cv2.destroyAllWindows()
            #vid.release()
            exit()

    # Do a bit of cleanup
    cv2.destroyAllWindows()
    vid.release()


def advance():
    global user
    global said
    global listen
    global copy1
    openai.api_key = os.getenv(
        "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")  # incase of problem change key value in api_requester
    model_engine = "text-davinci-003"
    speak("advance mode activated")
    while True:
        try:
            prompt = takecommand()
            copy1 = 1
            tprompt = prompt.split()
            lprompt = len(tprompt)
            if "deactivate" in prompt:
                speak("deactivating... advance mode")
                copy1=0#copy work
                break
            elif prompt != "" and lprompt > 1:
                completion = openai.Completion.create(
                    model=model_engine,
                    prompt=prompt,
                    max_tokens=1024,
                    n=1,
                    stop=None,
                    temperature=0.5,
                )
                response = completion.choices[0].text
                print(response)#zz
                if "program" in prompt or "code" in prompt:
                    copy1=0
                    #time.sleep(2)
                    said=response
                    #copy1=1
                else:
                    copy1=0
                    ll = response.split()
                    l11 = []
                    c = 0
                    s = ""
                    for lll in ll:
                        c += 1
                        if c==1 and "." in lll and len(lll)<=2:
                            l11.append(lll)
                            l11.append(" ")
                        elif "." in lll:
                            l11.append(lll+"\n\n")
                            c=0
                        if c<=8 and ("." not in lll):
                            l11.append(lll + " ")
                        if c > 8 :#sethu
                            l11.append("\n   ")
                            c = 0
                    for l in l11:
                        s += l

                    said = s
                    #copy1=1
                #speak(response)
        except Exception:
            print("try again...")#zz
            said="try again..."


def TaskExecution():
        global threadui
        global said
        global user
        global listen
        global dead
        global drag
        global mouse_thread_flag
        global total_error
        print('Natasha :: version: VAPC-1')
        speak("i am Natasha ,..,    version  V A P C 1")
        print('CREATED BY:\n* SP.SETHULAKSHMANAN')
        said='Natasha :: version: VAPC-1'+'\nCREATED BY:\n* SETHULAKSHMANAN SP\n'#* SANJITH KUMAR M\n* VIGRAM K M\n* YOKESH SHAMLIN SHINANTH JS'
        speak('I  AM  ONLINE')


        #wishme() #zz
        try:
            while True:
                try:
                    print('say my name to wake me up')  # zz
                    listen = 'say my name to wake me up'
                    wake_up = takecommand()
                    if "bye" in wake_up or 'go offline' in wake_up or 'stop listening' in wake_up:
                        print('going offline')
                        said = 'going offline'
                        speak('going offline')
                        threadui = 1
                        dead = True
                        exit()

                    elif wake_up == "":
                        continue
                    # mouse controlds
                    # elif "speed" in wake_up:
                    # drag = 50
                    # elif "slow" in wake_up:
                    # drag = 10
                    elif "maximize" in wake_up:
                        maximize_window()
                        continue
                    elif "minimise" in wake_up:
                        minimize_window()
                        continue
                    elif "close" in wake_up:
                        close_window()
                        continue
                    elif "switch tab" in wake_up or "which tab" in wake_up or "pitch tab" in wake_up or "twitch tab" in wake_up:
                        pyautogui.keyDown("ctrl")
                        pyautogui.press("tab")
                        pyautogui.keyUp("ctrl")
                        speak("switched")
                        continue
                    elif "switch" in wake_up or "which" in wake_up or "pitch" in wake_up or "twitch" in wake_up:
                        pyautogui.keyDown("alt")
                        pyautogui.press("tab")
                        time.sleep(1)
                        pyautogui.press("left")
                        pyautogui.press("left")
                        pyautogui.keyUp("alt")
                        speak("switched")
                        continue
                    elif "play" in wake_up or "pause" in wake_up or "pass" in wake_up:
                        pyautogui.press("space")
                        continue
                    elif "select" in wake_up or "press" in wake_up:
                        pyautogui.press("enter")
                        continue
                    elif "copy" in wake_up:
                        pyautogui.keyDown("ctrl")
                        pyautogui.press("c")
                        pyautogui.keyUp("ctrl")
                        continue
                    elif "paste" in wake_up:
                        pyautogui.keyDown("ctrl")
                        pyautogui.press("v")
                        pyautogui.keyUp("ctrl")
                        continue
                    elif "delete" in wake_up:
                        pyautogui.press("delete")
                        pyautogui.keyUp("delete")
                        continue
                    elif "select all" in wake_up:
                        pyautogui.keyDown("ctrl")
                        pyautogui.press("a")
                        pyautogui.keyUp("ctrl")
                        continue
                    elif "right click" in wake_up or "right" in wake_up:
                        right_click()
                        continue
                    elif "left click" in wake_up or "left" in wake_up or "click" in wake_up:
                        left_click()
                        continue
                    elif "double click" in wake_up:
                        double_click()
                        continue
                    elif "hold" in wake_up or "drag" in wake_up:
                        hold()
                        continue
                    elif "release" in wake_up:
                        release()
                        continue
                    elif "advanced mode" in wake_up or "advance mode" in wake_up:
                        advance()
                        speak("call my name,..., when you need my help")
                        continue
                    elif "interactive mode" in wake_up:
                        theraphy()
                        speak("call my name,..., when you need my help")
                        continue
                    elif "keyboard" in wake_up:
                        type()
                        speak("call my name,..., when you need my help")
                        continue
                    elif ("terminate mouse" in wake_up or "terminate most" in wake_up or "deactivate mouse" in wake_up or "deactivate most" in wake_up or "deactivate mouth" in wake_up) and dead != True:
                        if mouse_thread_flag == 1:
                            mouse_thread_flag = 0
                            dead = True
                            speak("deactivated the mouse control")
                            speak("call my name,..., when you need my help")
                            continue
                        else:
                            speak("you have not activated mouse functionalities")
                            continue
                    elif "deactivate mouse" not in wake_up and (
                            "activate mouse" in wake_up or "activate most" in wake_up or "activate mouth" in wake_up):
                        if mouse_thread_flag == 0:
                            mouse_thread_flag = 1
                            dead = False
                            thread1 = threading.Thread(target=mouse_cursor_control)
                            # thread2 = threading.Thread(target=TaskExecution)
                            # thread2.start()
                            thread1.start()
                            speak("call my name,..., when you need my help")
                            speak("intiating mouse control")
                            continue
                            # mouse_cursor_control()
                        else:
                            speak("this feature is already activated ")
                            continue
                    elif "emergency" in wake_up:
                        # Fetch the service account key JSON file contents
                        cred = credentials.Certificate(r"natasha-bd631-firebase-adminsdk-htd4a-b09ad6e75d.json")

                        # Initialize the app with a service account, granting admin privileges
                        firebase_admin.initialize_app(cred, {
                            'databaseURL': 'https://natasha-bd631-default-rtdb.firebaseio.com/'
                        })
                        ref = db.reference('data')
                        ref.set('true')
                        said = "don't worry the emergency message is sent \nto the emergency number given in the NAT app" + "\n" + "they will rescue you soon..."
                        speak(
                            "don't  worry  the emergency message  is  sent  to   the  emergency number  given in the  NAT  app")
                        speak("they will rescue you soon...")
                        continue


                    elif 'natasha' in wake_up or "wake up" in wake_up or "get up" in wake_up:
                        while True:
                            speak("listening")
                            query = takecommand()

                            if 'the time' in query:
                                stime = datetime.datetime.now().strftime("%H:%M:%S")
                                speak("current time is ")
                                print(stime)
                                said = stime
                                speak(stime)
                                speak("call my name,..., when you need my help")
                                break

                            elif "your father" in query or "your sister" in query or "your brother" in query or "your mother" in query:
                                speak("i don't have any hind of relationship")
                                speak("call my name,..., when you need my help")
                                break

                            elif 'your name' in query or 'who are you' in query or 'introduce' in query or "you do" in query:
                                speak('''i am natasha  ,...., artificial intellegence ,....., intellegent  software  
                                            under  development 
                                             ,..., and  i  was  created  by,..., saythu lakshmanan ,..,''')
                                speak(''' purpose of creating me   is  to make humans work  easier. I can open  applications  on 
                                            the desktop folder , 
                                            play musics  , search in youtube ,.., as well as chrome ,..,
                                            i can take   screen shot ,  tell  jokes,  i  also  have a  snake  game  in built , and  more ,...., 
                                            to   know  my  features  refer  manual.  ''')
                                speak("call my name,..., when you need my help")
                                break

                            # elif 'joke' in query:
                            # a = open("jokes", 'r')
                            # b = a.readlines()
                            # c = random.randint(0, len(b) - 1)
                            # speak(b[c])

                            elif "tell me motivation quotes" in query or 'motivate me' in query:
                                stMsgs = [
                                    'Failure will never overtake me if my determination to succeed is strong enough',
                                    'The past cannot be changed. The future is yet in your power',
                                    'Only I can change my life. No one can do it for me',
                                    "Change your life today. Don't gamble on the future, act now, without delay",
                                    '''Do the difficult things while they are easy and do the great things while they are 
                                          small. A journey of a thousand miles must begin with a single step''',
                                    'Either I will find a way, or I will make one',
                                    'Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time',
                                    'Good, better, best. Never let it rest. Till your good is better and your better is best']
                                highMsgs = ['Dont worry dude,every hard time comes to an end']
                                speak(random.choice(stMsgs))
                                speak('I think this Motivated You sir ... if Not')
                                speak(random.choice(highMsgs))
                                speak("call my name,..., when you need my help")
                                break


                            elif "stop listening" in query or 'stop' in query:
                                winsound.Beep(32767, 500)
                                speak("call my name,..., when you need my help")
                                break

                            elif 'write note' in query or 'take note' in query or 'take notes' in query or 'write notes' in query:
                                print("what should i write?")  # zz
                                said = "what should i write?"
                                speak("what should i write ?")
                                notes = takerawcommand().lower()
                                file = open('notes.txt', 'a+')
                                print('sir should i include date and time?')  # zz
                                said = 'should i include date and time?'
                                speak('should i include date and time?')
                                ans = takerawcommand().lower()
                                if 'yes' in ans or 'sure' in ans or 'okay' in ans or 'ok' in ans:
                                    speak('adding date and time')
                                    strtime = datetime.datetime.now().strftime("%H:%M:%S")
                                    file.write(strtime)
                                    file.write(':-')
                                    file.write(notes + '\n')
                                    speak('done taking notes sir')
                                else:
                                    file.write(notes + '\n')
                                    print('done taking notes sir')
                                    said = 'done taking notes '
                                    speak('done taking notes')
                                speak("call my name,..., when you need my help")
                                break

                            elif 'show note' in query:
                                try:
                                    file = open('notes.txt', 'r')
                                    speak("showing notes")
                                    txt = file.read()
                                    print(txt)  # zz
                                    said = txt
                                    speak(txt)
                                    speak("call my name,..., when you need my help")
                                    break
                                except Exception:
                                    speak("sorry  sir   there   is   no   notes   found")
                                    break

                            elif 'search in youtube' in query:
                                speak('what should i search')
                                search_term = takecommand()
                                speak("here we go to youtube")
                                webbrowser.open('https://www.youtube.com/results?search_query=' + search_term)
                                speak("call my name, when you need my help")
                                break

                            elif 'cpu' in query or 'my system' in query or 'this pc' in query:
                                speak('analyzing   system   data')
                                system()
                                system2()
                                cpu()
                                speak("call my name,..., when you need my help")
                                break

                            elif 'joke' in query:
                                joke()
                                speak("call my name,..., when you need my help")
                                break

                            elif 'calculate' in query:
                                try:
                                    indx = query.lower().split().index('calculate')
                                    query = query.split()[indx + 1:]
                                    res = client.query(''.join(query))
                                    answer = next(res.results).text
                                    print('the answer is :' + answer)  # zz
                                    said = 'the answer is :' + answer
                                    speak('the answer is ' + answer)
                                    speak("call my name,..., when you need my help")
                                    break
                                except Exception:
                                    speak("sorry i am unable to do this problem,..., command failed")
                                    speak("call my name,..., when you need my help")
                                    break


                            elif 'game' in query:
                                print("you have to add")
                            elif "search in google" in query:
                                speak('what should i search?')
                                searchterm = takerawcommand()
                                speak('here we go to google')
                                webbrowser.open(
                                    'https://www.google.com/search?q=' + searchterm)  # c8ef00a6dad54b4daef5085a2015aaaa
                                speak("call my name,..., when you need my help")
                                break

                            elif "search in" in query:
                                speak(''' sir  i  can  search  in  youtube  and  google  ,..., 
                                            if you  want  to   know   about anything via audio,...,  just say the word or the name ''')
                                speak("call my name ,.., when you need my help")
                                break

                            elif query == "":
                                continue

                            elif 'remember that' in query:
                                print('what should i remember')
                                said = 'what should i remember'
                                speak('what should i remember ')
                                memory = takerawcommand()
                                speak('you asked me to remember that ' + memory)
                                remember = open('memory.txt', 'a+')
                                remember.write(memory + '\n')
                                remember.close()
                                speak("call my name,..., when you need my help")
                                break

                            elif 'Wi-Fi' in query or 'password' in query:
                                # first we will import the subprocess module

                                # now we will store the profiles data in "data" variable by
                                # running the 1st cmd command using subprocess.check_output
                                data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode(
                                    'utf-8').split(
                                    '\n')

                                # now we will store the profile by converting them to list
                                profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

                                # using for loop in python we are checking and printing the wifi
                                # passwords if they are available using the 2nd cmd command
                                for i in profiles:
                                    # running the 2nd cmd command to check passwords
                                    results = subprocess.check_output(
                                        ['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode(
                                        'utf-8').split('\n')
                                    # storing passwords after converting them to list
                                    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                                    # printing the profiles(wifi name) with their passwords using
                                    # try and except method
                                    try:
                                        print("{:<30}|  {:<}".format(i, results[0]))
                                        said = "{:<30}|  {:<}".format(i, results[0])
                                    except Exception:
                                        print("{:<30}|  {:<}".format(i, ""))
                                        said = "{:<30}|  {:<}".format(i, "")
                                time.sleep(5)
                                speak("call my name,..., when you need my help")
                                break


                            elif 'do you remember anything' in query:
                                try:
                                    remember = open('memory.txt', 'r')
                                    speak('you asked me to remember that' + remember.read())
                                    speak("call my name,..., when you need my help")
                                    break
                                except Exception:
                                    print("sorry sir i didn't remember anything")
                                    said = "sorry i didn't remember anything"
                                    speak("sorry   i   don't  remember  anything")
                                    break

                            elif 'where is' in query:
                                query = query.replace("where is", '')
                                location = query
                                speak('user asked to locate' + location)
                                webbrowser.open("https://www.google.com/maps/place/" + location)
                                speak("call my name,..., when you need my help")
                                break

                            elif 'restart' in query:
                                speak("Do you want to restart your computer sir?")
                                while True:
                                    command = takecommand()
                                    if "no" in command:
                                        speak("Thank u sir I will not restart the computer")
                                        break
                                    if "yes" in command:
                                        # Shutting down
                                        command.Speak("restarting the computer")
                                        os.system("shutdown /s /t 1")
                                        break
                                    speak("Say that again sir")
                                # os.system("shutdown /r /t 1")
                                # speak('restarting operating system')
                                # break

                            elif 'shutdown' in query:
                                while True:
                                    command = takecommand()
                                    if "no" in command:
                                        speak("Thank u sir I will not shut down the computer")
                                        break
                                    if "yes" in command:
                                        # Shutting down
                                        command.speak("Shutting the computer")
                                        os.system("shutdown /s /t 30")
                                        break
                                    speak("Say that again sir")

                                # os.system("shutdown /s /t 1")
                                # speak('shutting down operating system')
                                # break

                            elif 'open google' in query:
                                speak("opening google")
                                webbrowser.open("google.com")
                                speak("call my name,..., when you need my help")
                                break

                            elif 'open youtube' in query:
                                speak("opening youtube")
                                webbrowser.open("youtube.com")
                                speak("call my name,..., when you need my help")
                                break

                            elif 'open' in query:
                                query = query.replace('open ', '')
                                # speak('which application should i have to open')
                                # ans = takerawcommand()
                                try:
                                    pyautogui.keyDown("win")
                                    time.sleep(1)
                                    pyautogui.press("s")
                                    time.sleep(0.5)
                                    pyautogui.keyUp("win")

                                    # time.sleep(1)
                                    #  pyautogui.keyUp("s")
                                    # explorer = "explorer.exe"
                                    # for proc in psutil.process_iter(['name']):
                                    #     if proc.info['name'] == explorer:
                                    #         subprocess.run('explorer.exe search-ms:', shell=True)
                                    #         break
                                    # else:
                                    #     subprocess.run('explorer.exe search-ms:', shell=True)
                                    time.sleep(1)
                                    pyautogui.typewrite(query)
                                    time.sleep(0.5)
                                    pyautogui.press('down')
                                    pyautogui.press('down')
                                    pyautogui.press('up')
                                    pyautogui.press('up')

                                    time.sleep(0.5)
                                    speak("opening " + query)
                                    pyautogui.press("enter")
                                    # os.startfile(query)
                                except Exception:
                                    speak("sorry sir i cannot find " + str(query) + " in desktop ")
                                    print("add the exe file to the desktop folder")
                                    said = "add the exe file to the desktop folder"
                                    os.startfile("")
                                    speak("add the exe file to the desktop folder")

                                speak("call my name,..., when you need my help")
                                break


                            # """elif "screenshot" in query:
                            # screenshot()
                            # speak('done sir ,check it on desktop')
                            # speak("call my name,..., when you need my help")
                            # break"""

                            elif 'play music' in query or 'song' in query or 'music' in query:
                                current_directory = os.getcwd()
                                final_directory = os.path.join(current_directory, r'natasha musics')
                                if not os.path.exists(final_directory):
                                    speak(
                                        'i   have ,..., created  a   empty    music   file    for  you,..,  named  natasha musics')
                                    os.makedirs(final_directory)
                                    os.startfile(final_directory)
                                    speak(
                                        "you have    to  add    musics    to     this    file    to  ,.., process  this  command ")
                                    speak("call my name,..., when you need my help")
                                    break
                                musicdir = "natasha musics"
                                songs = os.listdir(musicdir)
                                a = len(songs)
                                if a == 0:
                                    speak('there no songs   in   natasha musics    file    to   play')
                                    os.startfile(os.path.join(musicdir))
                                    speak('add  some songs  to this  folder     natasha   musics')
                                    print('natasha musics')
                                    said = 'natasha musics'
                                    speak("call my name,..., when you need my help")
                                    break
                                else:
                                    pass
                                speak("in this file there are  " + str(a) + " number of songs")
                                print(str(a) + " number of songs")  # zz
                                said = str(a) + " number of songs"
                                speak('so what number should i have to play')
                                print(
                                    'say the number with the word  number EXAMPLE: number 2 ,number 4 .\nIf you want me to choose the number say you choose or your wish or random')  # zz
                                said = str(
                                    a) + " number of songs" + "\n" + 'say the number with the word  number EXAMPLE: number 2 ,number 4 .\nIf you want me to choose the number say you choose or your wish or random'
                                speak(
                                    'select a number... and please say that with the word  number for  example  like   number 2 ,..., or ,...,if you want me to choose  the number,..., say,..., you choose ,..., or say,... your wish,...., or say random')
                                ans = takerawcommand().lower()

                                if 'number' in ans:
                                    try:
                                        no = int(ans.replace('number', ''))
                                        if no <= a:
                                            nos = int(no)
                                            speak("okay sir")
                                            os.startfile(os.path.join(musicdir, songs[nos]))
                                            speak("call my name,..., when you need my help")
                                            break
                                        elif no > a:
                                            speak('the number you have chosen ,..,  is out of range')
                                            print('chosen number is out of range')
                                            said = 'chosen number is out of range'
                                            speak("call my name,..., when you need my help")
                                            break

                                        else:
                                            speak("sorry sir your command is not in the right format")
                                            speak("so music cannot be played")
                                            speak(
                                                "but if you command me to play music of,..., my wish .   i can do that ")
                                            speak("waiting for you command")
                                            ans = takerawcommand().lower()
                                            if ans == '':
                                                speak(
                                                    "i did not get any input from you therefore ,canceling music command")
                                                speak("call my name,..., when you need my help")
                                                break

                                            if 'random' or 'you choose' or 'your wish' in ans:
                                                no = random.randint(0, len(songs) - 1)
                                                speak(" playing music of my wish, i hope you like it")
                                                os.startfile(os.path.join(musicdir, songs[no]))
                                                speak("call my name,..., when you need my help")
                                                break
                                            else:
                                                speak(
                                                    "i did not get any correct input from you therefore ,canceling music command")
                                                speak("call my name,..., when you need my help")
                                                break
                                    except Exception:
                                        speak('please give the input in correct format ,.., canceling music command')
                                        speak("call my name,..., when you need my help")
                                        break
                                elif 'random' in ans or 'you choose' in ans or 'your wish' in ans:
                                    no = random.randint(0, len(songs) - 1)
                                    speak(" playing music of my wish, i hope you like it")
                                    # print('2')
                                    os.startfile(os.path.join(musicdir, songs[no]))
                                    speak("call my name,..., when you need my help")
                                    break
                                else:
                                    speak("i did not get any input from you therefore ,canceling music command")
                                    speak("call my name,..., when you need my help")
                                    break

                            elif 'play video' in query or 'video' in query:
                                current_directory = os.getcwd()
                                final_directory = os.path.join(current_directory, r'natasha videos')
                                if not os.path.exists(final_directory):
                                    speak(
                                        'i   have ,..., created  a   empty    video   file    for  you,..,  named  natasha videos')
                                    os.makedirs(final_directory)
                                    os.startfile(final_directory)
                                    speak(
                                        "you have    to  add    musics    to     this    file    to  ,.., process  this  command ")
                                    speak("call my name,..., when you need my help")
                                    break
                                videodir = "natasha videos"
                                videos = os.listdir(videodir)
                                a = len(videos)
                                if a == 0:
                                    speak('there no videos   in   natasha videos    file    to   play')
                                    os.startfile(os.path.join(videodir))
                                    speak('add  some videos  to this  folder     natasha   videos')
                                    print('natasha videos')
                                    said = 'natasha videos'
                                    speak("call my name,..., when you need my help")
                                    break
                                else:
                                    pass
                                speak("in this file there are  " + str(a) + "  number of videos")
                                print(str(a) + "  number of videos")
                                said = str(a) + "  number of videos"
                                speak('so what number should i have to play')
                                print(
                                    'say the number with the word  number EXAMPLE: number 2 ,number 4 .\nIf you want me to choose the number say you choose or your wish or random')
                                said = str(
                                    a) + "  number of videos" + "\n" + 'say the number with the word  number EXAMPLE: number 2 ,number 4 .\nIf you want me to choose the number say you choose or your wish or random'
                                speak(
                                    'select a number... and please say that with the word  number for  example  like   number 21 ,..., or ,...,if you want me to choose  the number,..., say,..., you choose ,..., or say,... your wish,...., or say random')
                                ans = takerawcommand().lower()

                                if 'number' in ans:
                                    try:
                                        no = int(ans.replace('number', ''))
                                        if no <= a:
                                            nos = int(no)
                                            speak("okay sir")
                                            os.startfile(os.path.join(videodir, videos[nos]))
                                            speak("call my name,..., when you need my help")
                                            break
                                        elif no > a:
                                            speak('the number you have chosen ,..,  is out of range')
                                            print('chosen number is out of range')  # zz
                                            said = 'chosen number is out of range'
                                            speak("call my name,..., when you need my help")
                                            break

                                        else:
                                            speak("sorry sir your command is not in the right format")
                                            speak("so  video  cannot be played")
                                            speak(
                                                "but  if  you  command  me  to  play  video  of,..., my wish .   i  can  do  that ")
                                            speak("waiting for your  command")
                                            ans = takerawcommand().lower()
                                            if ans == '':
                                                speak(
                                                    "i did not get any input from you therefore ,canceling video command")
                                                speak("call my name,..., when you need my help")
                                                break

                                            if 'random' or 'you choose' or 'your wish' in ans:
                                                no = random.randint(0, len(videos) - 1)
                                                speak(" playing video of my wish, i hope you like it")
                                                os.startfile(os.path.join(videodir, videos[no]))
                                                speak("call my name,..., when you need my help")
                                                break
                                            else:
                                                speak(
                                                    "i did not get any correct input from you therefore ,canceling video command")
                                                speak("call my name,..., when you need my help")
                                                break
                                    except Exception:
                                        speak('please give the input in correct format ,.., canceling video command')
                                        speak("call my name,..., when you need my help")
                                        break

                                elif 'random' in ans or 'you choose' in ans or 'your wish' in ans:
                                    no = random.randint(0, len(videos) - 1)
                                    speak(" playing video of my wish, i hope you like it")
                                    # print('2')
                                    os.startfile(os.path.join(videodir, videos[no]))
                                    speak("call my name,..., when you need my help")
                                    break

                                else:
                                    speak("i did not get any input from you therefore ,canceling video command")
                                    speak("call my name,..., when you need my help")
                                    break

                            elif 'go offline' in query or 'bye' in query:
                                speak('going offline sir')
                                speak('i  hope  you   like   my  service')
                                threadui = 1
                                dead = True
                                exit()

                            elif 'new file' in query:
                                current_directory = os.getcwd()
                                speak('what   should   i   name  ')
                                a = takerawcommand()
                                if a == '':
                                    final_directory = os.path.join(current_directory, r'new file')
                                    speak("sir  i  am  giving  name for the file as ,..,  new file")
                                    if os.path.exists(final_directory):
                                        speak(
                                            ' sir    please    rename   the  files   named  by  me ,.., there   is  already  a folder  on this  name')
                                        speak("call my name,..., when you need my help")
                                        break
                                    if not os.path.exists(final_directory):
                                        os.makedirs(final_directory)
                                        speak(' sir  i  have created   the   file  named ,.., rename it')
                                        speak("call my name,..., when you need my help")
                                        break

                                else:
                                    final_directory = os.path.join(current_directory, a)

                                    if os.path.exists(final_directory):
                                        speak('there   is  already  a folder  on this  name')
                                        speak("call my name,..., when you need my help")
                                        break
                                    if not os.path.exists(final_directory):
                                        os.makedirs(final_directory)
                                        speak('i have  created  a new  file in desktop  named' + str(a))
                                        speak("call my name,..., when you need my help")
                                        break
                            elif "advanced mode" in query or "advance mode" in query:
                                advance()
                                speak("call my name,..., when you need my help")
                                break

                            elif "interactive mode" in query:
                                theraphy()
                                speak("call my name,..., when you need my help")
                                break
                            elif "keyboard" in query:
                                type()
                                speak("call my name,..., when you need my help")
                                break
                            elif ("terminate mouse" in query or "terminate most" in query or "deactivate mouse" in query or "deactivate most" in query or "deactivate mouth" in query) and dead != True:
                                if mouse_thread_flag == 1:
                                    mouse_thread_flag = 0
                                    dead = True
                                    speak("deactivated the mouse control")
                                    speak("call my name,..., when you need my help")
                                    break
                                else:
                                    speak("you have not activated mouse functionalities")
                                    break
                            elif "deactivate mouse" not in query and (
                                    "activate mouse" in query or "activate most" in query or "activate mouth" in query):
                                if mouse_thread_flag == 0:
                                    mouse_thread_flag = 1
                                    dead = False
                                    thread1 = threading.Thread(target=mouse_cursor_control)
                                    # thread2 = threading.Thread(target=TaskExecution)
                                    # thread2.start()
                                    thread1.start()
                                    speak("call my name,..., when you need my help")
                                    speak("intiating mouse control")
                                    break
                                    # mouse_cursor_control()
                                else:
                                    speak("this feature is already activated ")
                                    break
                            elif "emergency" in query:
                                # Fetch the service account key JSON file contents
                                cred = credentials.Certificate(r"natasha-bd631-firebase-adminsdk-htd4a-b09ad6e75d.json")

                                # Initialize the app with a service account, granting admin privileges
                                firebase_admin.initialize_app(cred, {
                                    'databaseURL': 'https://natasha-bd631-default-rtdb.firebaseio.com/'
                                })
                                ref = db.reference('data')
                                ref.set('true')
                                said = "don't worry the emergency message is sent \nto the emergency number given in the NAT app" + "\n" + "they will rescue you soon..."
                                speak(
                                    "don't  worry  the emergency message  is  sent  to   the  emergency number  given in the  NAT  app")
                                speak("they will rescue you soon...")
                                break
                            elif "maximize" in query:
                                maximize_window()
                                break
                            elif "minimise" in query:
                                minimize_window()
                                break
                            elif "close" in query:
                                close_window()
                                break
                            else:
                                continue
                            # else:
                            """query = query
                                try:
                                    try:
                                        res = client.query(query)
                                        results = next(res.results).text
                                        print(results)
                                        speak(results)
                                        speak("         call my name,..., when you need my help")
                                        break

                                    except:
                                        try:
                                            speak('i cannot   figure  it  out')
                                            speak("do you want to get information about " + query)
                                            d = takecommand()
                                            if "yes" in d or 'ya' in d or 'yeah' in d:
                                                print('Searching...')
                                                speak('fetching ,.., information')
                                                results = wikipedia.summary(query, sentences=2)
                                                speak('Got it.')
                                                speak('WIKIPEDIA says - ')
                                                print(str(results))
                                                speak(results)
                                                speak("call my name,..., when you need my help")
                                                break
                                            else:
                                                speak(" canceling search process ,your command is taken as no ")
                                                speak("call my name,..., when you need my help")
                                                break

                                        except Exception:
                                            print("no results found")
                                            speak('sorry sir, i do not know much about it ')
                                            speak("call my name,..., when you need my help")
                                            break
                                except Exception:
                                    print("no results found")
                                    speak('sorry sir, i do not know much about it ')
                                    speak("call my name,..., when you need my help")
                                    break
                            """





                    else:
                        continue

                except Exception:
                    print("try again...")

                    # TaskExecution()
        except Exception:
            speak("Sorry for the inconvenience reopen the application")
            mouse_thread_flag = 0
            dead = True
            total_error = True
            time.sleep((2))
            exit()



if (__name__=="__main__"):
    thread3=threading.Thread(target=UI)
    thread3.start()
    TaskExecution()