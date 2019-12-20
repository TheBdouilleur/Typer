import speech_recognition as sr
from pyautogui import typewrite
import logger
text = ""


def listen(text):
    text = text
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listening bro:")
        typewrite('Listening...', interval=0.05)
        audio = r.listen(source)
        text = r.recognize_google(audio, 'fr-FR')
        return text

def format(text):
    text = text
    checked = False
    typewrite("Formatting...", interval=0.05)
    while not checked:
        # 1. Special characters
        if "à" in text:
            text = text.replace("à", "a")
        elif "â" in text:
            text = text.replace("â", "a")
        elif "é" in text:
            text = text.replace("é", "e")
        elif "è" in text:
            text = text.replace("è", "e")
        elif "ê" in text:
            text = text.replace("ê", "e")
        elif "î" in text:
            text = text.replace("î", "i")
        elif "ô" in text:
            text = text.replace("ô", "o")
        elif "ú" in text:
            text = text.replace("ú", "u")
        elif "û" in text:
            text = text.replace("û", "u")
        elif "ç" in text:
            text = text.replace("ç", "c")
    
        # 2. Punctuation
        elif "virgule" in text:
            text = text.replace("virgule", ", ")
        elif "point" in text:
           text = text.replace("point", ". ")
        elif "point d'interrogation" in text:
            text = text.replace("point d'interrogation", "? ")
        elif "point d'exclamation" in text:
            text = text.replace("point d'exclamation", "! ")
        elif "a la ligne" in text:
            text = text.replace("a la ligne", "\n")
        else:
            checked = True
    return(text)


if __name__ == "__main__":
    logger.log_start()
    try:
        text = listen(text)
        print("You said(raw): {}".format(text))
        text = format(text)
        print("You said(refined): {}".format(text))
        typewrite(text, interval=0.05)
    except Exception as e:
        logger.log_exception(e)
        typewrite("Sorry... didn't work"+str(e), interval=0.05)

    