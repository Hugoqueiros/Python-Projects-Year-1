def main(string):
    s= ''
    for c in string:
        if c == ' ':
            s+=c
        return s
    frase = str(input("Insira a sua frase : " )).strip().upper()
    palavras = frase.split()
    junto = '' .join (palavras)
    inverso = ' '
    inverso = junto[::-1]
    if inverso == junto :
        print ("É um palíndromo")
    else:
        print ("Não é um palíndromo")
   


if __name__ == '__main__':
    print(string)
