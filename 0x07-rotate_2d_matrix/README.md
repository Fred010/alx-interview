Here’s a draft for your `README.md` file:

---

# **0x07. Rotate 2D Matrix**

## **Description**
This project focuses on implementing an in-place algorithm to rotate an \( n \times n \) 2D matrix by 90 degrees clockwise. The challenge is designed to test your understanding of matrix manipulation, in-place operations, and algorithmic efficiency in Python.

The key steps involved in this process are:
1. **Transpose the matrix**: Convert rows into columns.
2. **Reverse each row**: Adjust the transposed matrix to complete the 90-degree rotation.

---

## **Learning Objectives**
By completing this project, you will:
- Understand how 2D matrices are represented in Python using lists of lists.
- Learn how to perform in-place operations to optimize space complexity.
- Gain familiarity with matrix transposition and row manipulation techniques.
- Practice using nested loops to iterate through 2D data structures.

---

## **Requirements**
- **Allowed editors**: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **Python 3.8.10**.
- Files should:
  - End with a new line.
  - Begin with `#!/usr/bin/python3`.
  - Be executable.
  - Follow **pycodestyle** (version 2.8.0).
- You **cannot** import any modules.
- All modules and functions must be documented.

---

## **Task**
### **0. Rotate 2D Matrix**
- **Prototype**: `def rotate_2d_matrix(matrix):`
- **Description**:
  Rotate an \( n \times n \) 2D matrix by 90 degrees clockwise **in-place**.
- **Input**:
  - A 2D list `matrix` where \( n \geq 1 \).
- **Output**:
  - Modify the input `matrix` directly (in-place). Do not return anything.
- **Example**:
    ```python
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    rotate_2d_matrix(matrix)
    print(matrix)
    # Output:
    # [[7, 4, 1],
    #  [8, 5, 2],
    #  [9, 6, 3]]
    ```

---

## **Usage**
1. Clone this repository:
    ```bash
    git clone https://github.com/<your-username>/alx-interview.git
    ```
2. Navigate to the project directory:
    ```bash
    cd 0x07-rotate_2d_matrix
    ```
3. Test the function using the provided `main_0.py`:
    ```bash
    ./main_0.py
    ```

---

## **Algorithm**
1. **Transpose the matrix**:
   - Swap elements \( matrix[i][j] \) and \( matrix[j][i] \) for \( i < j \).
2. **Reverse each row**:
   - Reverse the elements in each row using slicing or the `reverse()` method.

---

## **Code**
```python
#!/usr/bin/python3
"""
Rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of lists): The n x n 2D matrix to be rotated.
    """
    n = len(matrix)
    
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()
```

---

## **Example Output**
Running the provided `main_0.py` script:
```bash
$ ./main_0.py
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

---

## **File Structure**
```
0x07-rotate_2d_matrix
├── 0-rotate_2d_matrix.py
├── main_0.py
└── README.md
```

---

## **Author**
- **[Fred Baafi]**
- GitHub: [Your GitHub Profile](https://github.com/Fred010)
