def prime_generator(n: int):
    for num in range(2, n + 1):  # iterate from 2 to n
        is_prime = True
        for i in range(2, num):  # check divisibility
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num

# Example usage
for p in prime_generator(30):
    print(p, end=" ")
