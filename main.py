''' DEVA === desktop virtual assistant'''



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
    

