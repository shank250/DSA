ll = [1,2,3,4,5]
n=5
k=2
def fnswap(start, end):
    dif = end - start
    iterat = dif // 2
    for i in range(iterat):
        tmp = ll[end-1-i]
        ll[end - i -1] = ll[start + i]
        ll[start + i] = tmp 
    return ll
    # M1 swap function which swaps the values
numOfTimes = len(ll)//k
start = 0
for i in range(numOfTimes):
    ll = fnswap(start, start + k)
    start = start + k
print(ll)

# from os import *
# from sys import *
# from collections import *
# from math import *

# '''
#     # Linked List Node structure for reference

#     class Node:
#         def __init__(self, data):
#             self.data = data
#             self.next = None

# '''

# def kReverse(head, k):
#     # get the length of the LL
#     # create a list 
#     headTmp = head
#     ll = []
#     while head:
#         ll.append(head.data)
#         head = head.next
#     # and then rearrage this list
#     def fnswap(start, end):
#         dif = end - start
#         iterat = dif // 2
#         for i in range(iterat):
#             tmp = ll[end-1-i]
#             ll[end - i -1] = ll[start + i]
#             ll[start + i] = tmp 
#         return ll
#         # M1 swap function which swaps the values
#     numOfTimes = len(ll)//k
#     start = 0
#     for i in range(numOfTimes):
#         ll = fnswap(start, start + k)
#         start = start + k
#     # push all the correct values
#     head = headTmp
#     i = 0
#     while head:
#         head.data = int(ll[i])
#         i += 1
#         head = head.next
#     return headTmp
#     # get the fliping address