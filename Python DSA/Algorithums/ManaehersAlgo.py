def longest_palindromic_substring(s):
    T = preprocess(s)
    n = len(T)
    P = [0] * n
    C = R = 0
    
    for i in range(1, n - 1):
        mirror = 2 * C - i
        if i < R:
            P[i] = min(R - i, P[mirror])
        
        # Expand around center i
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1
        
        # Update center and right boundary
        if i + P[i] > R:
            C = i
            R = i + P[i]
    
    # Find the maximum length palindrome
    max_len = max(P)
    center_index = P.index(max_len)
    start = (center_index - max_len) // 2
    return s[start: start + max_len]

def preprocess(s):
    return '#' + '#'.join(s) + '#'


longest_palindromic_substring("babad")