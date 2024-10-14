#array v
v = [3, 5, 2, 5, 3, 5, 1]
n = len(v)
# Write your code here
sorted_list = sorted(v, reverse=False)
# sorted_list = v.sort()
# dictionary where key represents number and
# value represents their frequency
freq_dict = {}
# prev = sorted_list[0]
# counter = 0
for i in sorted_list:
    # will check if the number is present or not in dictionary
    if freq_dict.get(i) is None:
        freq_dict[i] = 1
    # if not then we will increase it by 1
    else:
        freq_dict[i] += 1
# then we will try to know the maximum frequency/value in the list/dict
max, min = None, None 
print(freq_dict)
for number in freq_dict:
    if min == None and max == None:
       min = number
       max = number
    if freq_dict[number] > freq_dict[max]:
        max = number
    if freq_dict[number] < freq_dict[min]:
        min = number
# and similarly minimum frequency number
print(min, max)