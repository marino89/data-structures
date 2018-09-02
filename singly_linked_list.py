
class Node:
    
    def __init__(self, data=None):
        self.data = data
        self.next = None    
    
    def __repr__(self):
        return 'Node(data={}, next={})'.format(self.data, self.next)


class SinglyLinkedList:

    def __init__(self):
        self.head = None  # reference to the very last node 
        self.tail = None  # reference to the very first node
        self._size = 0
    
    def append(self, data):
        node = Node(data)
        if self.head is not None:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self._size += 1

    def __repr__(self):
        current = self.tail
        res = ''
        while current is not None:
            res += current.data
            res += ' -> '
            current = current.next
        return res

    def __len__(self):
        return self._size
    
    def __iter__(self):
        current = self.tail
        while current is not None:
            value = current.data
            current = current.next
            yield value

    def delete(self, data):
        current = self.tail
        previous = None
        while current is not None:
            if current.data == data:
                if previous is None:
                    self.tail = current.next
                else:
                    previous.next = current.next
                self._size -= 1
            previous = current
            current = current.next

    def search(self, data) -> bool:
        current = self.tail
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def clear(self):
        self.head = None
        self.tail = None

    def pop(self):
        """Remove first element in the list and return its value."""
        if self.tail is None:
            raise Exception("Empty list!")
        current = self.tail
        value = current.data
        self.tail = current.next
        return value


words = ('eggs', 'ham', 'spam', 'nutella', 'cereals')
ingredients = SinglyLinkedList()
for word in words:
    ingredients.append(word)
print(ingredients)
ingredients.delete('ham')
print(ingredients)
ingredients.delete('eggs')
print(ingredients)
print('Searching for spam...', ingredients.search('spam'))
print('pop', ingredients.pop())