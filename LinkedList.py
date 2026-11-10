
# LINKED LIST - ZAMORA

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self):
        if self.head is None:
            return None

        removed = self.head.data
        self.head = self.head.next
        return removed

    def display(self):
        current = self.head
        elements = []

        while current:
            elements.append(current.data)
            current = current.next

        return elements


letters = LinkedList()
name = "ZAMORA"

# Adding letters
for letter in name:
    letters.add(letter)
    print("Added:", letter, "| Linked List:", letters.display())

print("\nRemoving letters:")

# Removing letters
while letters.head is not None:
    removed = letters.remove()
    print("Removed:", removed, "| Linked List:", letters.display())

print("\nLinked List is empty!")
