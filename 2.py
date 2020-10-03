# leet code - problem - 2
# l1 = [2,4,3], l2 = [5,6,4]
# 342 + 465 = 807
# iterate l1 and l2 simultaneously , using pointer p1 and p2 respectively
# if there is no element in any one of the list then imagine a 0
# add the individual numbers and if carry is found use the carry
# once both p1 and p2 have reached end , then stop 

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def printList(self, l1):
        while l1 is not None:
            print("{}".format(l1.val)),
            l1 = l1.next
            if l1:
                print("-->"),

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        p1 = l1
        p2 = l2
        out = None
        carry = 0
        firstNode = None
        lastNode = None

        while True:
            if p1:
                n1 = p1.val
                p1 = p1.next
            else:
                n1 = 0

            if p2:
                n2 = p2.val
                p2 = p2.next
            else:
                n2 = 0

            s = carry + n1 + n2 
            if s >= 10:
                s -= 10
                carry = 1
            else:
                carry = 0

            if lastNode:
                node = ListNode(s, None)
                lastNode.next = node 
                lastNode = node
            else:
                firstNode = ListNode(s, None)
                lastNode = firstNode

            if p1 is None and p2 is None:
                break

        if carry:
            node = ListNode(carry, None)
            lastNode.next = node 
            lastNode = node

        return firstNode


if __name__ == "__main__":
    p = ListNode(3,None)
    p = ListNode(4, p)
    p = ListNode(2, p)
    l1 = p

    p = ListNode(4,None)
    p = ListNode(6, p)
    p = ListNode(5, p)
    l2 = p

    m=Solution()
    # (2 -> 4 -> 3) + (5 -> 6 -> 4)
    # 465 + 342 = 807
    # 807
    res = m.addTwoNumbers(l1,l2)
    m.printList(res)
