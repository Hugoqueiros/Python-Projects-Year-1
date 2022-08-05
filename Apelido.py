def main():


    n=str(input("Insira o seu nome: ")).strip()
    nome = n.split ()
    print("Seu apelido é: {} " .format(nome [len(nome)-1]))

if __name__ == '__main__':
    main()
