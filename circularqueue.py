class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size  
        self.front = self.rear = -1  

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full!")  
        else:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item
            print(f"{item} inserted into the queue.")

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty!") 
        else:
            dequeued_item = self.queue[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.size
            print(f"{dequeued_item} deleted from the queue.")

    def display(self):
        if self.front == -1:
            print("Queue is empty!")
        else:
            print("Queue elements are:", end=" ")
            i = self.front
            while True:
                print(self.queue[i], end=" ")
                if i == self.rear:
                    break
                i = (i + 1) % self.size
            print()

if __name__ == "__main__":
    size = int(input("Enter the size of the circular queue: "))
    circular_queue = CircularQueue(size)

    while True:
        print("\nMenu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == "1":  
            item = input("Enter the element to insert: ")
            circular_queue.enqueue(item)

        elif choice == "2":
            circular_queue.dequeue()

        elif choice == "3": 
            circular_queue.display()

        elif choice == "4": 
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")
