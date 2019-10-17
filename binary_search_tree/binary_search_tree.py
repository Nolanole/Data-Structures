import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack
# sys.path.append('../doubly_linked_list')
# from doubly_linked_list import DoublyLinkedList


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            return False if self.left is None else self.left.contains(target)
        else:
            return False if self.right is None else self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        return self.value if self.right is None else self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)

    #iterative:
    def for_each_iterative(self, cb):
        stack = []
        stack.append(self)
        while len(stack):
            current_node = stack.pop()
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            cb(current_node.value)
        


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left is not None:
            node.left.in_order_print(node.left)
        print(node.value)
        if node.right is not None:
            node.right.in_order_print(node.right)    
            

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        #create a queue
        q = Queue()
        #add start node to queue
        q.enqueue(node)
        #while queue not empty:
        while q.len() > 0:
            #pop front item
            current_node = q.dequeue()
            #do the thing
            print(current_node.value)
            #if left:
            if current_node.left is not None:
                #add it
                q.enqueue(current_node.left)
            #if right:
            if current_node.right is not None:
                #add it
                q.enqueue(current_node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        #create a stack- use dll stack
        stack = Stack()
        #push startnode to stack
        stack.push(node)
        #while stack > 0:
        while stack.len() > 0:
            #pop out start node:
            current_node = stack.pop()
            #do the thing to the popped node
            print(current_node.value)
            #if left child:
            if current_node.left is not None:
                #add left child to stack
                stack.push(current_node.left)
            #if right child:
            if current_node.right is not None:
                #add right child        
                stack.push(current_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
