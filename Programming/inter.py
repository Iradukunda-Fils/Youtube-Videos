import sys

print(sys.argv)
print(sys.platform)

if True:
    print("something..!")
    
    
def func(item: list) -> list:
    item.append("hello")
    return item

t1 = [1,2,3,4]

t2 = t1

t3 = func(t1)

print(t1)
print(t3)