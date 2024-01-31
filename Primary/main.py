import speech_recognition as sr
import pyttsx3
import json

def load_personal_info():
    with open('Primary/Testdata/data.json', 'r') as file:
        data = json.load(file)
    return data

personal_info = load_personal_info()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")
    return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_answer(question):
    if "name" in question.lower():
        return "Your name is " + personal_info.get("name", "not known")
    elif "age" in question.lower():
        return "You are " + str(personal_info.get("age", "age not known")) + " years old"
    # Add more conditions for other types of questions
    else:
        return "I don't understand that question."

def main():
    try:
        while True:
            text = listen()
            if text:
                if "exit" in text.lower():  # Check if the spoken text contains the word 'exit'
                    speak("Exiting program. Goodbye!")
                    break 
                answer = get_answer(text)
                speak(answer)
            else:
                speak("I didn't catch that. Please say it again.")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    finally:
        print("Program terminated.")

if __name__ == "__main__":
    main()
