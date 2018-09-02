class HashItem:
    def __init__(self, key: str, value: int):
        self.key = key
        self.value = value

    def __repr__(self):
        return 'HashItem(key={}, value={})'.format(self.key, self.value)


class HashTable:
    def __init__(self):
        self._size = 256  # number of elements 0, 1, ..., 255
        self.slots = [None] * self._size
        self._count = 0

    @property
    def count(self):
        return self._count

    def _hash(self, key: str) -> int:
        """Return an integer in [0, 256]"""
        return sum(ord(c) * i for i, c in enumerate(key, start=1)) % self._size
    
    def _rehash(self, h: int) -> int:
        """Linear probing collision resolution mechanism"""
        return (h + 1) % self._size

    def put(self, key, value):
        item = HashItem(key, value)
        idx = self._hash(key)  # compute the hash for the key
        slot = self.slots[idx]
        while slot is not None:
            if slot.key == key:
                break
            idx = self._rehash(idx)
            slot = self.slots[idx]
        if slot is None:
            self._count += 1
        self.slots[idx] = item  # if slot is already occupied, override its value

    def get(self, key): 
        idx = self._hash(key)
        slot = self.slots[idx]
        while slot is not None:
            if slot.key == key:
                return slot.value
            idx = self._rehash(idx)
            slot = self.slots[idx]
        return None

    def __setitem__(self, key, value):
        self.put(key, value)
    
    def __getitem__(self, key):
        self.get(key)

    def __len__(self):
        return self._size
    
    @property
    def load_factor(self):
        return self._count / self._size
    

if __name__ == '__main__':
    keys = ('France', 'UK', 'Italy', 'US')
    values = ('Macron', 'May', 'Conte', 'Trump')

    ht = HashTable()
    for k, v in zip(keys, values):
        ht.put(k, v)    

    print('Size: {}, Count: {} --> Load Factor: {}'.format(
        len(ht), ht.count, ht.load_factor))
    print('France: ', ht.get('France'))

