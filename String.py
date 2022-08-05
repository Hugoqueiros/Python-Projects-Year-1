# verificar se a string (palavra) e um palindromo
# com exemplo de docstring
def palindromo( string ):
    '''
        (string) -> boolean
        retorna True se string for um palindromo e
        retorna False em caso contrario
        >>> palindromo( radar )
        True
        >>> palindromo( rodar )
        False
    '''
    string = string.lower()
    if string == string[::-1]:
        return True
    else:
        return False
     
# verificar se e um palindromo - frases completas com
# caracteres de pontuacao: p.e. "Was it a rat I saw?", "Step on no pets"
def palindromoFrase( string ):
    string = string.lower()
    string = removeEspacos( string )
    string = removeNaoAlfabeticos( string )
 
    if string == string[::-1]:
        return True
    else:
        return False
 
# contar o numero de ocorrencias de um caracter
def contaOcorrencias( string, c ):
    '''
        (string, char) -> int
        retorna o numero de ocorrencias de um caracter numa string
        >>> contaOcorrencias( "palavra", 'a' )
        3
        >>> contaOcorrencias( "palavra", 'e' )
        0
    '''
    contador = 0
    for a in string:
        if a == c:
            contador += 1
    return contador
 
# indicar a primeira posicao onde ocorre um caracter
def primeiraPosicaoCaracter( string, c ):
    posicao = 0
    for a in string:
        if a == c:
            return posicao
        else:
            posicao += 1
    # retorna -1 se c nao existir em string
    return -1
             
# contar o  numero de espaços
def contaEspacos( string ):
    espacos = 0
    for c in string:
        if c ==' ':
            espacos += 1
    return espacos
 
# remover espacos da string
def removeEspacos( string ):
    s = ''
    for c in string:
        if c != ' ':
            s += c
    return s
 
# remover caracteres nao alfabeticos
def removeNaoAlfabeticos( string ):
    s = ''
    for c in string:
        if c.isalpha():
            s += c
    return s
 
# escrever a string considerando apenas os caracteres de ordem par (começa em 0)
def ordemPar( string ):
    print( string[::2])
 
# substituir na string um caracter por outro
def substitui( string, inicial, final ):
    for i in range(0,len(string)):
        if string[i]==inicial:
            string = string[:i]+final+string[i+1:]
    return string
 
# escrever os códigos ascii dos caracteres da string
def to_ascii( string ):
    for c in string:
        print( ord( c ) )
 
# contar o numero de vogais da string
def contaVogais( string ):
    contador = 0
    for c in string:
        if c in 'aeiou':
            contador += 1
    return contador
 
# funcao principal
def main():
 
    # alguns exemplos de utilizacao das funcoes acima
    s = input("Insira uma sequencia de caracteres: " )
 
    if palindromoFrase( s ):
        print( "A frase ", s, "e´um palindromo" )
    else:
        print( "A frase ", s, "nao e´um palindromo" )
 
    print('Codigos ASCII dos caracteres de ', s )
    to_ascii( s )
     
    if palindromo( s ):
        print( s, "e´um palindromo" )
    else:
        print( s, "nao e´um palindromo" )
 
    print( "Trocar 'a' por 'x' em 'programa':", substitui( 'programa', 'a', 'x'))
 
    print( 'Numero de vogais de ', s , ': ', contaVogais( s ) )
 
    print( s, ' sem espacos: ', removeEspacos( s ) )
 
    print( s, ' so com caracteres alfabeticos: ', removeNaoAlfabeticos( s ) )
 
    print( 'Caracteres de ordem par de ', s, ':')
    ordemPar(s)
     
    print( "Ocorrencias de 'a' na string ", s, ": ", contaOcorrencias( s, 'a' ) )
 
     
     
if __name__ == '__main__':
     main()
