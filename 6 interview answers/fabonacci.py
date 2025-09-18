def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# Test speed
start = time.time()
print("Memoized:", fib_memo(n))
end = time.time()
print("Memoized recursion took:", end - start, "seconds")
