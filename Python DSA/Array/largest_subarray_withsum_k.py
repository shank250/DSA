def longestSubarrayWithSumK(a: [int], k: int) -> int:
    start = 0
    current_sum = 0
    max_length = 0
    subarray = []
    n = len(a)
    for end in range(n):
        current_sum += a[end]

        while current_sum > k:
            current_sum -= a[start]
            start += 1

        if current_sum == k:
            if end - start + 1 > max_length:
                max_length = end - start + 1
                subarray = a[start:end+1]

    return max_length