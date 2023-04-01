import speech_recognition as sp_re
import  pyttsx3
from googletrans import Translator 

class Audio :
    
    def __init__(self , language = 'en') -> None:
        self.init = pyttsx3.init() 
        self.lang = language
        self.transl = Translator()
    
    # definindo a linguagem da fala 
    def language(self):
        if self.lang == "pt":
            lang_audio = "pt-BR"
            message = "Desculpe ! não entendi , pode repetir ?" 
            
        elif self.lang == "es":
            lang_audio = "es-ES"
            message = "¡Lo siento! No entiendo, ¿puedes repetir?"   
        
        else :
            lang_audio = "en-US"
            message = "Sorry! I don't understand, can you repeat?" 
            
       
        return lang_audio,message
                
    # funçao que pega o que ta escrito ,depois transmite em saida de audio 
    def talking(self , robo):
        self.init.say(robo)    
        self.init.runAndWait()
    
    # função de ovir e converter em texto
    def listen(self):  
        lang_audio , message = self.language() 
        microfone = sp_re.Recognizer()

        with sp_re.Microphone() as source:
            microfone.adjust_for_ambient_noise(source) # recução de ruido
            audio = microfone.listen(source) # Armazena o que foi dito em uma variavel
            
        try:
            audio_txt = microfone.recognize_google(audio,language=lang_audio) # converte o audio em texto
            
        except sp_re.UnknownValueError:#Se nao reconheceu o padrao de fala, fala  a mensagem
            self.talking(message)
            
        return audio_txt

    # traduzindo todo o texto para um idioma so 
    def command(self):
        text_a = self.listen()
        lang_origin = self.transl.detect(text_a).lang
        comd = self.transl.translate(text_a , src=lang_origin , dest='en').text
        return comd