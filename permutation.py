from randomized_queue import RandomizedQueue

rq = RandomizedQueue()

# Read words from input
items = input("Enter words separated by space: ").split()

# Enqueue all words into RandomizedQueue
for item in items:
    rq.enqueue(item)

# Read k
k = int(input("How many random items to print? "))

# Validate that k doesnot exceed the number of inputs 
if k > rq.size():
    raise ValueError("k cannot be greater than number of input words")

# Print k random items
for _ in range(k):
    print(rq.dequeue())
