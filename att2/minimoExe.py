# Ajuste os métodos abaixo psuh_aux, pop_aux e get_min para que # seja possível
# encontrar o elemento mínimo de uma pilha simplesmente buscando no topo (peek) da pilha min_stack.

from stack import Stack

if __name__ == "__main__":
    main_stack = Stack()
    min_stack = Stack()

    def push_aux(data):
        """
        Função para empilhar na pilha principal e atualizar a pilha de mínimos quando necessário.
        """
        #---- SEU CÓDIGO AQUI ----
        
        main_stack.push(data)
        if(min_stack.is_empty()):
            min_stack.push(data)
        elif(data <= min_stack.peek()):
            min_stack.push(data)

        #-------------------------

    def pop_aux():
        """
        Função para desempilhar da pilha principal e atualizar a pilha de mínimos quando necessário.
        """
        #---- SEU CÓDIGO AQUI ----
        
        if(not main_stack.is_empty() and not min_stack.is_empty()):
            main_stack.pop()
            if(main_stack.peek() == min_stack.peek()):
                min_stack.pop()

        #-------------------------

    def get_min():
        """
        Função para retornar o mínimo atual.
        """
        #---- SEU CÓDIGO AQUI ----

        if(not min_stack.is_empty()):
            return min_stack.peek()
        
        return 'Pilha de minimos vazia'


        #-------------------------

    # Testes
    print("\nEmpilhando: 5, 3, 7, 2, 8")
    push_aux(5)
    print(f"Min atual: {get_min()}")

    push_aux(3)
    print(f"Min atual: {get_min()}")

    push_aux(7)
    print(f"Min atual: {get_min()}")

    push_aux(2)
    print(f"Min atual: {get_min()}")

    push_aux(8)
    print(f"Min atual: {get_min()}")

    print("\nDesempilhando e mostrando o mínimo:")
    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    try:
        print(get_min())
    except IndexError as e:
        print(f"Erro esperado: {e}")
