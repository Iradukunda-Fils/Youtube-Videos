class Math:
    def __init__(self, *numb: list | tuple):   
        self.numbers: list | tuple = numb
        
    @property
    def sum(self):
        return sum(i for i in self.numbers)
    
    @property
    def len(self):
        return len(self.numbers)
            
        