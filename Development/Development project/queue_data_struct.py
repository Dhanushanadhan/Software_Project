from queue import  Empty
class QueueAdapter:
    def __init__(self):
        self.queue = []
        self.size = 0
    def __str__(self):
        return str(self.queue[:self.size])
    def enqueue(self, item):
        self.queue.append(item)
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        self.size -= 1
        return self.queue.pop(0)

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def front(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.queue[0]
    
    def __getitem__(self, index):
        return self.queue[index]
    def __setitem__(self, index, value):
        self.queue[index] = value