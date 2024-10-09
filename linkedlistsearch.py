class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True  
            current = current.next
        return False  

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

llist = LinkedList()
llist.append(10)
llist.append(20)
llist.append(30)

print("Linked List:")
llist.print_list()

key = int(input("Enter element to search: "))
if llist.search(key):
    print(f"Element {key} found in the list.")
else:
    print(f"Element {key} not found in the list.")
