def main():
    c = 0
    soma= 0
    maior = 0
    while c < 7:
        t = float(input("Insira uma temperatura: "))
        soma= soma + t
        c = c + 1
        if c == 7:
            media = soma / c
            print("A media é ", media,"ºC")
    if media < t:
        print ("As temperaturas acima da media foram ", t,"ºC")
        


if __name__ == '__main__':
    main()
        
    
