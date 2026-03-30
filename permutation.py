from randomized_queue import RandomizedQueue
rq = RandomizedQueue()
items = input("Enter words separated by space: ").split()

for item in items:
    rq.enqueue(item)

k = int(input("How many random items to print? "))

for _ in range(k):
    print(rq.dequeue())