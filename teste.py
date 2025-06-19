# import pygame
# import platform
# import asyncio
# import math

# # Configurações iniciais
# WIDTH, HEIGHT = 400, 400
# FPS = 60
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# SKIN_COLOR = (240, 180, 140)
# MOUTH_COLOR = (200, 80, 80)
# EYE_COLOR = (40, 40, 40)
# PUPIL_COLOR = (255, 255, 255)
# HAIR_COLOR = (70, 50, 30)
# BACKGROUND_COLOR = (220, 240, 255)

# # Estado da animação
# mouth_frame = 0  # 0: fechada, 1: meio aberta, 2: aberta
# mouth_target = 0
# blink_timer = 0
# blink_duration = 100
# blink_interval = 3500
# eyebrow_offset = 0
# last_key_time = 0
# mouth_duration = 120  # milissegundos por quadro da boca
# text_input = "milissegundos por quadro da boca"
# animation_timer = 0

# def setup():
#     global screen, clock
#     pygame.init()
#     screen = pygame.display.set_mode((WIDTH, HEIGHT))
#     pygame.display.set_caption("Rosto Animado 2D Vetorial")
#     clock = pygame.time.Clock()

# def draw_background():
#     # Fundo com gradiente simples
#     pygame.draw.rect(screen, BACKGROUND_COLOR, (0, 0, WIDTH, HEIGHT))
#     pygame.draw.circle(screen, (200, 220, 240), (200, 200), 150)

# def draw_face():
#     # Desenhar cabelo (curvas estilizadas)
#     pygame.draw.arc(screen, HAIR_COLOR, (80, 50, 240, 200), math.pi, 2 * math.pi, 30)
#     pygame.draw.arc(screen, HAIR_COLOR, (100, 60, 200, 180), math.pi * 0.8, math.pi * 1.2, 20)
    
#     # Desenhar rosto
#     pygame.draw.ellipse(screen, SKIN_COLOR, (120, 100, 160, 200))
    
#     # Desenhar sobrancelhas
#     eyebrow_y = 130 + eyebrow_offset
#     pygame.draw.arc(screen, BLACK, (140, eyebrow_y, 40, 20), math.pi, 2 * math.pi, 3)
#     pygame.draw.arc(screen, BLACK, (220, eyebrow_y, 40, 20), math.pi, 2 * math.pi, 3)
    
#     # Desenhar olhos (com piscar)
#     eye_open = 25 if blink_timer < blink_duration else 8
#     pygame.draw.ellipse(screen, EYE_COLOR, (145, 150, 30, eye_open))
#     pygame.draw.ellipse(screen, EYE_COLOR, (225, 150, 30, eye_open))
#     # Pupilas
#     pygame.draw.ellipse(screen, PUPIL_COLOR, (155, 155, 8, 8))
#     pygame.draw.ellipse(screen, PUPIL_COLOR, (235, 155, 8, 8))
    
#     # Desenhar nariz
#     pygame.draw.arc(screen, BLACK, (190, 170, 20, 20), math.pi / 2, math.pi, 2)
    
#     # Desenhar boca (três quadros de animação)
#     mouth_y = 230
#     if mouth_frame == 0:  # Fechada
#         pygame.draw.arc(screen, MOUTH_COLOR, (170, mouth_y, 60, 20), 0, math.pi, 5)
#     elif mouth_frame == 1:  # Meio aberta
#         pygame.draw.ellipse(screen, MOUTH_COLOR, (170, mouth_y - 10, 50, 20))
#     else:  # Aberta
#         pygame.draw.ellipse(screen, MOUTH_COLOR, (165, mouth_y - 15, 60, 30))

# def update_loop():
#     global mouth_frame, mouth_target, blink_timer, eyebrow_offset, last_key_time, text_input, animation_timer
    
#     current_time = pygame.time.get_ticks()
#     animation_timer += 1000 / FPS
    
#     # Processar eventos
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             return
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_BACKSPACE:
#                 text_input = text_input[:-1]
#             elif event.unicode.isprintable():
#                 text_input += event.unicode
#                 mouth_target = 2
#                 eyebrow_offset = -4
#                 last_key_time = current_time
#                 animation_timer = 0
    
#     # Atualizar animação da boca
#     if mouth_target > 0 and animation_timer >= mouth_duration:
#         mouth_frame = mouth_target
#         if current_time - last_key_time > mouth_duration * 2:
#             mouth_target -= 1
#             animation_timer = 0
#     elif mouth_target == 0:
#         mouth_frame = 0
    
#     # Atualizar sobrancelhas
#     eyebrow_offset += (0 - eyebrow_offset) * 0.1
    
#     # Atualizar piscar
#     blink_timer += 1000 / FPS
#     if blink_timer > blink_interval + blink_duration:
#         blink_timer = 0
    
#     # Desenhar
#     draw_background()
#     draw_face()
#     pygame.display.flip()
#     clock.tick(FPS)

# async def main():
#     setup()
#     while True:
#         update_loop()
#         await asyncio.sleep(1.0 / FPS)

# if platform.system() == "Emscripten":
#     asyncio.ensure_future(main())
# else:
#     if __name__ == "__main__":
#         asyncio.run(main())

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
            raise ValueError(f"Idioma inválido: {language}")
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

    def get_frame_duration(self):
        # Retorna a duração de cada quadro em milissegundos.
        return self.frame_duration

    def get_current_frame(self, index):
        # Retorna o quadro atual com base no índice.
        if 0 <= index < len(self.mouth_frames):
            return self.mouth_frames[index]
        return 0  # Boca fechada se fora do índice
    
fala = Speech(language='fr-FR')  # Exemplo de uso
fala.speak("comment vas-tu ?")  # Fala o texto e gera os quadros de animação
