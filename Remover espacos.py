def main():
    frase = str(input("Insira a sua frase : " )).strip().upper()
    palavras = frase.split()
    junto = '' .join (palavras)
    print(junto)


if __name__ == '__main__':
    main()
