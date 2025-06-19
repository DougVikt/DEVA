from speak import Speech # Importa a classe Speech do módulo speak
import speech_recognition as sr
import threading
import time
import socket

class Listener:
    def __init__(self, speech: Speech):
        # Inicializa a classe de escuta com Speech, idioma e caminho opcional para modelo offline.
        self.speech = speech
        self.language = speech.get_language()  # Obtém o idioma da classe Speech
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.is_listening = False
        self.use_offline = False
        self.offline_model_path = ""  # Caminho para modelo pocketsphinx
        self.listen_thread = None
        self.lock = threading.Lock()

    def check_internet(self):
        # Verifica se há conexão à internet.
        try:
            socket.create_connection(("www.google.com", 80), timeout=2)
            return True
        except OSError:
            return False

    def listen_background(self):
        # Captura áudio do microfone em segundo plano e processa com Speech.
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            while self.is_listening:
                try:
                    audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=5)
                    try:
                        if not self.use_offline and self.check_internet():
                            text = self.recognizer.recognize_google(audio, language=self.language)
                            # Se a conexão estiver ativa, usa o Google Speech Recognition
                        else:
                            self.use_offline = True
                            if self.offline_model_path and 'pt' in self.language:
                                text = self.recognizer.recognize_sphinx(
                                    audio,
                                    language='pt-BR',
                                    hmm=self.offline_model_path + '/model',
                                    lm=self.offline_model_path + '/lm.bin',
                                    dic=self.offline_model_path + '/dict.dic'
                                )
                            else:
                                text = self.recognizer.recognize_sphinx(audio, language='en-US')
                            # Se não houver conexão, usa o modelo offline pocketsphinx
                        with self.lock:
                            self.speech.speak(text)  # Usa a classe Speech para falar
                    except sr.UnknownValueError:
                       self.speech.speak("I didn't understand the audio.")
                    except sr.RequestError:
                        self.use_offline = True
                except sr.WaitTimeoutError:
                    pass  # Timeout silencioso
                time.sleep(0.1)  # Evita uso excessivo de CPU

    def start_listening(self):
        """Inicia a captura de áudio em segundo plano."""
        if not self.is_listening:
            self.is_listening = True
            self.use_offline = False if self.check_internet() else True
            self.listen_thread = threading.Thread(target=self.listen_background, daemon=True)
            self.listen_thread.start()
            print(f"Captura de áudio iniciada ({'offline' if self.use_offline else 'online'}).")

    def stop_listening(self):
        """Para a captura de áudio."""
        if self.is_listening:
            self.is_listening = False
            if self.listen_thread:
                self.listen_thread.join()
                self.listen_thread = None
            print("Captura de áudio parada.")