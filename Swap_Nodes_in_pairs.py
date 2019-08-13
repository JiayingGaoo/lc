# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def printNodes(self, head: ListNode) -> ListNode:
        _l = head
        while _l is not None:
            print(_l.val)
            _l = _l.next

    def swapPairs(self, head: ListNode) -> ListNode:
        _even_head = head
        if head is None:
            return None
        if head.next is None:
            return head

        _odd_head = head.next
        _even = _even_head
        _odd = _odd_head
        _l = head

        i = 0
        while _l is not None:
            if i % 2 == 0 and i > 0:
                _odd.next = _l.next
                _odd = _odd.next
            if i % 2 == 1:
                _even.next = _l.next
                _even = _even.next
            _l = _l.next
            i = i + 1
        _even = None
        _odd = None
        # print('_even')
        # self.printNodes(_even_head)
        # print('_odd')
        # self.printNodes(_odd_head)

        _even = _even_head
        _odd = _odd_head
        _l = _odd_head

        while _odd is not None or _even is not None:
            _odd = _odd.next
            # print(_l.val)

            _l.next = _even
            _even = _even.next

            _l = _l.next
            # print(_l.val)
            if _odd is None:
                break
            _l.next = _odd
            _l = _l.next
            if _even is None:
                break

        print('result:')
        self.printNodes(_odd_head)
        return _odd_head


node_0 = ListNode(0)
node_1 = ListNode(1)
node_2 = ListNode(2)
# node_3 = ListNode(3)
# node_4 = ListNode(4)
# node_5 = ListNode(5)
# node_6 = ListNode(6)
# node_7 = ListNode(7)
# node_8 = ListNode(8)
# node_9 = ListNode(9)
# node_10 = ListNode(10)
# node_11 = ListNode(11)

node_0.next = node_1
node_1.next = node_2
# node_2.next = node_3
# node_3.next = node_4
# node_4.next = node_5
# node_5.next = node_6
# node_6.next = node_7
# node_7.next = node_8
# node_8.next = node_9
# node_9.next = node_10
# node_10.next = node_11

Sol = Solution()
# Sol.printNodes(node_1)
Sol.swapPairs(node_0)
