class node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None 
    def insert(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
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
linked_list.printlist()






