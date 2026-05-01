class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def middle(self):
        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
           slow = slow.next
           fast = fast.next.next

        return slow.data

    
    def reverse(self):
        prev = None
        current = self.head

        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def detect_cycle(self):
        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def delete(self,data):
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
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)

print("Original list:")
ll.traverse()

print("\nMiddle node:", ll.middle())

ll.reverse()
print("\nAfter reversing:")
ll.traverse()

print("\nCycle detected:", ll.detect_cycle())

ll.delete(4)
print("\nAfter deleting 4:")
ll.traverse()

print("\nSearch for 3:", ll.search(3))

print("\nFinal list:")
ll.traverse()