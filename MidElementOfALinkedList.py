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
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
linked_list = linkedlist()
linked_list.insert(16)
linked_list.insert(13)
linked_list.insert(21)
linked_list.insert(40)
print("Middle element of the linked list:", linked_list.find_middle())

          