from _collections_abc import Iterable

class listADT:
    def __init__(self, capacity):
       
            self.capacity = capacity
            self.size  = 0
            self.array = [None]*capacity
       
    def __str__(self):
        return f"{self.array[:self.size]}"

    #To performe appending operation
    def append(self, value):
            if self.size == self.capacity:
                self.resize(2*self.capacity)
            self.array[self.size] = value
            self.size += 1


    #To resize the list
    def resize(self, new_capacity):
        new_array = [None]*new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    #To calculate the lenght of list
    def __len__(self):
        return self.size
  
     #To make a object iterable   
    def __getitem__(self, index):
        if index >= 0  and index < self.size:
            return self.array[index]
        raise IndexError('Index out of range')

    #To access the element from index position given
    def __setitem__(self, index, value):
        self.array[index] = value

    def insert(self, index, value):
        if self.size == self.capacity:
            self.resize(2*self.capacity)
        for i in range(self.size, index, -1):
            self.array[i]= self.array[i-1]
        self.array[index] = value
        self.size += 1

    def delete(self, index):
        if index >= 0  and index < self.size:
            for i in range( index, self.size-1, 1):
                self.array[i] = self.array[i+1]
            self.size -= 1
        else:   
            raise IndexError('Index out of range')
        
