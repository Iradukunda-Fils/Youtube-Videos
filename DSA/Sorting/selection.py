def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        
        for j in range(i + 1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    return arr

def main():
    arr = [3, 5, 1, 34, 12, 43 ,12 ,34 ,53]
    
    print(selection_sort(arr))
    
    
if __name__ == "__main__":
    main()