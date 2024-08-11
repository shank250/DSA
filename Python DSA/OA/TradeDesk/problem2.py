def solution(numbers, pattern):
    # variable to store the no of occurence of pattern in subarray
    count = 0

    n = len(numbers) #length of numbers list
    m = len(pattern)# length of paterns list
    
    for i in range(n - m + 1): #traveling the numbers list until the m

        match = True #letting that pattern is matched if all the conditions are satisfied

        for j in range(m):
            if j == 0: #skiping the initial check for j = 0
                continue
            # checking all the possible conditions for -1 1 0
            if (pattern[j] == 1 and numbers[i+j] <= numbers[i+j-1]) or \
               (pattern[j] == 0 and numbers[i+j] != numbers[i+j-1]) or \
               (pattern[j] == -1 and numbers[i+j] >= numbers[i+j-1]):
                match = False
                break
        if match:
            count += 1
    
    return count

print(solution([4,1,3,4,4,5,5,1], [1,0,-1]))