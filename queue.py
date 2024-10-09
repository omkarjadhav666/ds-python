class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, item):
        self.queue.append(item)
        print(f"{item} inserted into the queue.")

    def delete(self):
        if not self.queue:
            print("Queue is empty!")
        else:
            removed_item = self.queue.pop(0)  
            print(f"{removed_item} deleted from the queue.")

    def display(self):
        if not self.queue:
            print("Queue is empty!")
        else:
            print("Queue elements are:", self.queue)

def menu():
    print("\nMenu:")
    print("1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

if __name__ == "__main__":
    queue = Queue()

    while True:
        menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":  
            item = input("Enter the element to insert: ")
            queue.insert(item)

        elif choice == "2":  
            queue.delete()

        elif choice == "3":  
            queue.display()

        elif choice == "4": 
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")
