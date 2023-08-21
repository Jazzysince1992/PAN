class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty. Cannot pop.")
            return None

    def is_empty(self):
        return len(self.items) == 0

# Example usage
stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)

print("Is the stack empty?", stack.is_empty())  # False

print("Popped:", stack.pop())  # Popped: 15
print("Popped:", stack.pop())  # Popped: 10
print("Popped:", stack.pop())  # Popped: 5
print("Popped:", stack.pop())  # Stack is empty. Cannot pop. Popped: None

print("Is the stack empty?", stack.is_empty())  # True
