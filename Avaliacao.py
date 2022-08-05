def main():
    c = 0
    maior_nota= 0
    teste_1 = 0
    teste_2 = 0
    pratica = 0
    assiduidade = 0

    while teste_1 <= 20 and teste_1 >= 0 and teste_2 <= 20 and teste_2 >= 0 or pratica <= 20 and pratica >= 0 or assiduidade <= 20 and assiduidade >= 0:

        while c < 2:
            nome = str(input("Nome: "))

            
            assiduidade = float(input("Assiduidade de 0 a 20: "))
            while assiduidade < 0 or assiduidade > 20:
                print ("Programa invalido")
                assiduidade = float(input("Assiduidade de 0 a 20: "))
           
            
            teste_1= float(input("Nota do 1º teste: "))
            while teste_1 < 0 or teste_1 > 20:
                print ("Programa invalido")
                teste_1 = float(input("Qual a nota do 1º teste? "))
            
                
            teste_2= float(input("Nota do 2º teste: "))
            while teste_2 < 0 or teste_2 > 20:
                print ("Programa invalido")
                teste1 = float(input("Qual a nota do 2º teste? "))
           
                
            
            pratica = float(input("Nota do trabalho prático: "))
            while pratica < 0 or pratica > 20:
                print ("Programa invalido")
                teste1 = float(input("Qual a nota do 1º teste? "))
            
            
                
            nota_final = (assiduidade * 0.1) + (((teste_1 + teste_2)/2)*0.50) + (pratica * 0.40)
            print("A nota do ", nome, " é ", nota_final)

            c+=1

        if maior_nota < nota_final:
            maior_nota = nota_final
        print("A maior nota é de: ", maior_nota, "e pertence ao aluno", nome)

            
if __name__ == '__main__':
    main()
