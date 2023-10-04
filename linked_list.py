class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.start_node = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node= new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
               self.start_node = new_node
               return
        n = self.start_node
        while n.ref is not None:
               n= n.ref
        n.ref = new_node;

    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            print("[ ", end="")
            n = self.start_node
            while n is not None:
                print(n.item , end=" ")
                n = n.ref
        print("]\n")

    def insert_at_index(self, index, data):
        if index < 0:
            print("Index out of bound")
            return

        new_node = Node(data)

        if index == 0:
            new_node.ref = self.start_node
            self.start_node = new_node
            return

        i = 0
        n = self.start_node
        while i < index - 1 and n is not None:
            n = n.ref
            i = i + 1

        if n is None:
            print("Index out of bound")
        else:
            new_node.ref = n.ref
            n.ref = new_node

    def insert_after_item(self, x, data):
            n = self.start_node
            print(n.ref)
            while n is not None:
                if n.item == x:
                    break
                n = n.ref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node
    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List has no element")
            return

        if x == self.start_node.item:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            return
    
    def get_length(self):
        length = 0
        current = self.start_node
        while current:
            length+=1
            current = current.ref
        return length

    def calculate_sum(self):
        current = self.start_node
        total = 0
        while current:
            total += current.item
            current = current.ref
        return 
    
    def concatenate(self, other_list, append_other_first=False):
        if not other_list.start_node:
            return

        current = self.start_node
        while current.ref:
            current = current.ref

        if append_other_first:
            current.ref = other_list.start_node
        else:
            other_current = other_list.start_node
            while other_current.ref:
                other_current = other_current.ref
            other_current.ref = self.start_node
            self.start_node = other_list.start_node
    
    def sorted_list(self):
        if self.start_node is None:
            return

        elements = []
        n = self.start_node
        while n is not None:
            elements.append(n.item)
            n = n.ref

        elements.sort()  # Mengurutkan elemen-elemen

        # Memperbarui linked list asli dengan elemen-elemen yang terurut
        n = self.start_node
        for item in elements:
            n.item = item
            n = n.ref
    
    def reverse_list(self):
        prev = None
        current = self.start_node
        while current:
            next_node = current.ref
            current.ref = prev
            prev = current
            current = next_node
        self.start_node = prev


