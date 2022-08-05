def main ():

        lado1 = int(input("Insira o valor para um dos lados do triângulo: "))
        lado2 = int(input("Insira o valor para um dos lados do triângulo: "))
        lado3 = int(input("Insira o valor para um dos lados do triângulo: "))

        while lado1>=1 or lado2>=1 or lado3>=1:

                if lado1==0 or lado2==0 or lado3==0:
                        print ("Numeros invalidos Programa terminado")
                        break

                if (lado1>= lado2 + lado3) or (lado2>= lado3 + lado1) or (lado3>= lado1 + lado2):
                        print ("Comprimento dos lados inválidos")
                        return main()
                        
                if lado1==lado2 and lado1==lado3:
                         print("Vai formar um triângulo equilátero")
                         return main()
                        
                if (lado1==lado2 and lado1!=lado3) or (lado1==lado3 and lado1!=lado2) or (lado2==lado3 and lado1!=lado3):
                        print ("Vai formar um triângulo isósceles")
                        return main()
                        
                if (lado1!=lado2 and lado1!=lado3 and lado2!=lado3) :
                        print ("Vai formar um triângulo escaleno")
                        return main()
                







if __name__ == '__main__':
    main()
