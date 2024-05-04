# 514. Freedom Trail

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # list having all the possible characters
        # a funciton which can find out minimum steps required to steps required to reach that char in ring
        def minimumStep(ring, char) -> int:
            rtn = 0
            frontIndex = ring.find(char)
            print("Before:", ring)
            print("frontIndex",frontIndex)
            newListofRing = list(reversed(ring))
            newListofRingStr = "".join(newListofRing)
            lastIndex = newListofRingStr.find(char)
            print("lastIndex", lastIndex)
            if frontIndex <= lastIndex:
                # swap for frontIndex steps left to right
                firstStr, secondStr = ring[:frontIndex], ring[frontIndex:]
                ring = secondStr + firstStr
                rtn += frontIndex
            else:
                # moce the last element in fron and rearrange it for lastIndex times
                firstStr, secondStr = ring[:len(ring) - lastIndex -1], ring[len(ring) - lastIndex-1:]
                ring = secondStr + firstStr
                rtn += lastIndex + 1
            print("After:", ring)
            print("swap:", rtn)
            return rtn, ring
        # print(minimumStep(ring, key[0]))
        # rearrangment of the string as clockwise or anticlockwise
        step = 0
        for ele in key:
            tmp, ring = minimumStep(ring, ele)
            step += tmp
            step += 1
            print("Steps: ", step)
            print("-----------------------------")
        return step
        # then one more step for pressing the button 
        # and then we will pass on to the next key str
sol = Solution().findRotateSteps("iotfo","fioot")
print("Answer: ",sol)