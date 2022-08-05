def main():
    vetor=[15,16,17,18,19,20,21]
    soma = vetor[0] + vetor[1] +vetor[2] +vetor[3] +vetor[4] +vetor[5] +vetor[6]
    media = soma / 7
    print ("A média das temperaturas foi: ", media)
    if vetor[0] > media:
        print("O 1 dia teve temperatura superior a media ")
    if vetor[1] > media:
        print("O 2 dia teve temperatura superior a media ")
    if vetor[2] > media:
        print("O 3 dia teve temperatura superior a media ")
    if vetor[3] > media:
        print("O 4 dia teve temperatura superior a media ")
    if vetor[4] > media:
        print("O 5 dia teve temperatura superior a media ")
    if vetor[5] > media:
        print("O 6 dia teve temperatura superior a media ")
    if vetor[6] > media:
        print("O 7 dia teve temperatura superior a media ")
    
    

if __name__ == '__main__':
    main()
