# 19. Remove Nth Node From End of List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def __init__(self):
        self.head = ListNode(1)
        self.head.next = ListNode(2)
        self.head.next.next = ListNode(3)
        self.head.next.next.next = ListNode(4)
        self.head.next.next.next.next = ListNode(5)

    def removeNthFromEnd(self, head, n: int):
        tmphead = head
        lenght = 0
        while head:
            lenght += 1
            head = head.next
        print("Length:", lenght)
        requiredindex = lenght - n
        n, head = 0, tmphead
        prev = None
        while head:
            if n == requiredindex:
                if prev == None:
                    tmphead = None
                else:
                    # del the current node
                    prev.next = head.next
                break
            prev = head
            head = head.next
            n += 1
        
        while tmphead:
            print(tmphead.val)
            tmphead = tmphead.next
        return tmphead
solutionClass = Solution()
print(solutionClass.removeNthFromEnd(solutionClass.head, 2))

