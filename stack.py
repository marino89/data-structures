class Node:
    
    def __init__(self, data=None):
        self.data = data
        self.next = None    
    
    def __repr__(self):
        return 'Node(data={}, next={})'.format(self.data, self.next)


class Stack:

    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self._size += 1
    
    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        self._size -= 1
        return data

    def peek(self):
        if self.top is None:
            return None
        return self.top.data


    def __len__(self):
        return self._size


if __name__ == '__main__':
    stack = Stack()
    for page in ('page1', 'page2', 'page3'):
        stack.push(page)
    for i in range(5):
        stack.pop()
        print('i = {}, len(stack) = {}, peek = {}'.format(
            i, len(stack), stack.peek()))







    