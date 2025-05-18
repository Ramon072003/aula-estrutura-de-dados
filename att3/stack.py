# Singly Linked List – Lista Simplesmente Encadeada
# Apenas com as operações básicas que vamos precisar para pilhas nesse momento.
# insert_at_top e remove_at_top

class Node:
    def __init__(self, data):
        self.data = data    # Valor do nó
        self.next = None    # Ponteiro para o próximo nó

class SinglyLinkedList:
    
    def __init__(self):
        self.top = None     # Ponteiro para o topo da Lista
        self.size = 0       # Tamanho da Lista

    def insert_at_top(self, data):
        """
        Insere um novo nó no topo da lista (top).
        """
        new_node = Node(data)     # Criamos o novo nó com o dado fornecido
        new_node.next = self.top  # O próximo do novo nó aponta para o atual top
        self.top = new_node       # Atualizamos o top para o novo nó (ele vira o topo da lista)
        self.size += 1 

    def delete_from_top(self):
        """
        Remove o nó do início da lista e retorna seu valor.
        Se a lista estiver vazia, levanta um erro.
        """
        if self.top is None:
            raise IndexError("Estrutura Vazia - Impossível remover elemento")
        
        removed_data = self.top.data    # Guarda o valor que está no topo e será removido
        self.top = self.top.next        # Top agora aponta para o próximo nó
                                        # Garbage Colector vai destruir o nó solto
        self.size -= 1                  
        return removed_data

    def is_empty(self):
        """
        Verifica se a lista está vazia.
        """
        return self.top is None

    def peek(self):
        """
        Retorna o valor do topo, sem removê-lo.
        """
        if self.top is None:
            raise IndexError("Estrutura Vazia - Impossível espiar")
        return self.top.data


# Implementação da Pilha usando a Lista Simplesmente Encadeada

class Stack:
    """
    Classe Stack (Pilha) implementada sobre a Lista Simplesmente Encadeada.
    """
    def __init__(self):
        self.singly_linked_list = SinglyLinkedList()
        self.queue = []

    def push(self, data):
        """
        Empilha (push) um novo elemento na pilha.
        """
        self.singly_linked_list.insert_at_top(data)
        print(f"{data} empilhado com sucesso.")

    def pop(self):
        """
        Desempilha (pop) o elemento do topo da pilha e retorna seu valor.
        """
        data = self.singly_linked_list.delete_from_top()
        print(f"{data} desempilhado com sucesso.")
        return data

    def peek(self):
        """
        Espia (peek) o elemento do topo sem removê-lo.
        """
        data = self.singly_linked_list.peek()
        print(f"O elemento no topo é: {data}")
        return data

    def is_empty(self):
        """
        Verifica se a pilha está vazia.
        """
        return self.singly_linked_list.is_empty()
    

        

    def size(self):
        """
        retorna o tamanho da pilha.
        """
        print (f"O tamanho da pilha é: {self.singly_linked_list.size}")
        return self.singly_linked_list.size
    
    def __str__(self):
        """
        Método mágico para representar a pilha no formato:

        1 (Topo)
        ↓
        5
        ↓
        3 (base)

        Mostra a ligação interna entre os nós da pilha.
        """
        if self.singly_linked_list.top is None:
            return "Pilha vazia"

        linhas = []
        atual = self.singly_linked_list.top  # Começa pelo topo
        index = 0  # Para saber se é o primeiro (topo) ou último (base)

        while atual is not None:
            if index == 0:
                # Primeiro elemento é o topo
                linhas.append(f"{atual.data} (Topo)")
            else:
                # Elementos intermediários, só valor
                linhas.append(f"{atual.data}")

            atual = atual.next
            if atual is not None:
                linhas.append("↓")  # Adiciona seta entre os nós
            index += 1

        # Após montar todas as linhas, indicamos que o último é a base
        if "↓" in linhas[-1]:
            # Se terminou com seta removemos
            linhas.pop()

        # Marca a base no último elemento (se não for igual ao topo)
        if index > 1:
            # Último elemento é a base (precisamos localizar a última linha com número)
            for i in range(len(linhas) - 1, -1, -1):
                if linhas[i] != "↓":
                    linhas[i] += " (base)"
                    break

        return "\n".join(linhas)
    

class Queue:
    def __init__(self):
        self.queue = []
        self.stack = Stack()

    def realoc(self, capacity):
        new = [0]*(capacity+1)
        j = capacity
        for i in range(capacity):
            new[j] = self.queue[j-1]
            j -=1
        self.queue = new
    
    def enqueue(self, data):
        self.stack.push(data)
        data = self.stack.peek()
        self.realoc(len(self.queue))
        for i in range(len(self.queue)):
            if self.queue[i] == 0:
                self.queue[i] = data

    def is_empty(self):
        return len(self.queue) == 0

    def remove(self):
        if(self.is_empty()):
            raise Exception('Queue is empty')
        new = [0]*(len(self.queue)-1)
        for i in range(len(new)):
            new[i] = self.queue[i]
        self.queue = new
    
    def data(self):
        return self.queue


# Testando a Pilha

if __name__ == "__main__":
    pilha = Stack()
    fila = Queue()

    # Tentando espiar uma pilha vazia (gera erro)
    try:
        pilha.peek()
    except IndexError as e:
        print(e)

    pilha.size()
    
    fila.enqueue(10)
    fila.enqueue(50)
    fila.enqueue(100)
    print(fila.data())
    fila.remove()
    fila.remove()
    print(fila.data())






