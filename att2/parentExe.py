# Dado uma string de expressão x. 
# Verifique se os pares e a ordem de ‘{’ , ‘}’ , ‘(’ , ‘)’ , ‘[’ , ‘]’ estão corretos.
# Por exemplo, a função deve retornar:
# ‘True’ para exp = “[()]{}{()()}” e 
# ‘False’ para exp = “[(])”.

from stack import Stack

def is_balanced(expression):
    """
    Verifica se a expressão possui parênteses balanceados.
    Usa a pilha implementada em stack.py.
    """
    pilha = Stack()
    verification = True
    #------- COLOQUE SEU CÓDIGO AQUI -------
    for char in expression:
        if( char == '[' or char == '{' or char == '(' ):
            pilha.push(char)
        
        if(char == ']'):
            if(not pilha.is_empty()):
                if(pilha.peek() != '['):
                    verification = not verification
                    break
                pilha.pop()
            else:
                verification = not verification
                break

        if(char == '}'):
            if(not pilha.is_empty()):
                if(pilha.peek() != '{'):
                    verification = not verification
                    break
                pilha.pop()
            else:
                verification = not verification
                break


        if(char == ')'):
            if(not pilha.is_empty()):
                if(pilha.peek() != '('):
                    verification = not verification
                    break
                pilha.pop()
            else:
                verification = not verification
                break
    
    return verification



    #---------------------------------------


# Teste
print(is_balanced("[{}(2+2)]{}")) #Esperado True
print(is_balanced("[{}(2+2))]{}")) #Esperado False
print(is_balanced("[{}])")) #Esperado False
