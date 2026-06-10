class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None 
    def insert(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev    
    def printlist(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

linked_list = linkedlist()
linked_list.insert(16)
linked_list.insert(21)
linked_list.insert(13)
linked_list.insert(40)
print("Original linked list:")
linked_list.printlist()
linked_list.reverse()
print("Linked list after reversal:")
linked_list.printlist() 
