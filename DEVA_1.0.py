''' DEVA === desktop virtual assistant'''

import speech_recognition as sp_re
import  pyttsx3
import datetime 
import wikipedia as wiki
import pyautogui as pyat
import os 

falar=pyttsx3.init()  

def robor(robo):      # funçao que pega o que ta escrito ,depois transmite em saida de audio 
  falar.say(robo)    
  falar.runAndWait()

def ouvindo():   # função de ovir e converter em texto
    microfone = sp_re.Recognizer()

    with sp_re.Microphone() as source:
        microfone.adjust_for_ambient_noise(source) # recução de ruido
        print("ouvindo....")
        audio = microfone.listen(source) # Armazena o que foi dito em uma variavel
        
    try:
        frase = microfone.recognize_google(audio,language='pt-BR') # converte o audio em texto
        
    except sp_re.UnknownValueError:#Se nao reconheceu o padrao de fala, fala  a mensagem
        robor("Não entendi , pode repetir !")
        
    return frase


def pesquisa():
    procurar=comando.replace("procure por","")
    wiki.set_lang('pt')
    fala=wiki.summary(procurar,2)
    return robor(fala)


robor("olá , sou Deva , é um praser te conhecer , em poderia lhe ajudar ?")
comando=ouvindo() 
if "data" in comando :
    robor(datetime.date.today().strftime('%D'))    
elif "hora" in comando :    
    robor(datetime.datetime.now().strftime('%H : %M'))        
elif "pesquisar" in comando :
    os.getcwd()
    os.startfile('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe')
    datetime.sleep(1)
    

