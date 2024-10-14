from collections import defaultdict


nums = [3,8,7,8,7,5]
k = 2 
x = 2
n = len(nums)

def m_sort(freq_d):
    sorted_item = sorted(freq_d.items(), key=lambda item: (-item[1], -item[0]))
    return sorted_item

ans = []

for i in range(n - k + 1):
    start = i
    end = i + k - 1
    hm = defaultdict(int)
    
    for j in range(start, end + 1):
        hm[nums[j]] += 1
    
    freq_lst = m_sort(hm)
    print(freq_lst)
    ptr = 0
    val_sum = 0
    if x >= len(freq_lst):
        for key, value in hm.items():
            val_sum += key*value
    else:
        for kth in range(x):
            print("tes")
            val_sum += freq_lst[kth][0]*freq_lst[kth][1]

            # if ptr >= len(freq_lst):
            #     break
            # if ptr< len(freq_lst) and hm[freq_lst[ptr]] > 0:
            #     x_ = freq_lst[ptr][0]
        #     x_ += val_sum
        #     hm[freq_lst[ptr]] -= 1
        # else:
        #     ptr += 1
        #     if ptr < len(freq_lst) and hm[freq_lst[ptr]]  > 0:
        #         x_ = freq_lst[ptr][0]
        #         x_ += val_sum
        #         hm[freq_lst[ptr]] -= 1
    ans.append( val_sum)
    # print(ans)
print(ans)


# Example usage:
# frequency_dict = {1: 3, 2: 5, 3: 5, 4: 2}
# sorted_result = sort_by_frequency_and_value(frequency_dict)
# print(sorted_result)
