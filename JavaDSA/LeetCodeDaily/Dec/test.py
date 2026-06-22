class Solution:
    def findMinimumTime(self, strength, K: int) -> int:
        n = len(strength)
        strength = sorted(strength, reverse=True)

        t , e, x, broken = 0, 0, 1, 0
        while(n != broken):
            e += x
            t += 1
            for ind in range(n):
                if strength[ind] != -1 and strength[ind] <= e:
                    strength[ind] = -1
                    x += K
                    e = 0
                    broken += 1
                    break

        return t
    
    def findAllthePermutations(arr: list[int], index: int) -> list[list[int]]:
        # select onw index and flip/swap it will all the remaining indexs
        # do this swaping untill n swaps are made

        
sol = Solution().findMinimumTime([7,3,6,18,22,50], 4)
