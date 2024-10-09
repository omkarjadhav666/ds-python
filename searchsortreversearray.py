def display_menu():
    print("\nMenu:")
    print("1. Add elements to the array")
    print("2. Search for an element")
    print("3. Sort the array")
    print("4. Reverse the array")
    print("5. Display the array")
    print("6. Exit")

def add_elements():
    n = int(input("How many elements would you like to add? "))
    for i in range(n):
        element = int(input(f"Enter element {i + 1}: "))
        array.append(element)
    print("Elements added successfully!")

def search_element():
    if not array:
        print("Array is empty! Add elements first.")
        return
    element = int(input("Enter the element to search: "))
    if element in array:
        print(f"Element {element} found at index {array.index(element)}.")
    else:
        print("Element not found.")

def sort_array():
    if not array:
        print("Array is empty! Add elements first.")
        return
    array.sort()
    print("Array sorted successfully!")

def reverse_array():
    if not array:
        print("Array is empty! Add elements first.")
        return
    array.reverse()
    print("Array reversed successfully!")

def display_array():
    if not array:
        print("Array is empty! Add elements first.")
    else:
        print("Current array:", array)

array = []

while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        add_elements()
    elif choice == "2":
        search_element()
    elif choice == "3":
        sort_array()
    elif choice == "4":
        reverse_array()
    elif choice == "5":
        display_array()
    elif choice == "6":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
