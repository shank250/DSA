# class Solution:
#     def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
# 2225. Find Players With Zero or One Losses
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
win, lose = {}, {}

for w, l in matches:
    win[w] = win.get(w, 0) + 1
    lose[l] = lose.get(l, 0) + 1

winners = set(win.keys())
rtn = []
rtn.append(list(winners-set(lose.keys())))
rtn.append(list(loser for loser, freq in lose.items() if freq == 1))
print(rtn)