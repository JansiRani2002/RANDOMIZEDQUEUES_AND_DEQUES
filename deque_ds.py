class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.first = None
        self.last = None
        self.n = 0

    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n

    def add_first(self, item):
        if item is None:
            raise ValueError("Item cannot be None")

        new_node = Node(item)
        new_node.next = self.first

        if self.is_empty():
            self.last = new_node
        else:
            self.first.prev = new_node

        self.first = new_node
        self.n += 1

    def add_last(self, item):
        if item is None:
            raise ValueError("Item cannot be None")

        new_node = Node(item)
        new_node.prev = self.last

        if self.is_empty():
            self.first = new_node
        else:
            self.last.next = new_node

        self.last = new_node
        self.n += 1

    def remove_first(self):
        if self.is_empty():
            raise IndexError("Deque is empty")

        item = self.first.item
        self.first = self.first.next

        if self.first:
            self.first.prev = None
        else:
            self.last = None

        self.n -= 1
        return item

    def remove_last(self):
        if self.is_empty():
            raise IndexError("Deque is empty")

        item = self.last.item
        self.last = self.last.prev

        if self.last:
            self.last.next = None
        else:
            self.first = None

        self.n -= 1
        return item

    def __iter__(self):
        current = self.first
        while current:
            yield current.item
            current = current.next