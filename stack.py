class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed to stack.")

    def pop(self):
        if not self.stack:
            print("Stack is empty!")
        else:
            popped_item = self.stack.pop()
            print(f"{popped_item} popped from stack.")

    def display(self):
        if not self.stack:
            print("Stack is empty!")
        else:
            print("Stack elements are:", self.stack)

def menu():
    print("\nMenu:")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

if __name__ == "__main__":
    stack = Stack()

    while True:
        menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":  
            item = input("Enter the element to push: ")
            stack.push(item)

        elif choice == "2":  
            stack.pop()

        elif choice == "3":  
            stack.display()

        elif choice == "4": 
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")
