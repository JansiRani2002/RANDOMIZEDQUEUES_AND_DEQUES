# RandomizedQueue implementation for assignment
import random

class RandomizedQueue:

    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def enqueue(self, item):
        if item is None:
            raise ValueError("Item cannot be None")
        self.data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        rand_index = random.randint(0, len(self.data) - 1)

        item = self.data[rand_index]

        # swap with last element
        self.data[rand_index] = self.data[-1]
        self.data.pop()

        return item

    def sample(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        return random.choice(self.data)

    def __iter__(self):
        shuffled = self.data.copy()
        random.shuffle(shuffled)
        for item in shuffled:
            yield item