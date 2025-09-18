def filter_numbers(nums):
    result = []
    for n in nums:
        if n < 0:
            break              # stop if negative
        if n % 3 == 0:
            continue           # skip multiples of 3
        result.append(n)
    return result
