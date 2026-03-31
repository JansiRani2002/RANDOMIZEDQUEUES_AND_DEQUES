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
            raise ValueError("Cannot enqueue None item")

        # prevent accidental enqueue of empty string
        if item == "":
            raise ValueError("Empty items are not allowed")

        self.items.append(item)

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