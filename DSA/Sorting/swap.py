class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def __repr__(self):
        return f"{self.value} -> {self.next.__repr__()}"
        

def swap_every_two_nodes(ll):
    head = ll
    prev = head
    
    while prev is not None and \
        prev.next is not None:
        prev.value, prev.next.value = prev.next.value, prev.value
        
        prev = prev.next.next
        
    return head


def main():
    ll = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
    print(repr(ll))
    print(swap_every_two_nodes(ll))
    

if __name__ == "__main__":
    main()