def multiply_matrix(a, b, mod):
    return (
        (a[0] * b[0] + a[1] * b[2]) % mod,
        (a[0] * b[1] + a[1] * b[3]) % mod,
        (a[2] * b[0] + a[3] * b[2]) % mod,
        (a[2] * b[1] + a[3] * b[3]) % mod
    )

def power_matrix(matrix, exp, mod):
    result = (1, 0, 0, 1)  # Identity matrix
    while exp > 0:
        if exp % 2 == 1:
            result = multiply_matrix(result, matrix, mod)
        matrix = multiply_matrix(matrix, matrix, mod)
        exp //= 2
    return result

def fibonacci_number(n):
    if n <= 1:
        return n
    base_matrix = (1, 1, 1, 0)
    result_matrix = power_matrix(base_matrix, n - 1, 10)
    return result_matrix[0]

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))