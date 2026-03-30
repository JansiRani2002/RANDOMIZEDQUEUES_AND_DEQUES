from deque_ds import Deque
from randomized_queue import RandomizedQueue

print("Testing Deque")

dq = Deque()
dq.add_first(10)
dq.add_last(20)
dq.add_first(5)

print("Deque elements:", list(dq))

print("Removed first:", dq.remove_first())
print("Removed last:", dq.remove_last())


print("\nTesting Randomized Queue")

rq = RandomizedQueue()
rq.enqueue("A")
rq.enqueue("B")
rq.enqueue("C")

print("Random sample:", rq.sample())
print("Random remove:", rq.dequeue())

print("Remaining items:")
for item in rq:
    print(item)