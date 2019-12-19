import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # If inserting we must already have a tree/root
        # If value is less than self.value go left, make a new
        # tree/node if empty, otherwise
        # keep going (recursion)
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        # if greater than or equal to then go right, make a new
        # tree/node if empty, otherwise
        # keep going
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target == self.value, return it
        if target == self.value:
            return True
        # go left or right based on smaller or bigger
        elif target < self.value:
            # go left if smaller
            if self.left:
                return self.left.contains(target)
            else:
                # if self.left is None:
                return False
        else:
            # go right if bigger
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        # if right exists, go right
        # otherwise return self.value
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # call cb on each node recursively
        cb(self.value)
        # if calling right side
        if self.right:
            self.right.for_each(cb)
        # if calling left side
        if self.left:
            self.left.for_each(cb)

        # Iterative Solution - Lecture
        # stack = Stack()
        # stack.push(self)

        # while stack.len() > 0:
        #     current_node = stack.pop()
        #     if current_node.right:
        #         stack.push(current_node.right)
        #     if current_node.left:
        #         stack.push(current_node.left)
        #     cb(current_node.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # base case if empty
        if node == None:
            return
        # left side to get the low values
        if node.left:
            if node.left != None:
                node.left.in_order_print(node.left)
            else:
                pass
        # right side to get the high values
        if node.right:
            if node.right != None:
                node.right.in_order_print(node.right)
            else:
                pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        bft_queue = Queue()
        bft_queue.enqueue(node)

        while bft_queue.size > 0:
            node = bft_queue.dequeue()
            print(node.value)
            if node.left != None:
                bft_queue.enqueue(node.left)
            if node.right != None:
                bft_queue.enqueue(node.right)

    # Breadth First Traversal
    # Make a queue
    # Put root in the queue
    # While queue is not empty
    #     pop out front of queue
    #     DO THE THING!
    #     if left:
    #     add left to bck of queue
    #     if right:
    #     add right to back of queue



    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        dft_stack = Stack()
        dft_stack.push(node)

        while dft_stack.size > 0:
            node = dft_stack.pop()
            print(node.value)
            if node.left != None:
                dft_stack.push(node.left)
            if node.right != None:
                dft_stack.push(node.right)

    # Steps:
    # Make a stack
    # put root in stack
    # while stack not empty
    #     pop root out of stack
    #     DO THE THING!!!!
    #     if left
    #         add left to stack
    #     if right
    #         add right to stack

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
