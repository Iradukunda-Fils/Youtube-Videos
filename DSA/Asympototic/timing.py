from time import time



start = time()

for i in range(10000):
    print(i)
    
end = time()

print("the time taken is: {} ".format(end - start))