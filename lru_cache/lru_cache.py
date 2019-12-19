from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        # self.limit = limit
        # self.size = 0
        # doubly-linked list that holds the key-value entries
        # self.list = DoublyLinkedList()
        # storage dict/cache
        # self.storage = {}

        # Lecture Solution
        self.limit = limit
        self.size = 0
        self.order = DoublyLinkedList()
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # if key-value pair doesn't exist in cache, return None
        # if key in self.storage:
        # if key in self.storage:
        #     val = self.storage[key]
        #     self.list.move_to_end(val)
        #     return val.value[1]
        # else:
        #     return None
        
        # Lecture Solution
        # Pull the value out of the dict using the key
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_front(node)
            return node.value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # if cache is already at max capacity
        # compare to self.limit of 10
        # if self.size == self.limit:
            # oldest entry needs to be removed to make room
            # del self.storage[self.list.head.value[0]]
            # self.list.delete(self.list.head)

        # if key already exists in the cache
        # overwrite the old value with new value
        # if key in self.storage:
        #     self.list.delete(self.storage[key])

        # add give key-value pair to cache/storage
        # self.list.add_to_tail((key, value))
        # self.size += 1
        # self.storage[key] = self.list.tail

        # Lecture Solution
        # Check the length if at limit, delete last
        # Check and see if key is in cache
        # If it is in the cache, move to front and update value
        # if self.size == self.limit
        # If not, add to the front of the cache
        # Defining tail as most recent and head as oldest
        # self.order.add_to_tail((key, value))
        # self.storage[key] = self.order.tail
        # self.size += 1

        # If it already exists, overwrite value
        if key in self.storage:
        # update dict
            node = self.storage[key]
            node.value = (key, value) # gets key value pair (tuple)
            # Mark as most recently used - put in the head of the DLL
            self.order.move_to_front(node)
            return
        # If at max capacity, dump oldest - remove from tail of DLL
        if self.size == self.limit:
            # dump the oldest:
            # remove it form the linked list
            # remove it from the dict
            del self.storage[self.order.tail.value[0]]
            self.order.remove_from_tail()
            self.size -= 1
        # Add pair to the cache - add to dict and add it nodes/DLL
        self.order.add_to_head((key, value))
        self.storage[key] = self.order.head
        self.size += 1


# class LRUCache:
#     def __init__(self, capacity):
#         self.list = LinkedList()
#         self.dict = {}
#         self.capacity = capacity

#     def _insert(self, key, val):
#         node = ListNode(key, val)
#         self.list.insert(node)
#         self.dict[key] = node

#     def get(self, key):
#         if key in self.dict:
#             val = self.dict[key].val
#             self.list.delete(self.dict[key])
#             self._insert(key, val)
#             return val
#         return -1

#     def set(self, key, val):
#         if key in self.dict:
#             self.list.delete(self.dict[key])
#         elif len(self.dict) == self.capacity:
#             del self.dict[self.list.head.key]
#             self.list.delete(self.list.head)
#         self._insert(key, val)
