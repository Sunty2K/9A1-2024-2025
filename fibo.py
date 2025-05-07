MOD = 10**9 + 7

# Hàm nhân ma trận 2x2
def mat_mult(A, B):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
             (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
             (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]]

# Hàm tính lũy thừa ma trận
def mat_pow(M, power):
    result = [[1, 0], [0, 1]]  # Ma trận đơn vị 2x2
    base = M
    while power > 0:
        if power % 2 == 1:
            result = mat_mult(result, base)
        base = mat_mult(base, base)
        power //= 2
    return result

# Hàm tính Fibonacci sử dụng ma trận
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Ma trận chuyển đổi
    F = [[1, 1], [1, 0]]
    result_matrix = mat_pow(F, n - 1)
    return result_matrix[0][0]  # Fibonacci(n) nằm tại [0][0] của ma trận

# Nhập đầu vào
n = int(input())
print(fibo(n))
