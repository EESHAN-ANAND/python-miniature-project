

import pyttsx3

if __name__ == '__main__':
    print("Welcome")
    engine = pyttsx3.init()


    # Set the voice and rate
    voices = engine.getProperty('voices')
    for voice in voices:
        if "english" in voice.name.lower() and "united states" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    
    while True:
        # Initialize the pyttsx3 engine
        

        x = input("Enter the words: ")

        
        if x=='q':
            # Convert the text to speech
            engine.say('Bye, will see you on the other side')
            
            # Play the speech
            engine.runAndWait()
            break
        else:
            # Convert the text to speech
            engine.say(x)
            
            # Play the speech
            engine.runAndWait()
