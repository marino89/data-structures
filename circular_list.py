
class Node:
    
    def __init__(self, data=None):
        self.data = data
        self.next = None    
    
    def __repr__(self):
        return 'Node(data={}, next={})'.format(self.data, self.next)


class CircularList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.tail.next = self.head
        self._size += 1

    def delete(self, data):
        current = self.head
        previous = None
        i = 1
        while i <= len(self):  # make sure we don't come back to the head node!
            if current.data == data:
                if previous is None:
                    self.head = current.next
                    self.tail.next = self.head
                else:
                    previous.next = current.next
                self._size -= 1
                return 
            previous = current
            current = current.next
            i += 1
        
    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def __len__(self):
        return self._size

    def print(self, n_cycles=3):
        cycles = 0
        for elt in self:
            if cycles <= n_cycles * len(self):
                print(elt)
            else:
                break
            cycles += 1


if __name__ == '__main__':
    cities = ('Marseille', )  #('Paris', 'Lyon', 'Marseille', 'Nice')
    loop = CircularList()
    for city in cities:
        loop.append(city)
    
    loop.print()
    print(len(loop))

    loop.delete('Marseille')
    print('\nAfter deletion: ')
    loop.print()
    print(len(loop))














