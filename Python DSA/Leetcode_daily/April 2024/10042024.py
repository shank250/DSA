# 950. Reveal Cards In Increasing Order

deck = [17,13,11,2,3,5,7]

class Solution:
    def deckRevealedIncreasing(self, deck) -> list[int]:
        should_paste = True
        ptr, count, length = 0, 0, len(deck)
        rtn = [None]*length
        sorted_cards = sorted(deck)
        while count < length:
            if ptr >= length:
                ptr = 0
            print(ptr)
            if rtn[ptr] == None:
                if should_paste:
                    rtn[ptr] = sorted_cards.pop(0)
                    should_paste = False
                    count += 1

                else:
                    should_paste = True
            ptr += 1
        print(rtn)
sol = Solution().deckRevealedIncreasing(deck)
