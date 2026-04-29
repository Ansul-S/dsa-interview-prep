# 29th Apr
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
# Append
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next != None:
            current = current.next

        current.next = new_node

# Prepend
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

# Delete
    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head

        while current.next != None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        print(f'{data} not found')

    def search(self, data):
        current = self.head
        while current != None:
            if current.data == data:
                return True
            current = current.next
        return False
    

    def traverse(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

ll = LinkedList()
ll.append(3)
ll.append(7)
ll.append(1)
ll.append(9)
ll.prepend(0)
ll.traverse()

print("---")
ll.delete(7)
ll.traverse()

print("---")
print(ll.search(3))   # True
print(ll.search(5))   # False