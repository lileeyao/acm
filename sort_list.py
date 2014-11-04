# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        #!/usr/bin/python
        if head is None:
            return None
        if head.next is None:
            return head

        length = 0
        it = head
        while it is not None:
            length = length + 1
            it = it.next

        return self.merge_sort(head, length)

    def merge_sort(self, head, length):
        if length == 1:
            tmp = head
            head = head.next
            tmp.next = None
            return tmp

        leftHead = self.merge_sort(head, length / 2)
        rightHead = self.merge_sort(head, length - length / 2)

        return self.merge(leftHead, rightHead)

    def merge(self, first, second):
        head = ListNode(0)
        head_ori = head
        while first is not None or second is not None:
            fv = sv = 99999999
            if first is not None and second is None:
                fv = first.val
            elif first is None and second is not None:
                sv = second.val
            elif first is not None and second is not None:
                fv = first.val
                sv = second.val

            if fv <= sv:
                head.next = first
                first = first.next
            else:
                head.next = second
                second = second.next
            head = head.next

        return head_ori.next

sol = Solution()
node1 = ListNode(2)
node2 = ListNode(1)
node1.next = node2
node2.next = None
sol.sortList(node1)
