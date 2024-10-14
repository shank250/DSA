# Insert Delete GetRandom 
import random
class RandomizedSet:

    def __init__(self):
        self.s = set()
        self.n = 0

    def insert(self, val: int) -> bool:
        if val in self.s:
            return False
        else:
            self.s.add(val)
            self.n += 1
            return True
        
    def remove(self, val: int) -> bool:
        if val in self.s:
            self.s.discard(val)
            self.n -= 1
            return True
        else:
            return False

    def getRandom(self) -> int:
        index = random.randint(0, self.n-1)
        list1 = list(self.s)
        return list1[index]