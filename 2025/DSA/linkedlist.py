class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1
        
    
    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            removed_data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return removed_data
        
        prev = self.head
        curr_index = 0
        while curr_index < index - 1:
            prev = prev.next
            curr_index += 1
        
        removed_data = prev.next.data
        new_next = prev.next.next
        prev.next = new_next
        self.size -= 1
        return removed_data
    
    def insert_at(self, index, data):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        new_node = Node(data)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            
            if self.size == 0:
                self.tail = new_node
                
            self.size += 1
            return
        
        prev = self.head
        curr_index = 0
        while curr_index < index - 1:
            prev = prev.next
            curr_index += 1
        
        new_node.next = prev.next
        prev.next = new_node
        self.size += 1

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements
    
    

def main(): 
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("Linked List after appends:", ll.display())
    
    ll.insert_at(1, 15)
    print("Linked List after inserting 15 at index 1:", ll.display())
    
    removed_item = ll.remove_at(2)
    print(f"Removed item at index 2: {removed_item}")
    print("Linked List after removal:", ll.display())
    


if __name__ == "__main__":
    main()