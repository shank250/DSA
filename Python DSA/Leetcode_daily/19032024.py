
# 621. Task Scheduler
# Input: tasks = ["A","C","A","B","D","B"], n = 1
# Output: 6

# Example 3:
# Input: tasks = ["A","A","A", "B","B","B"], n = 3
# Output: 10

tasks = ["A","A","A","B","B","B"]
n = 2

from collections import Counter

hm = Counter(tasks)
newTasks = []
