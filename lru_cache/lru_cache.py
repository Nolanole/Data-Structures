from doubly_linked_list import ListNode, DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.  
    """
    def __init__(self, limit=10):
        self.size = 0
        self.limit = limit
        self.storage = DoublyLinkedList()
        self.storage_dict = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage_dict:
            node = self.storage_dict[key]
            val = node.value[1]

            if node.next is None and node.prev is None:
                if self.size == 1:
                    return val
                else:
                    return None
            else:
                self.storage.move_to_end(node)
                return val
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
        #if key already in dict, remove the value from the dll
        if key in self.storage_dict:
            old_node = self.storage_dict[key]
            self.storage.delete(old_node)
        
        #add the new_node to the tail:
        self.storage.add_to_tail((key, value))
        self.size = self.storage.length

        #if adding to tail exceeds the limit, remove the head:
        if self.size > self.limit:
            old_head = self.storage.head
            self.storage.remove_from_head()
            self.size = self.storage.length

            # #reset the next and prev of old head node to None
            # old_head.next = None
            # old_head.prev = None

            #delete the old node from the dict
            del self.storage_dict[old_head.value[0]]
        
        #update the dict w/ new node value
        self.storage_dict[key] = self.storage.tail