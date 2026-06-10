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
    def search_in_linked_list(self, target):
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next
        return False

linked_list = linkedlist()
linked_list.insert(16)
linked_list.insert(21)
linked_list.insert(13)
linked_list.insert(40)
target = 21
if linked_list.search_in_linked_list(target):
    print(f"{target} found in the linked list.")
else:
    print(f"{target} not found in the linked list.")
