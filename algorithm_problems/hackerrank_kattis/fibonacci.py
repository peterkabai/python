def fib_naive(n):
    if n <= 1:
        return n
    else:
        return fib_naive(n-1) + fib_naive(n-2)

def fib_tabulation(n):
    values = [0] * n
    for i in range(n):
        if i < 1:
            values[i] = 1
        else:
            values[i] = values[i-1] + values[i-2]
    return values[-1]

def fib_memoization(n, values=None):
    if values is None:
        values = [0] * (n + 1)
        values[0] = 0
        values[1] = 1
    if n > 1 and values[n] is 0:
        values[n] = fib_memoization(n-1, values)[n-1] + fib_memoization(n-2, values)[n-2]
    if values[-1] is not 0:
        return values[-1]
    else:
        return values

print(fib_naive(3))
print(fib_naive(9))
print(fib_tabulation(3))
print(fib_tabulation(9))
print(fib_memoization(3))
print(fib_memoization(9))
