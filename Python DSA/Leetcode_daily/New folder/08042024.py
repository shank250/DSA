from collections import Counter

students = [1,1,0,0]
sandwiches = [0,1,0,1]

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        hm = Counter(students)
        for i in range(len(students)):
        	if hm[sandwiches[i]] < 0:
        		hm[sandwiches[i]] -= 1
    		else:
    			return hm[0] + hm[1]
		return 0

sol = Solution().countStudents(students, sandwiches)
print(sol)