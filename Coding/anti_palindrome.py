
def make_anti_palindrome(s: str) -> str:
    n = len(s)
    
    # Anti-palindromes are only defined for even-length strings.
    if n % 2 != 0:
        return "-1"
    
    from collections import Counter
    char_count = Counter(s)
    
    # Check feasibility: No character should appear more than n/2 times.
    for char, count in char_count.items():
        if count > n//2:
            return "-1"
    
    # Lexicographically sort the string
    sorted_chars = sorted(s)
    
    # Split into two halves
    half = n // 2
    first_half = sorted_chars[:half]
    second_half = sorted_chars[half:]
    
    # Create the result array
    result = [None] * n
    for i in range(half):
        result[i] = first_half[i]
        result[half + i] = second_half[i]
    
    # Check and rearrange to ensure anti-palindrome
    for i in range(n // 2):
        if result[i] == result[n - i - 1]:
            # Swap the conflicting character with the next available one
            if i + 1 < n // 2:
                result[half + i], result[half + i + 1] = result[half + i + 1], result[half + i]
            else:
                return "-1"  # If no valid swap is possible, return -1
    
    return "".join(result)

# Example usage
s = "abca"
output = make_anti_palindrome(s)
print(output)  # Output: "aabc"
