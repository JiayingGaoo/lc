# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def reverse(self, input_list: list):
        len_list = len(input_list)
        for i in range(0, int(len_list/2)):
            temp_val = input_list[i]
            input_list[i] = input_list[len_list - 1 - i]
            input_list[len_list - 1 - i] = temp_val
        return input_list

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # first, obtaining the int digit for l1 and l2, denoted as i1 and i2
        # l1: 2->4->3: i1 = 342
        # l2: 5->6->4: i2 = 465
        # then: i1 + i2 = i_sum = 807
        # According to i_sum, give the listnode 7->0->8
        list_1 = []
        list_2 = []
        while l1 is not None:
            list_1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            list_2.append(l2.val)
            l2 = l2.next
        list_1 = self.reverse(list_1)
        list_2 = self.reverse(list_2)
        str_1 = ''
        str_2 = ''
        for l in list_1:
            str_1 = str_1 + str(l)
        for l in list_2:
            str_2 = str_2 + str(l)
        list_sum = list(str(int(str_1) + int(str_2)))
        list_sum = self.reverse(list_sum)
        print('list_sum = ', list_sum)
        head = ListNode(int(list_sum[0]))
        l_sum = head
        i = 1
        while i < len(list_sum):
            l_sum.next = ListNode(int(list_sum[i]))
            l_sum = l_sum.next
            i = i + 1
        l_sum.next = None
        return head


# test_node_1
test_l1_node_1 = ListNode(2)
test_l1_node_2 = ListNode(4)
test_l1_node_3 = ListNode(3)
test_l1_node_1.next = test_l1_node_2
test_l1_node_2.next = test_l1_node_3
# test_node_2
test_l2_node_1 = ListNode(5)
test_l2_node_2 = ListNode(6)
test_l2_node_3 = ListNode(4)
test_l2_node_1.next = test_l2_node_2
test_l2_node_2.next = test_l2_node_3

Sol = Solution()
Sol.addTwoNumbers(test_l1_node_1, test_l2_node_1)


Sol = Solution()