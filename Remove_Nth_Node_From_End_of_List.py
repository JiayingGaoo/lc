# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def printListNode(self, head: ListNode):
        l1 = head
        while l1 != None:
            print(l1.val)
            l1 = l1.next
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l1 = head
        list_len = 0
        while l1 != None:
            list_len = list_len + 1
            l1 = l1.next
            # self.printListNode(head)
        print('list_len = ', list_len)
        if list_len < n:
            return None
        if list_len == n:
            return head.next
        l1 = head
        i = 0
        while l1 != None:
            if i == list_len - n - 1:
                print('cur: l1.val = ', l1.val)
                l2 = l1.next.next
                l1.next = l2
                break
            i = i + 1
            l1 = l1.next
        self.printListNode(head)
        return head


node_0 = ListNode(1)
node_1 = ListNode(2)
node_2 = ListNode(3)
node_3 = ListNode(4)
node_4 = ListNode(5)
node_0.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

Sol = Solution()
Sol.removeNthFromEnd(node_0, 2)
