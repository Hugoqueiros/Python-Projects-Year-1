def calcularmedia(soma,c):
        media=0
        media=soma/c
        return media
def main():
    c=1
    cm=0
    idade=int(input("Introduza a sua idade: "))
    salario=int(input("Introduza o seu salário: "))
    sexo=str(input("Introduza o seu sexo: "))
    maior=idade
    menor=idade
    soma=salario
    if(sexo=="mulher"):
        if(salario<=500):
            cm=cm+1
    while(idade>0):
        idade=int(input("Introduza a sua idade: "))
        if(idade<0):
            break
        c=c+1
        salario=int(input("Introduza o seu salário: "))
        sexo=str(input("Introduza o seu sexo: "))
        soma=soma+salario
        if(sexo=="mulher"):
            if(salario<=500):
                cm=cm+1
        if(idade>maior):
            maior=idade
        if(idade<menor):
            menor=idade
    print("A média de salários é de",calcularmedia(soma,c),"€")
    print(cm,"mulheres recebem um salário até 500€")
    print("A maior idade é",maior,"e a menor é",menor)
if __name__ == '__main__':
    main()
