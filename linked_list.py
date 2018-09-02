class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return 'Node({} -> {})'.format(self.data, str(self.next_node))

    __repr__ = __str__


class LinkedList:
    def __init__(self, head=None):
        self.head = None  # Pointer to the first node

    def insert(self, item):
        # Create a new node whose pointer points to head
        new_node = Node(item, self.head)
        # Make the head pointer point to the new node
        self.head = new_node

    def append(self, item):
        new_node = Node(item, None)
        current_node = self.head
        if self.head is None:
            self.head = new_node
        else:
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def __len__(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next_node
        return count

    def __contains__(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next_node
        return found

    def remove(self, item):
        current_node = self.head
        previous_node = None
        is_found = False
        # We first look for the node containing the item
        while not is_found:
            if current_node.data == item:
                is_found = True
            else:
                previous_node = current_node
                current_node = current_node.next_node
        # We then focus on the previous_node
        if previous_node is None:
            self.head = current_node.next_node
        else:
            previous_node.next_node = current_node.next_node
        return is_found

    def find(self, item):
        current_node = self.head
        while current_node is not None:
            if current_node.data == item:
                return current_node
            else:
                current_node = current_node.next_node
        return None

    def pop(self):
        if self.head is None:
            return None
        deleted_element = self.head
        temp = self.head.next_node
        self.head = temp
        return deleted_element

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.next_node


class Stack:
    def __init__(self, top=None):
        self.linked_list = LinkedList(top)

    def push(self, new_element):
        new_node = Node(new_element)
        self.linked_list.insert(new_node)

    def pop(self):
        self.linked_list.pop()


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert(10)
    print('list length = {}'.format(len(linked_list)))
    linked_list.insert('Hello')
    print('list length = {}'.format(len(linked_list)))
    linked_list.insert(2010)
    