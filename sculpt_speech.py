import speech_recognition as sp_re
import  pyttsx3
import wikipedia as wiki


speak=pyttsx3.init()  
# funçao que pega o que ta escrito ,depois transmite em saida de audio 
def talking(robo):
  speak.say(robo)    
  speak.runAndWait()
  
# função de ovir e converter em texto
def listen():   
    microfone = sp_re.Recognizer()

    with sp_re.Microphone() as source:
        microfone.adjust_for_ambient_noise(source) # recução de ruido
        audio = microfone.listen(source) # Armazena o que foi dito em uma variavel
        
    try:
        frase = microfone.recognize_google(audio,language='pt-BR') # converte o audio em texto
        
    except sp_re.UnknownValueError:#Se nao reconheceu o padrao de fala, fala  a mensagem
        talking("Não entendi , pode repetir !")
        
    return frase


def check():
    comando = listen()
    procurar = comando.replace("procure por","")
    wiki.set_lang('pt')
    talk = wiki.summary(procurar,2)
    return talking(talk)
