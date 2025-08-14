# Last In First Our (FIFO)

# Time Complexity of removing element in queue is O(n)
# Time Complexity of adding element in queue is O(1)


""" 
- Time Complexity of removing element in queue is O(n)
    Where n is the length of the queue
    
- Time Complexity of adding element in queue is O(1)

Time Complexity of visiting elements in queue is O(n)
    Where n is the step in traversing  in the queue 
    
Space Complexity of visiting elements in queue is o(m)
    Where m is the length of the queue
    
The Best Case Scenario of visiting single element
    When we know its position it is constant time "O(1)" 
"""


class Que:
    def __init__(self):
        self.items: list = []
        
    def enqueue(self, value):
        self.items.append(value)
        return self.items
    
    def dequeue(self):
        return self.items.pop(0)
    
    def peek(self):
        return self.items[0]
    
    def traverse(self):
        
        i:int = 0
        
        while i < len(self.items):
            yield self.items[i]
            i += 1
            
qu: Que = Que()

qu.enqueue([2, 3, 4])
qu.enqueue(["hello", "World"]) 
print(qu.dequeue())       
print(list(qu.traverse())) 