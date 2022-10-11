def calcular(n1,n2,op="!"):
    try:

        if "mais" in op:
            resultado=n1 + n2 
        elif "menos" in op:
            resultado=n1 - n2 
        elif "vezes" in op:
            resultado=n1 * n2 
        elif "dividir" in op:
            resultado=n1 / n2 
        elif "potencia" in op:
            if n2 == 0 :
                n2 = 2
            resultado=n1**n2
        elif "raiz" in op:
            resultado=n1**(1/2)
        elif "porcentagem" in op:
            resultado=n1*(n2/100)
        return resultado      
    except :
        print("ERRO !!")

   
     
