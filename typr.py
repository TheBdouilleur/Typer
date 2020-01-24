import speech_recognition as sr
from pyautogui import typewrite
import logger
import requests
import json
import ssl
API_ENDPOINT = 'https://api.wit.ai/speech'
r = sr.Recognizer()
m = sr.Microphone()
 
def  listen():# generate str type var from micro input
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    with m as source:
        print("Listening...")
        #typewrite('Listening...')
        audio = r.listen(source)
        return audio
 
def recognizeWit(audio_sample): # recognize the text from the audio sample ( in AudioData format)
    print('Recognizing...')
    result = r.recognize_wit(audio_sample, 'K3UF6XMKHGPE26SO35I3QSWNSO3J7MMR')
    text = result.pop('_text')# '_text' is the text key in the 'result' dictionary returned by r.recognize_wit()
    return text
 
def recognizeHoundify(audio_sample):
    print('Recognizing...')
    text = r.recognize_houndify(audio_sample, 'wENbpy4XThJmkSO7u9SdXA==', '9HbD3CujTs-82oqGqUx3GQnu0yE_NXvTe_p6BbO_IfFY10xSgp1K71AJpQcqPwmyMAnF1z-PwTg8Eee7H8vPKA==')
    return text
 
def format(text):# format the text ( str format ) into a printable and natural-language-like text
    print("Formatting...")
    checked = False
    while not checked:# treatment of aliases ( ex special characters)
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
        elif "point d'interrogation" in text:
            text = text.replace("point d'interrogation", "? ")
        elif "point d'exclamation" in text:
            text = text.replace("point d'exclamation", "! ")
        elif "point" in text:
           text = text.replace("point", ". ")
        elif "a la ligne" in text:
            text = text.replace("a la ligne", "\n")
        #TODO. Add correcting support for capitals after punctuation marks
        else:
            checked = True
    return(text)
 
 
if __name__ == "__main__":
    logger.log_start()
    try:
        audio = listen()
        rawText = recognizeWit(audio)
        print("You said(raw): {}".format(rawText))
        fineText = format(rawText)
        print("You said(refined): {}".format(fineText))
        typewrite(fineText)
    except Exception as e:
        logger.log_exception(e)
        typewrite("Sorry... didn't work"+str(e))