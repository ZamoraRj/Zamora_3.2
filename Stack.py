
# STACK - ZAMORA

stack = []

name = "ZAMORA"

# Adding letters (PUSH)
for letter in name:
    stack.append(letter)
    print("Pushed:", letter, "| Stack:", stack)

print("\nRemoving letters (POP):")

# Removing letters
while len(stack) > 0:
    removed = stack.pop()
    print("Popped:", removed, "| Stack:", stack)

print("\nStack is empty!")
 