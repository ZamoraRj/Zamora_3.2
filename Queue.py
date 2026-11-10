
# QUEUE - ZAMORA

from collections import deque

queue = deque()

name = "ZAMORA"

# Adding letters (ENQUEUE)
for letter in name:
    queue.append(letter)
    print("Enqueued:", letter, "| Queue:", list(queue))

print("\nRemoving letters (DEQUEUE):")

# Removing letters
while len(queue) > 0:
    removed = queue.popleft()
    print("Dequeued:", removed, "| Queue:", list(queue))

print("\nQueue is empty!")
