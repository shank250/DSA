# class Solution:
#     def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
#         l = len(jobDifficulty)
#         if l < d:
#             return -1
#         elif l == d:
#             return sum(jobDifficulty)
#         else:
#             jobsDif = sorted(jobDifficulty)
#             rtn = 0 
#             for i in range(d-1):
#                 rtn += jobsDif[i]
#             rtn += jobsDif[-1]
#             return rtn
jobDifficulty = [6,5,4,3,2,1]
d = 2

l = len(jobDifficulty)
if l < d:
    print( -1)
elif l == d:
    print( sum(jobDifficulty))
else:
    jobsDif = sorted(jobDifficulty)
    rtn = 0 
    for i in range(d-1):
        rtn += jobsDif[i]
    rtn += jobsDif[-1]
    print( rtn)