#este subprograma vai calcular a media
#parametros formais são o s, que corresponde à soma dos valores, e o c, que corresponde a contagem de números

def media_function(s,c):
    media = 0
    media = s/c
    return media

#programa principal
#parametros reais são o n, que vai ler o numero
    
def main():
    s = 0
    n = int(input("Insira um número inteiro: "))
    s = s + n
    c = 1
    
    if n == 0:
        print ("Programa terminado")
        print ("Foram lidos: ", c, " valores" )

    if n > 0:
        c = c -1

    while s <=  -255:
        n = int(input("Insira um número inteiro: "))
        c = c + 1
           
        media = media_function(s,c)    
        print ("A média é:", media)
        print("Finalizado")
        break
    
    while s > -255:
        n = int(input("Insira um número inteiro: "))
        c = c + 1
        print ("Foram lidos: ", c, " valores" )
        print ("Programa finalizado")
        break
    

    
            

if __name__ == '__main__':
    main()
