# 231. Power of Two

n = 2

def isPowerOfTwo(n):
    while (n >= 1):
        if n == 1:
            return True
        n = n / 2
    return False

print(isPowerOfTwo(n=n))