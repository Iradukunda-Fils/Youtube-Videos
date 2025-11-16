class Queue:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("dequeue from empty queue")
    
    def __len__(self):
        return len(self.items)
    

def main():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Queue size after enqueues:", len(queue))
    print("The elements in the queue are:", queue.items)
    print("Dequeued item:", queue.dequeue())
    print("Queue size after dequeue:", len(queue))
    print("Is queue empty?", queue.is_empty())
    print("The elements in the queue are:", queue.items)

if __name__ == "__main__":
    main()