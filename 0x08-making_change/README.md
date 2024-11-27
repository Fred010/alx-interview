## **README.md**

### **0. Change comes from within**

**Problem:**
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount `total`.

**Solution Approaches:**

1. **Greedy Algorithm:**
   * Prioritizes using the largest denomination coin possible at each step.
   * Efficient but not always optimal.

2. **Dynamic Programming:**
   * Breaks down the problem into smaller subproblems and builds an optimal solution.
   * Guarantees the minimum number of coins.

**Implementation:**

We've implemented both approaches in separate Python scripts:

1. **`0-making_change_greedy.py`**: Implements the greedy algorithm.
2. **`0-making_change_dp.py`**: Implements the dynamic programming approach.

**Usage:**

1. **Run the Scripts:**
   ```bash
   python 0-making_change_greedy.py
   python 0-making_change_dp.py
   ```

2. **Test Cases:**
   The `0-main.py` script provides test cases to evaluate both implementations.

**Key Concepts:**

- **Greedy Algorithms:** Prioritize immediate gratification.
- **Dynamic Programming:** Break down problems into smaller subproblems.
- **Time and Space Complexity:** Analyze the efficiency of algorithms.
- **Python Programming:** Utilize Python's syntax and libraries for implementation.

**Additional Notes:**

- **Coin Denominations:** The provided code assumes an infinite supply of each coin denomination.
- **Optimization:** Explore optimizations like memoization or tabulation to improve performance.
- **Edge Cases:** Consider edge cases like zero target amount or insufficient coins.
- **Real-world Applications:** This problem has applications in various fields, including finance, operations research, and computer science.
