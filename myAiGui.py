import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import wikipedia
from tkinter import *

# Function to make Edith speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to greet the user based on the time of day
def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        update_text_output("Good Morning, Aditya!")
        speak("Good Morning, Aditya!")
    elif 12 <= hour < 18:
        update_text_output("Good Afternoon, Aditya!")
        speak("Good Afternoon, Aditya!")
    else:
        update_text_output("Good Evening, Aditya!")
        speak("Good Evening, Aditya!")
    update_text_output("I am Edith. How can I assist you today?")
    speak("I am Edith. How can I assist you today?")

# Function to take voice from the user
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        update_text_output("\nListening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        update_text_output("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        update_text_output(f"You said: {command}")
    except Exception as e:
        update_text_output("Sorry, I didn't catch that. Could you say that again please?")
        return "None"
    
    return command.lower()

# Function to update the text output
def update_text_output(text):
    text_output.insert(END, text + "\n")
    text_output.see(END)
    text_output.update_idletasks()

#function to execute commands
def execute_command():
    wish_me()
    while True:
        command = listen()
        
        if 'wikipedia' in command:
            update_text_output(f'Searching results for {command}')
            speak(f'Searching results for {command}')
            command = command.replace('wikipedia',' ')
            result = wikipedia.summary(command, sentences = 2)
            update_text_output('\nAccording to Wikipedia')
            speak('According to wikipedia')
            update_text_output(result)
            speak(result)

        elif 'time' in command or 'what is the time' in command:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            update_text_output(f"The time is {current_time}")
            speak(f"The time is {current_time}")
            
        elif 'your name' in command:
            update_text_output('I am Edith, your personal assistant. How may i assist you?')
            speak('I am Edith, your personal assistant. How may i assist you?')

        elif 'open youtube' in command:
            webbrowser.open("https://www.youtube.com")
            update_text_output("Opening YouTube")
            speak("Opening YouTube")

        elif 'open google' in command:
            webbrowser.open("https://www.google.com")
            update_text_output("Opening Google")
            speak("Opening Google")

        elif 'play music' in command:
            music_dir = 'D:\\Internship\\Hex_Softwares\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            update_text_output("Playing music")
            speak("Playing music")

        elif 'nice work' in command:
            update_text_output("Thank you, Aditya! I appreciate your kind words.")
            speak("Thank you, Aditya! I appreciate your kind words.")

        elif 'exit' in command or 'quit' in command:
            update_text_output("Goodbye, Aditya! Have a great day.")
            speak("Goodbye, Aditya! Have a great day.")
            break

        else:
            update_text_output("I'm sorry, I don't understand that command.")
            speak("I'm sorry, I don't understand that command.")

#function to start the voice assistant
def start_edith():
    execute_command()

#initializing the AI name
ai_name = 'Edith'

#initialize the tts engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[4].id)

root = Tk()
root.title("Edith - Voice Assistant")

label = Label(root, text="Edith - Your Personal Voice Assistant", font=("Arial", 14))
label.pack(pady=10)

#display the ouput 
text_output = Text(root, height=15, width=50)
text_output.pack(pady=10)

#button to start voice assistant
start_button = Button(root, text="Start Edith", command=start_edith, font=("Arial", 12))
start_button.pack(pady=10)

root.mainloop()
