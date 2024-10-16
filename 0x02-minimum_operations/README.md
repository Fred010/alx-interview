# Technical Interview: Minimum Operations

### Project Overview
This Python project aims to implement an efficient algorithm to calculate the minimum number of operations required to convert a given integer n to 1. The allowed operations are:

Divide n by 2 if n is even.
Subtract 1 from n if n is odd.

### Algorithm
The algorithm used is a _greedy approach_:
* Base Case: If n is 1, return 0 as no operations are needed.
* Even Number: If n is even, divide it by 2 and increment the operation count.
* Odd Number: If n is odd, subtract 1 from n and increment the operation count.
* Recursive Call: Recursively call the function with the updated n until the base case is reached.

### Implementation
```
def min_operations(n):
    """Calculates the minimum number of operations to convert n to 1.

    Args:
        n: The integer to convert.

    Returns:
        The minimum number of operations required.
    """

    if n == 1:
        return 0

    if n % 2 == 0:
        return 1 + min_operations(n // 2)
    else:
        return 1 + min_operations(n - 1)
```

Usage
```
n = 10
result = min_operations(n)
print("Minimum operations to convert", n, "to 1:", result)
```

### Explanation
* The min_operations function takes an integer n as input.
* It checks if n is 1. If so, it returns 0.
* If n is even, it divides it by 2 and recursively calls itself with the updated n.
* If n is odd, it subtracts 1 from it and recursively calls itself.
* The final result is the accumulated count of operations.

### Time Complexity
The time complexity of this algorithm is O(log n) in the worst case, as the number of recursive calls is roughly equal to the number of times n can be divided by 2 before reaching 1.

