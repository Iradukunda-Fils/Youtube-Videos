

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        SWAPPED = False
        
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                SWAPPED = True
    return arr


def main():
    arr = [1, 32, 34, 443, 56, 4234, 12]
    print(bubble_sort(arr))
    
    
if __name__ == "__main__":
    main()