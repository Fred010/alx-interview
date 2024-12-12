# 0x0A-primegame

**Prime Game**

**Description**

Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including *n*, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play *x* rounds of the game, where *n* may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

**Prototype**

```python
def isWinner(x, nums):
````

  * `x`: The number of rounds.
  * `nums`: An array of *n* for each round.

**Returns**

  * The name of the player that won the most rounds.
  * If the winner cannot be determined, return `None`.

**Assumptions**

  * *n* and *x* will not be larger than 10000.
  * No external packages can be imported.

**Example**

```
x = 3, nums = [4, 5, 1]

First round: 4
Maria picks 2 and removes 2, 4, leaving 1, 3
Ben picks 3 and removes 3, leaving 1
Ben wins because there are no prime numbers left for Maria to choose

Second round: 5
Maria picks 2 and removes 2, 4, leaving 1, 3, 5
Ben picks 3 and removes 3, leaving 1, 5
Maria picks 5 and removes 5, leaving 1
Maria wins because there are no prime numbers left for Ben to choose

Third round: 1
Ben wins because there are no prime numbers for Maria to choose

Result: Ben has the most wins
```

**Files**

  * `0-prime_game.py`: Contains the implementation of the `isWinner` function.

**Compilation and Execution**

```bash
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
```

**Expected Output**

```
Winner: Ben
```

**Concepts**

  * Prime numbers
  * Sieve of Eratosthenes
  * Game theory
  * Dynamic programming (optional)
  * Python programming (loops, conditionals, lists)

**Resources**

  * [Prime Numbers: Introduction to prime numbers](https://www.google.com/url?sa=E&source=gmail&q=https://www.khanacademy.org/math/precalculus/x2f8bb11c42b538c:rational-exponents/x2f8bb11c42b538c:prime-numbers/a/introduction-to-prime-numbers)
  * [Sieve of Eratosthenes in Python](https://www.google.com/url?sa=E&source=gmail&q=https://www.geeksforgeeks.org/sieve-of-eratosthenes/)
  * [Game Theory Introduction](https://www.google.com/url?sa=E&source=gmail&q=https://www.investopedia.com/terms/g/game-theory.asp)
  * [What Is Dynamic Programming With Python Examples](https://www.google.com/url?sa=E&source=gmail&q=https://www.educative.io/blog/dynamic-programming-python)
  * [Python Lists](https://www.google.com/url?sa=E&source=gmail&q=https://docs.python.org/3/tutorial/datastructures.html)
