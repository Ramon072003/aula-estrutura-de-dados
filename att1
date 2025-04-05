class DynamicIntArray:
    def __init__(self, capactiy=2):
        if capactiy <=0:
            return ValueError('Capacidade inicial deve ser maior que 0')
        
        self.capacity = capactiy
        self.size = 0
        self.data = [0] * self.capacity

    def _resize_up(self, new_capacity):
        print(f"Aumentando a capacidade {self.capacity} para {new_capacity}")
        new_data = [0] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def append(self, value):
        if self.size == self.capacity:
            self._resize_up(2*self.capacity)
        self.data[self.size] = value
        self.size +=1

    def is_empty(self):
        if(self.size <=0):
            return True
        return False

    def get(self, index):
        if(index > self.size):
            return ValueError('Index fora dos limites')
        return self.data[index]
    
    def set(self, index, value):
        if(index > self.size-1):
            print('Index fora dos limites ao usar set')
        self.data[index] = value
    
    def _capacity_isUsage(self):
        usage = (self.capacity*25)/100
        if(self.size <= usage):
            return True
        return False

    def remove_at(self, index):
        if(index > self.size-1):
            print('Index fora dos limites')
            return None
        
        valueRemove = self.data[index]
        new_data = [0] * (self.size-1)

        for i in range(self.size-1):
            if(self.data[i] != valueRemove):
                if(new_data[i-1] == self.data[i]):
                    new_data[i] = self.data[i+1]
                else:
                    new_data[i] = self.data[i]
            else:
                for j in range(i, self.size):
                    new_data[i] = self.data[i+1]


        self.data = new_data

        if(self._capacity_isUsage()):
            new_capacity = self.capacity/2
            print(f'Redimensionando de {self.capacity} para {new_capacity}')
            self.capacity = new_capacity
        return valueRemove
    
    def remove(self, value):
        index = -1
        for i in range(self.size):
            if self.data[i] == value:
                index = i
                break

        if index == -1:
            print("Valor não encontrado")
            return None

        valueRemove = self.data[index]
        new_data = [0] * (self.size - 1)

        j = 0
        for i in range(self.size):
            if i == index:
                continue
            new_data[j] = self.data[i]
            j += 1

        self.data = new_data
        self.size -= 1

        if self._capacity_isUsage():
            new_capacity = self.capacity / 2
            print(f'Redimensionando de {self.capacity} para {new_capacity}')
            self.capacity = new_capacity

        return valueRemove

            
    
    def contains(self, value):
        for i in range(self.size):
            if(self.data[i]==value):
                return True
        return False
    
    def index_of(self, value):
        for i in range(self.size):
            if(self.data[i]==value):
                return i
        return -1
    
    def insert_at(self, index, value):
        if(index > self.size-1):
            print('Index fora dos limites')
            return None

        new_data = [0] * (self.size+1)
        for i in range(self.size):
            new_data[i] = self.data[i]

        new_data[index+1] = new_data[index]
        new_data[index] = value
        self.data = new_data

        if self.size == self.capacity:
            self._resize_up(2*self.capacity)


    def showInfo(self):
        print("capacity",self.capacity)
        print("size",self.size)

    def __str__(self):
        return str(self.data[:self.size])

lista = DynamicIntArray(2)
lista.append(10)
lista.append(99)
lista.append(50)
lista.append(510)
lista.append(7)

print(lista)
print(lista.remove(510))

print(lista)










