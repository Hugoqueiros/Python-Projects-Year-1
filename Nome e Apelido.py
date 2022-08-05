def main():


    n=str(input("Insira o seu nome: ")).strip()
    nome = n.split ()
    print("O seu nome é: {} " .format (nome [0]))
    print("Seu apelido é: {} " .format(nome [len(nome)-1]))

if __name__ == '__main__':
    main()
