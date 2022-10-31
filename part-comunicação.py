# variavel que recebe o tipo de idioma da confg
idioma = "pt-br"
falar = sx.init()
# saida e endrada de audio simples , modificaar posteriormente 
def fala (saida):
    falar.say(saida)
    falar.runAndWait()

def ouvir():
    microfone = sr.Recognizer()
    with sr.Microphone() as ruido:

        microfone.adjust_for_ambient_noise(ruido)
        print(".....")
        audio = microfone.listen(ruido)
    
    try:
    
        frase = microfone.recognize_google(audio,language=idioma)
        
    except sr.UnknownValueError:
        if idioma == "en":
            fala("Can you repeat !")
            
        elif idioma == "pt-br":
            fala("pode repetir !")
            
    
    return frase
