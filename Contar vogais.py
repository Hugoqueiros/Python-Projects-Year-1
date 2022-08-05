
def contavogais( str ):
    contador = 0
    for c in str:
        if c in 'aeiou' :
            contador  += 1
    return contador

if __name__ == '__main__':
    print(contavogais( "abcde"))
