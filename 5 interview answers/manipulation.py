def unique_chars_no_vowels(s: str) -> set:
    vowels = set("aeiouAEIOU")
    chars = set(s)            # unique characters
    return chars - vowels     # remove vowels

# Example
text = "Hello World"
print(unique_chars_no_vowels(text))
# Output: {'H', 'W', 'd', 'l', 'r', ' '}
