


def linear(n: int) -> None:
    """
    Time Complexity:
        Best Case: Ω(n)
        Worst Case: O(n)
        Average Case: Θ(n)
    
    Explanation:
        The loop runs exactly (n - 1) times, so the algorithm always takes linear time,
        regardless of the input. Therefore, best case, worst case, and average case are all linear.
    """

    
    for i in range(1, n):
        print("The number is: %d in linear time" % i)
        
    else: 
        print(" Whole iteration is done completed..!")
        
    
def linear_constant(n: int) -> int | None :
    """
    Time Complexity:
        Best Case: Ω(1)  -> if value is found on the first iteration
        Worst Case: O(n) -> if value is not found in the list
        Average Case: Between O(1) and O(n), so Θ(n) does not apply
    
    Explanation:
        This function loops through values from 1 to n.
        If value 30 is found early, it returns early (constant time).
        If not found, it loops through all elements (linear time).
    """


    
    for i, v in enumerate(range(1, n), start=0):
        if v == 30:
            return "The index of value %d is: %d" % (v, i)
        print("Element %d is found at %d " % (v, i))
    else: 
        print("The whole iteration is done..!")
        
    
def constant(a: int, b: int, op: str = "addition") -> int:
    """
    Time Complexity:
        Best Case: Ω(1)
        Worst Case: O(1)
        Average Case: Θ(1)
    
    Explanation:
        The function checks input types and performs a simple arithmetic operation.
        No matter what inputs are provided, the time to execute remains constant.
    """

    
    if (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(op, str)):
        
        match (op):
            # Check each possible operation
            
            case "multiplication":
                return a * b
            case  "division":
                return a / b
            case "fool division":
                return a // b
            case "addition":
                return a + b
            case "subtraction":
                return a - b
            case _:
                raise TypeError(
                    "The possible operations supported is:"
                    "*, /, //, +, -"
                    "only...!"
                    )
                
                
    # return the error if input is not valid
    raise TypeError(
        "please use the correct input in the algorith..!"
    )
    
def logarithim(array: list | tuple, target: str):
    """
    Time Complexity:
        Best Case: Ω(1)
        Worst Case: O(logn)
        
    Explanation:
        The function checks does not iterate through the whole n element, instead
        it breaks the problem into sub parts in any scenario.
    """
    low = 0
    high = len(array) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if array[mid] == target:
            return mid
        
        elif array[mid] < target:
            low = mid + 1
        
        else:
            high = mid - 1
            
    return -1
    
    
        
def permutation(n_input: list | tuple, pocket: list = []) -> None:
    """
    Time Complexity:
        Best Case: Ω(n!)
        Worst Case: O(n!)
        Average Case: Θ(n!)
    
    Explanation:
        The function take input and search for every possible combination of the given input.
        No matter what inputs are provided, the time to execute remains factorial.
    """
    
    if not n_input:
        print(pocket)
        return
    
    for i in range(len(n_input)):
        permutation(n_input[:i] + n_input[i + 1:], pocket + [n_input[i]])
    
    
    

def main() -> None:
    # linear(50 + 1)
    
    # linear_constant(50)
    
    # print(constant(6, 3, "multiplication"))
    
    # permutation([1,2,3])
    print(logarithim([1,2,3,4,5,6,7,8,910], 7))
    
    
    
if __name__ == "__main__":
    main()