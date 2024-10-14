# 2402. Meeting Rooms III

n = 2
meetings = [[0,10],[1,5],[2,7],[3,4]]

startDuration = {} #start time: duration
for start, end in meetings:
    startDuration[start] = (end-start)

print(startDuration)

roomMeetFreq = [0 for i in range(n)]
busyRooms = [False for i in range(n)]

while startDuration:
    time = 0
    try:
        avalRoomIndex = busyRooms.index(True)
        
    except ValueError:
        pass
    time += 1