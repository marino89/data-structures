class Node:
    
    def __init__(self, data=None, next_=None, prev=None):
        self.data = data
        self.next = next_
        self.prev = prev
    

class DoublyLinkedList:

    def __init__(self):
        self.head = None  # pointer to the beginner node
        self.tail = None  # pointer to the latest node added
        self._size = 0
    
    def append(self, data):
        node = Node(data)
        if self.tail is None:
            self.tail = self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self._size += 1
    
    def __repr__(self):
        res = ''
        current = self.head
        while current is not None:
            res += current.data
            res += ' -> '
            current = current.next
        return res

    def __len__(self):
        return self._size

    def delete(self, data):
        node_deleted = False
        current = self.head
        if current is None:
            node_deleted = False
        elif current.data == data:
            self.head = current.next
            self.head.prev = None
            node_deleted = True
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        else:
            while current is not None:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next
        if node_deleted:
            self._size += 1

    def info(self):
        print(self)
        print('head pointer:', self.head.data)
        print('tail pointer:', self.tail.data)
        

dll = DoublyLinkedList()
way = ('Paris', 'Lyon', 'Marseille', 'Nice')
for n in way:
    dll.append(n)
dll.info()
# delete Lyon
dll.delete('Marseille')
dll.info()





