def substrings_of_length(s: str, k: int) -> list:
    if k <= 0 or k > len(s):
        return []
    return [s[i:i+k] for i in range(len(s) - k + 1)]

# Example
print(substrings_of_length("abcdef", 3))
# Output: ['abc', 'bcd', 'cde', 'def']
