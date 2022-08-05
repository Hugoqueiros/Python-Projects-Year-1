def main():
    frase= 'Substituir carateres mais que 3'
    print(frase)
    frase = frase.replace ("carateres", str(input(' ')))
    print(frase)

if __name__ == '__main__':
    main()
