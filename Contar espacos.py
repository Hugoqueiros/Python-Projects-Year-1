def contaespacos(str):
    espacos = 0
    for c in str:
        if c == ' ':
            espacos += 1
    return espacos

if __name__== '__main__':
    print(contaespacos (" O Almeida é o meu chinelo "))
