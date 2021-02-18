# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def get_length_node(self, head: ListNode) -> int:
        n_leng = 0
        while head:
            n_leng += 1
            head = head.next
        return n_leng

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur_node = head
        n_leng = self.get_length_node(head) - n
        if n_leng == 0:
            return cur_node.next
        pointer = 1
        while head:
            if pointer == n_leng:
                head.next = head.next.next
            head = head.next
            pointer += 1
        return cur_node

