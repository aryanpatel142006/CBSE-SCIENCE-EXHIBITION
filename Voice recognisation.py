import speech_recognition as sr
import time
import pyttsx3
import pyautogui

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

recognizer = sr.Recognizer()
microphone = sr.Microphone()


def speak(query):
    engine.say(query)
    engine.runAndWait()


def recognize_speech():
    with microphone as source:
        audio = recognizer.listen(source, phrase_time_limit=5)
    response = ""
    speak("Identifying speech..")
    try:
        response = recognizer.recognize_google(audio)
    except:
        response = "Error"
    return response


time.sleep(5)
speak("voice recognition systems are online, select your answers from option 1 2 3 or 4")
while True:
    speak("please say your answer")
    voice = recognize_speech().lower()
    print(voice)
    if 'option one' in voice or '1' in voice:
        speak('Option one')
        pyautogui.click(959, 1048)
        pyautogui.press("A")
        pyautogui.click(972, 861)
    elif '2' in voice or 'tu' in voice:
        speak('Option two')
        pyautogui.click(959, 1048)
        pyautogui.press("b")
        pyautogui.click(972, 861)
    elif 'option three' in voice or '3' in voice:
        speak('Option three')
        pyautogui.click(959, 1048)
        pyautogui.press("c")
        pyautogui.click(972, 861)
    elif 'option four' in voice or '4' in voice:
        speak('Option four')
        pyautogui.click(959, 1048)
        pyautogui.press("d")
        pyautogui.click(972, 861)
    elif 'read again' in voice:
        pyautogui.click(196, 740)
    elif 'quit' in voice or 'exit' in voice:
        speak('quitting quiz')
        pyautogui.click(958,785)

        break
    elif 'begin' in voice:
        pyautogui.click(972,861)
    else:
        speak('please speak again')
    time.sleep(1)