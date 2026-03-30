# AI Usage Documentation

This document records how AI tools were used during the development of this project.

AI tools were used **only for learning assistance, explanation, and documentation**.  
All core implementation logic was written and understood by the student.

---

# AI Tool Used

ChatGPT (OpenAI)

Purpose:
- Understanding data structures
- Debugging errors
- Improving documentation
- Generating README and documentation structure

---

# Prompt Log

## Prompt 1
**Prompt**
Explain doubly linked list in simple words and how it can be used to implement a deque.

**AI Response Summary**
The AI explained the structure of a node with `next` and `prev` pointers and how this enables insertion and deletion from both ends efficiently.

**Usage**
Used to understand the design of the `Deque` class.

---

## Prompt 2
**Prompt**
How to implement a randomized queue in Python?

**AI Response Summary**
Suggested storing elements in a list and selecting a random index during dequeue operations.

**Usage**
Used as conceptual guidance while implementing `RandomizedQueue`.

---

## Prompt 3
**Prompt**
Explain how to randomly remove an element from a list in O(1) time.

**AI Response Summary**
Suggested swapping the random element with the last element and popping it.

**Usage**
Applied in `dequeue()` method of `RandomizedQueue`.

---

## Prompt 4
**Prompt**
Generate a README.md for a project implementing Deque and Randomized Queue.

**AI Response Summary**
AI generated structured documentation including project overview, implementation details, and complexity.

**Usage**
Used for project documentation only.

---

# Verification

All AI generated suggestions were reviewed and verified before being used.

The final implementation was tested using `main.py`.

---

# Declaration

AI was used only as a **learning and documentation assistant**, and not as a replacement for understanding the concepts. 


