def calcular(n1,n2,op="!"):
    try:

        if op == "+":
            resut=n1 + n2 
        elif op == "-":
            resut=n1 - n2 
        elif op== "*":
            resut=n1 * n2 
        elif op=="/":
            resut=n1 / n2 
        return print(resut)
    except :
        print("ERRO !!")
