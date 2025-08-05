class Item:
    def __new__(cls, name, price):
        if isinstance(price, (int, float)) and isinstance(name, str):
            return super().__new__(cls)
        
        raise TypeError("Invalid Price or non str name..? Expected Integer..!")
        
        
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return "%(nam)s ( $%(prc)s)" % {"nam": self.name, "prc": self.price}


    def __repr__(self):
        return "Item( %(rpnam)s, %(prc)s )" % {"rpnam": repr(self.name), "prc": self.price}
    
    
    def __eq__(self, other): 
        return (
            isinstance(other, self.__class__)
            and self.name == other.name 
            and self.price == other.price 
                )
 
 
    def __hash__(self):
        return hash((self.name, self.price))
    
    
    def __add__(self, other):
        if isinstance(other, self.__class__): 
            return Item("total of %(self)s and %(other)s" % {"self": self.name, "other": other.name}, 
                    self.price + other.price)
            
        raise TypeError("Not instance of the class..!")
        
        
    def __len__(self):
        return int(self.price)
        
    
    def __call__(self, scaller):
        self.price *= scaller
        return self
    
    
    
    
    
class Cart: 
    def __init__(self):
        self.items: list[Item] = []
        
        
    def __len__(self):
        return len(self.items)
    
    
    def __getitem__(self, index):
        return self.items[index]
    
    
    def __contains__(self, item):
        if isinstance(item, Item):
           return item in self.items
       
        raise TypeError("Only Item instance can be checked in the Cart.")
    
    
    def __add__(self, other):
        if isinstance(other, Item):
            self.items.append(other)
            return self
        
        raise TypeError("Only Item instance can be added to Cart.")
    
    
    def __str__(self): 
        return "Cart with %(items)i Items: %(item)s " % {
        "items": len(self.items),
         "item": ", ".join(str(i) for i in self.items)  
        }
        
        
    def __repr__(self):
        return "Cart( %(rep)s )" % {"rep": repr(self.items)}
    
    


def main():
    item1 = Item("TV", 30)
    item2 = Item("shoe", 100)
    item3 = Item("Toy", 50)
    # print(len(item1))
    # print( item2 + item3 + item1)
    
    cart = Cart() + item1 + item2 + item3
    
    cart1 = Cart()
    
    # print(cart[::-1])
    
    print(item1 in cart)
    
    # print(item1(2))


if __name__ == "__main__":
    main()
