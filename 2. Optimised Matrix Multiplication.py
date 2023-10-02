def matrix_chain_multiplication(matrices):
    n = len(matrices)
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]
    for i in range(1, n):
        m[i][i] = 0
    for chain_length in range(2, n):
        for i in range(1, n - chain_length + 1):
            j = i + chain_length - 1
            m[i][j] = float('inf') 
            for k in range(i, j):
                cost = m[i][k] + m[k+1][j] + matrices[i-1][0] * matrices[k][1] * matrices[j][1]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k  

    def parenthesize(i, j):
        if i == j:
            return f'Matrix {i}'
        else:
            k = s[i][j]
            left_chain = parenthesize(i, k)
            right_chain = parenthesize(k + 1, j)
            return f'({left_chain} × {right_chain})'

    optimal_parenthesization = parenthesize(1, n - 1)
    min_scalar_multiplications = m[1][n - 1]

    return optimal_parenthesization, min_scalar_multiplications


matrices = [(2, 3), (3, 4), (4, 2)]

optimal_parenthesization, min_scalar_multiplications = matrix_chain_multiplication(matrices)

print("Optimal Parenthesization:", optimal_parenthesization)
print("Minimum Scalar Multiplications:", min_scalar_multiplications)

"""
Explanation:

We use a dynamic programming approach where m[i][j] stores the minimum number of scalar multiplications needed to compute the product of matrices from i to j, and s[i][j] stores the index k where the optimal split occurs.

We initialize the diagonal of the m matrix to 0 because a single matrix doesn't require any multiplications.

We iterate over the chain length (chain_length) from 2 to n - 1, where n is the number of matrices.

For each chain length, we consider all possible split positions (k) within the chain and calculate the cost of multiplying the two resulting subchains.

We update m[i][j] with the minimum cost and record the optimal split position k.

Finally, we reconstruct the optimal parenthesization using the s matrix.

Time Complexity Analysis:

The algorithm has a time complexity of O(n^3) because it involves three nested loops.
The space complexity is O(n^2) for the m and s matrices.
Efficiency for Large Instances:

This dynamic programming algorithm is efficient for reasonably sized instances of the problem.
For very large instances with a large number of matrices, the time and space complexity may become a limiting factor.
In such cases, more advanced optimization techniques or parallel computing could be employed to handle the problem efficiently.
"""
