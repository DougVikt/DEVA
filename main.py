# Autor : DougVikt 

# Funções :
# um assistente virtual animada 
# que pode executar comandos de voz
# Reconhecimento de voz
# Conversão de texto para fala
# controle de software do computador
# editar arquivos em geral 
# salvar comandos no arquivo config


import time
import speech_recognition as sr
from functions.voice_recognition import Listener
from functions.speak import Speech



if __name__ == "__main__":

    # Cria uma instância da classe Speech 
    speech = Speech(language="pt-BR")  # ou "en-US", conforme necessário

    # Cria uma instância do Listener
    listener = Listener(speech)

    # Inicia a escuta em segundo plano
    print("Iniciando escuta. Fale algo no microfone...")
    listener.listening(start=True)

    try:
        # Mantem o programa rodando enquanto escuta
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Parando escuta...")
        listener.listening(start=False)