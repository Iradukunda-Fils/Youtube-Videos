
def insertion_sort(arr):
    """
    step 1: 
    
    [1, 4, 2, 3]
    
    step 2:
    
    [1, 4, 4, 3]
    
    [1, 2, 4, 3]
    
    step 3:
    
    [1, 2, 4, 4]
    
    2 > 3 False
    
    [1, 2, 3, 4]
    """
    for i in range(1, len(arr)): 
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
    
    return arr

def main():
    arr = [12, 43, 2, 53, 2, 1, 5, 6, 7]
    
    print(insertion_sort(arr))
    

if __name__ == "__main__":
    main()