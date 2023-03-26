import pyautogui as gui

# abrir o navegador com o mouse , mas pela posição do meu pc 
def navegador_mouse():
    gui.moveTo(700,899)
    gui.click()

# por enquanto esse sera o padrão 
def navegador_padrao():
    gui.PAUSE = 1
    gui.press("win")
    gui.write('Microsoft Edge')
    gui.press('enter')

def fec_abr_tudo():
    gui.PAUSE = 1
    gui.keyDown('win')
    gui.press('d')
    gui.keyUp('win')

def arquivos() :
    gui.PAUSE = 1
    gui.press("win")
    gui.write('explorador de arquivos')
    gui.press('enter')

# quando o comando 'frase' tiver 'apagar lixeira' ou 'limpar lixeira' 
def limpar_lixeira():
    gui.PAUSE = 1
    gui.press('win')
    gui.write('lixeira')
    gui.press('enter')
    gui.keyDown('ctrl')
    gui.press('a')
    gui.press('d')
    gui.keyUp('ctrl')
    gui.press('enter')
    gui.keyDown('alt')
    gui.press('f4')
    gui.keyUp('alt')

def funcao_basica(self):
    # fecha o app aberto
    if 'fechar' in self:
        gui.keyDown('alt')
        gui.press('f4')
        gui.keyUp('alt')
    # minimiza todos os apps
    elif 'minimizar' in self and 'maximizar' in self:
        gui.keyDown('win')
        gui.press('d')
        gui.keyUp('win')
    # abri um app especificado
    else :
        gui.PAUSE = 1
        gui.press("win")
        gui.write(self)
        gui.press('enter')

# abrir o navegador
# criar classe navegador , so comandos do navegador 
# alt + -> , avança a pagina
# alt + <- , volta a pagina 
# f5 , atualiza 
# alt + d , para pesquisar 
# ctrl + t , nova aba 
# ctrl + w , fechar aba 
# ctrl + tab , proxima aba 


class Navegador :
    def __init__(self) -> None:
        pass
    
    def zoom_mais(self):
        gui.keyDown('ctrl')
        gui.press('+')
        gui.keyUp('ctrl')
    
    def zoom_menos(self):
        gui.keyDown('ctrl')
        gui.press('-')
        gui.keyUp('ctrl')
    
    def nv_janela_anom(self):
        gui.keyDown('ctrl')
        gui.keyDown('shift')
        gui.press('n')
        gui.keyUp('ctrl')
        gui.keyUp('shift')
    
    def nova_janela(self):
        gui.keyDown('ctrl')
        gui.press('n')
        gui.keyUp('ctrl')
    
    def pular_aba(self):
        gui.keyDown('ctrl')
        gui.press('tab')
        gui.keyUp('ctrl')
    
    def fechar_aba(self):
        gui.keyDown('ctrl')
        gui.press('w')
        gui.keyUp('ctrl')
    
    def nova_aba(self):
        gui.keyDown('ctrl')
        gui.press('f')
        gui.keyUp('ctrl')
    
    def localizar(self):
        gui.keyDown('ctrl')
        gui.press('t')
        gui.keyUp('ctrl')
            
    def imprimir(self):
        gui.keyDown('ctrl')
        gui.press('p')
        gui.keyUp('ctrl')
        
    def pesquisar(self):
        gui.keyDown('alt')
        gui.press('d')
        gui.keyUp('alt')
            
    def atualizar(self):
        gui.press('f5')
        
    def tela_cheia(self):
        gui.press('f11')
            
    def voltar(self):
        gui.keyDown('alt')
        gui.press('left')
        gui.keyUp('alt')

    def avancar(self):
        gui.keyDown('alt')
        gui.press('right')
        gui.keyUp('alt')
        
    def reabrir_aba(self):
        gui.keyDown('ctrl')
        gui.keyDown('shift')
        gui.press('t')
        gui.keyUp('ctrl')
        gui.keyUp('shift')
        
    def historico(self):
        gui.keyDown('ctrl')
        gui.press('h')
        gui.keyUp('ctrl')
    
    def marcar(self):
        gui.keyDown('ctrl')
        gui.press('d')
        gui.keyUp('ctrl')
                
        
       

nav = Navegador()
nav.zoom_mais()





