def main():
    contador = 0
    for joao in range (150,233, 2):
        contador= contador + 1
        

    for ze in range (110,234 , 3):
        contador = contador + 1
        

    if ze>joao:
        anos= (ze - 110)/3
        print("O ze esta mais alto do que o joao ", ((ze-joao)/100), "e demorou ",anos)




if __name__ == '__main__':
    main()
