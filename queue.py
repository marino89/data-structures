from random import randint
import time


class ListQueue:

    def __init__(self):
        self._list = []
    
    def size(self):
        return len(self._list)
    
    def enqueue(self, data):
        self._list.insert(0, data)
    
    def dequeue(self):
        return self._list.pop()
        
    
class DoubleListQueue:

    def __init__(self):
        self.inbound_stack = []  # only use to store elements that are added to the queue
        self.outbound_stack = []  # for element deletion only
    
    def enqueue(self, data):
        self.inbound_stack.append(data)   # pushed element data on top of the stack

    def dequeue(self):
        if len(self.inbound_stack) == 0:
            return None
        out = self.inbound_stack.pop()
        self.outbound_stack.append(out)
        return out


class Node:
    
    def __init__(self, data=None, next_=None, prev=None):
        self.data = data
        self.next = next_
        self.prev = prev


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def dequeue(self):
        """Remove the node at the front of the queue (head node)."""
        if self.head is None:
            return None
        
        data = self.head.data
        if self._size == 1:
            self.tail = None
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self._size -= 1
        return data
    
    def is_emtpy(self) -> bool:
        return self._size == 0

    def __len__(self):
        return self._size


class Track:
    """Music track"""
    def __init__(self, title=None):
        self.title = title
        self.length = randint(5, 10)  # minutes 
    
    def __repr__(self):
        return 'Track(title={}, time={})'.format(
            self.title, self.length)

class Playlist(Queue):
    """Queue that holds a number of tracks objects"""
    def __init__(self, pause_time=1.0):
        super().__init__()
        self.pause_time = pause_time

    def pause(self):
        time.sleep(self.pause_time)

    def add_track(self, track: Track):
        self.enqueue(track)
    
    def next_track(self) -> Track:
        if self.head is None:
            return None
        return self.head.data


    def play(self):
        print('Playlist now playing...')
        while not self.is_emtpy():
            current_track_node = self.dequeue()
            print('Now Playing {} -- Next Song: {}'.format(
                current_track_node.title, self.next_track()))
            self.pause()
        print('Playlist is empty!')

    def __repr__(self):
        return 'Playlist({] tracks})'.format(len(self))


if __name__ == '__main__':
    playlist = Playlist()
    songs = ('Asturias', 'Granada', 'Mallorca', 'Sevilla')
    for song in songs:
        playlist.add_track(Track(song))
    playlist.play()

