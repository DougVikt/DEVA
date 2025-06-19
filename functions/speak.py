import pyttsx3

class Speech:
    VALID_LANGUAGES = [ # Lista de idiomas válidos
        'pt-BR', 'en-US', 'es-ES', 'fr-FR', 'de-DE', 'it-IT', 
        'pt-br', 'en-us', 'es-es', 'fr-fr', 'de-de', 'it-it',
        'PT-BR', 'EN-US', 'ES-ES', 'FR-FR', 'DE-DE', 'IT-IT',
    ]
    def __init__(self, language='pt-BR'):
        # Verifica se o idioma é válido.
        if language not in self.VALID_LANGUAGES:
            raise ValueError(f"Invalid language: {language}")
        # Inicializa a classe com o idioma especificado.
        self.language = language.lower()  # Ex.: 'pt-BR', 'en-US', 'es-ES'
        self.vowels = {'a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'ã', 'õ', 'à', 'è', 'ì', 'ò', 'ù'}
        self.frame_duration = 120 if 'pt' in language else 100  # ms por quadro
        self.mouth_frames = []
        self.engine = pyttsx3.init()
        self.set_language()

    def set_language(self):
        # Configura a voz com base no idioma.
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if self.language in voice.id.lower():
                self.engine.setProperty('voice', voice.id)
                break
        self.engine.setProperty('rate', 160)  # Velocidade da fala
        self.engine.setProperty('volume', 1.0)  # Volume (0.0 a 1.0)

    def process_text(self, text):
        # Processa o texto e gera uma sequência de quadros de animação da boca.
        self.mouth_frames = []
        for char in text.lower():
            if char in self.vowels:
                self.mouth_frames.append(2)  # Boca aberta para vogais
            elif char.isspace() or char in {'.', ',', '!', '?'}:
                self.mouth_frames.append(0)  # Boca fechada para pausas
            elif char.isalpha():
                self.mouth_frames.append(1)  # Boca meio aberta para consoantes
        if not self.mouth_frames:
            self.mouth_frames = [0]  # Default: boca fechada
        return self.mouth_frames

    def speak(self, text):
        # Fala o texto e retorna os quadros de animação.
        self.process_text(text)
        self.engine.say(text)
        self.engine.runAndWait()
        return self.mouth_frames

    def get_language(self):
        # Retorna a duração de cada quadro em milissegundos.
        return self.language

    def get_current_frame(self, index):
        # Retorna o quadro atual com base no índice.
        if 0 <= index < len(self.mouth_frames):
            return self.mouth_frames[index]
        return 0  # Boca fechada se fora do índice
    
# fala = Speech(language='fr-FR') Exemplo de uso
# fala.speak("comment vas-tu ?")  Fala o texto e gera os quadros de animação
# frames = fala.speak("Olá, como você está?")  Fala o texto e gera os quadros de animação
