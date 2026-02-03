
import time
import os


import speech_recognition as sr
import webbrowser
import pyttsx3
import pyaudio

# recognizer = sr.Recognizer()

engine = pyttsx3.init()

def speck(text):
    engine.say(text)
    engine.runAndWait()
# speck()
def proccescommad(c):
    if "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")

    elif "off the pc" in c.lower():
        engine.say("yes sir omnitrix shut dawon the pc see you later")
        engine.runAndWait()
        
        os.system("shutdown /s /t 0")
    elif "open discord" in c.lower():
        webbrowser.open("https://discord.com/")

    elif"open facebook"in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif"open code" in c.lower():
        webbrowser.Chrome()

    elif  "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")

    elif  "open wikipedia" in c.lower():
        webbrowser.open("https://www.wikipedia.org")
    elif "open skyfall" in c.lower():
        webbrowser.open("https://youtu.be/DeumyOzKqgI?si=sLs6agau5FU-cgd4")
    elif "open my hit song" in c.lower():
        webbrowser.open("https://youtu.be/gr45CCvL2i4?si=h4uWlS6Yd2faNIqM")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
    elif"open moviebox" in c.lower():
        webbrowser.open("https://www.google.com/search?client=firefox-b-d&q=moive+box")
    else:
        engine.say(f"Sorry sir {c.lower()} is not find in the data")
        engine.runAndWait()

if __name__ == "__main__":
    
    speck("Iam yor assistant Sir i am  omnitrix what can i help you")
    while True:

        r = sr.Recognizer()
        # listen for the wake word omnitrix

        print("listing.......")
        # recognize speech using goole
        try:
            with sr.Microphone() as source: 

                print("recogniging.......")

                r.adjust_for_ambient_noise(source)   # noise fix

                audio = r.listen(source, timeout=2, phrase_time_limit=2)
                # time.sleep(1)
                
            word = r.recognize_google(audio)   # spelling fix + same variab
            print(word)


            if (word.lower() in "omnitrix"):
                engine.say(("yes sir"))
                engine.runAndWait
                
                
                # time.sleep(1)


                with sr.Microphone() as source:

                    print("omnitrix is active....")

                    r.adjust_for_ambient_noise(source)   # noise fix

                    audio = r.listen(source, timeout=2, phrase_time_limit=2)

                    commad = r.recognize_google(audio)
                    print(commad)
                    engine.say(("yes sir"+commad))
                    engine.runAndWait()
                    
                    
                    
                                        
                    engine.say(f"are you ready sir for {commad}")
                    engine.runAndWait
                    
                    time.sleep(2)


                    proccescommad(commad)




        except Exception as e:

            print(f"omnitrix don't understend  {0}".format(e))


