#Linked_list Implementation
class Node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next     
class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = self.head
        self.size = 0
    def is_Empty(self):
        return self.head == self.tail
    def append(self, item):
        new_node = Node(item)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1 

    def traverse(self):
        pos = self.head
        while pos.next != None:
            pos = pos.next
        return pos
       
      
    def display(self):
        elements = []
        current = self.head.next
        while current:
            elements.append(current.item)
            current = current.next
        print(elements)
    def  find_position(self, value):
        pos = 1
        current = self.head
        while current.next != None:
            current = current.next
            if current.item == value:
                return pos
            pos += 1
        return f"{value} is not exist in linked list" 
    def insert_position(self, position):
        temp = self.head
        for _ in range( position-1 ):
            temp = temp.next
        return temp
    def insert(self,  position, item):  
        pos = self.insert_position(position)
        new_node = Node(item)
        new_node.next = pos.next 
        pos.next = new_node
        # if position is end of the linked list we should update the position of end/tail  pointer
        if pos == self.tail :
            self.tail = pos
        self.size += 1
    def delete(self, data = None):     
        if data != None:
            position = self.find_position(data)
            pos = self.insert_position(position)
            pos.next = pos.next.next 
            if pos.next == self.tail:
                self.tail = pos
            self.size -= 1
        else:
            temp = self.head.next
            self.head.next = temp.next

    def insert_by_previous (self, data, item):
        position = self.find_position(data)
        pos = self.insert_position(position)
        new_node = Node(item)
        new_node.next = pos.next
        pos.next = new_node
        # if position is end of the linked list we should update the position of end/tail  pointer
        if pos == self.tail :
            self.tail = pos
        self.size += 1
    def delete_by_previous(self, data):
        position = self.find_position(data) -1
        pos = self.insert_position(position)
        pos.next = pos.next.next 
        if pos.next == self.tail:
            self.tail = pos
        self.size -= 1


