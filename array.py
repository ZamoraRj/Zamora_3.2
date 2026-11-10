
# ARRAY - ZAMORA

letters = []

name = "ZAMORA"

# Adding letters
for letter in name:
    letters.append(letter)
    print("Added:", letter, "| Array:", letters)

print("\nRemoving letters:")

# Removing letters
while len(letters) > 0:
    removed = letters.pop(0)
    print("Removed:", removed, "| Array:", letters)

print("\nArray is empty!")
