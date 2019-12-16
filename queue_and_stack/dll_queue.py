import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # DLL already has the functions we can use
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # add an item to the back of the queue (tail)
        self.value = value
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        # remove and return an item from the front of the queue (head)
        # if queue empty
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        # returns number of items in queue
        return self.size
