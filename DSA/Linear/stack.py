# Last In First Our (LIFO)

# Time Complexity of removing element in stack is O(1)
# Time Complexity of adding element in stack is O(1)


""" 
- Time Complexity of removing element in stack is O(1)
- Time Complexity of adding element in stack is O(1)

Time Complexity of visiting elements in stack is O(n)
    Where n is the steps of traversing the stack
    
Space Complexity of visiting elements in stack is o(m)
    Where m is the length of the stack
    
The Best Case Scenario of visiting single element
    When we know its position it is constant time "O(1)" 
"""


class Stack:
    def __init__(self):
        self.items: list = []
        
    def push(self, value):
        self.items.append(value)
       
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def traverse(self):
        
        i:int = 0
        while i < len(self.items):
            yield self.items[i]
            i += 1
            
st: Stack = Stack()

st.push([2, 3, 4])
st.push(["hello", "World"]) 
print(st.peek())       
print(list(st.traverse())) 
        