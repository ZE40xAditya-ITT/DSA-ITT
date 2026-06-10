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
    def delete(self, target):
        current = self.head
        previous = None
        while current:
            if current.data == target:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        return False    
linked_list = linkedlist()
linked_list.insert(16)
linked_list.insert(21)
linked_list.insert(13)
linked_list.insert(40)
target = 21
if linked_list.delete(target):
    print(f"{target} deleted from the linked list.")
else:
    print(f"{target} not found in the linked list.")
print("linked list after deletion:")
current = linked_list.head  
while current:
    print(current.data)
    current = current.next