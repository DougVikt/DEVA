def perimt(n1,n2,n3,op="!"):
    pi=3.14159265359    
    try :
        if "quadrado" in op:
            resposta=4*n1
        elif "circulo" in op:
            resposta=2*pi*(n1/2)
        elif "retangulo" in op:
            resposta=2*(n1+n2)    
        elif "triangulo" in op:
            resposta=n1+n2+n3
        return resposta
    except:
        print("ERRO !!")


def area(n1,n2,op="!"):
    pi=3.14159265359    
    try:
        if "quadrado" in op:
            resposta=n1**2
        elif "triangulo" in op:
            resposta=(n1*n2)/2
        elif "retangulo" in op:
            resposta=n1*n2
        elif "circulo" in op:
            n1=n1/2
            resposta=pi*(n1**2)
        return resposta
    except:
            print("ERRO !!")
