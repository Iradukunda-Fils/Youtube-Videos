class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)
    
    def __len__(self):
        return len(self.items)
    
    
def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack size after pushes:", stack.size())
    print("Top item (peek):", stack.peek())
    print("The elements in the stack are:", stack.items)
    print("Popped item:", stack.pop())
    print("Stack size after pop:", len(stack))
    print("Is stack empty?", stack.is_empty())
    print("The elements in the stack are:", stack.items)
    
    
if __name__ == "__main__":
    main()