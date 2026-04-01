# Randomized Queue and Deque (Python)

## Project Overview
This project implements two important data structures:

1. **Deque (Double Ended Queue)**
2. **Randomized Queue**

The purpose of this project is to understand:
- Linked Lists
- Randomized Algorithms
- Data Structure Design
- Iterators
- Python Object-Oriented Programming

---

# Project Structure
randomized_queues_dequeues/
│
├── deque_ds.py # Deque implementation using doubly linked list
├── randomized_queue.py # Randomized Queue implementation
├── permutation.py # Program to print k random elements
├── main.py # Testing script
└── README.md # Project documentation


---

# 1. Deque (Double Ended Queue)

A **Deque** allows insertion and removal from both ends of the data structure.

Example:
Front ← 5 10 20 → Back


### Operations

| Method | Description |
|------|-------------|
| `add_first(item)` | Insert element at front |
| `add_last(item)` | Insert element at end |
| `remove_first()` | Remove element from front |
| `remove_last()` | Remove element from end |
| `is_empty()` | Check if deque is empty |
| `size()` | Returns number of elements |

### Implementation

The deque is implemented using a **Doubly Linked List**.

Node structure:
Node
├── item
├── next
└── prev

### Time Complexity

| Operation | Complexity |
|----------|------------|
| Add First | O(1) |
| Add Last | O(1) |
| Remove First | O(1) |
| Remove Last | O(1) |

---

# 2. Randomized Queue

A **Randomized Queue** removes items **randomly instead of FIFO order**.

Example:
Queue = [A, B, C, D]

Random Dequeue → C

Remaining → [A, B, D]


### Operations

| Method | Description |
|------|-------------|
| `enqueue(item)` | Add item |
| `dequeue()` | Remove random item |
| `sample()` | Return random item without removing |
| `is_empty()` | Check if queue is empty |
| `size()` | Number of elements |

### Implementation

The structure uses a **dynamic Python list**.

Random removal steps:

1. Pick random index
2. Swap with last element
3. Remove last element

This ensures **O(1) removal time**.

---

# 3. Permutation Program

The `permutation.py` program prints **k random items from input**.

Example:

Input:
Enter words separated by space: A B C D E
How many random items to print? 3


Output:
D
A
C


Each run produces a **different random output**.

---

# Running the Project

## Step 1: Clone Repository
git clone <repository-url>
cd randomized_queues_dequeues 


---

## Step 2: Run Test Program
python main.py 


Example Output
Testing Deque
Deque elements: [5, 10, 20]
Removed first: 5
Removed last: 20

Testing Randomized Queue
Random sample: B
Random remove: A

Remaining items:
C
B



---

## Step 3: Run Permutation Program

---

# Key Concepts Used

- Doubly Linked Lists
- Randomized Algorithms
- Python Lists
- Iterators
- Exception Handling
- Object-Oriented Programming

---

# Learning Outcomes

After completing this project we learned:

- Implementation of **Deque using doubly linked list**
- Implementation of **Randomized Queue**
- Efficient **O(1) insert and remove operations**
- Usage of **Python iterators**
- Understanding of **randomized data structures**

---

# Author

Developed as part of a **Data Structures & Algorithms assignment**.


Note on Commit 219bdda

The commit message indicates changes to the RandomizedQueue, 
but the actual modifications were made in deque_ds.py to add 
validation improvements and utility methods.

This note clarifies the intent of that commit.

