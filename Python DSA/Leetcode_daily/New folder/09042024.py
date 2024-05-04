# 2073. Time Needed to Buy Tickets
			
tickets = [2,3,2]
k = 2

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
		targetValue = tickets[k]
		rtn = 0
		for index, val in enumerate(tickets):
			if (val >= targetValue) and (index <= k):
				rtn += targetValue
			elif (val >= targetValue) and (k < index):
				rtn += targetValue - 1
			else:
				rtn += val
		return rtn

