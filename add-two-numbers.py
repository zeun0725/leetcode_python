# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def getNumbers(self, listnode: ListNode) -> str:
        cur_node = listnode
        str_num = ''
        while cur_node:
            str_num += str(cur_node.val)
            cur_node = cur_node.next
        return str_num[::-1]
    
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_num = self.getNumbers(l1)
        l2_num = self.getNumbers(l2)
        listnode = str(int(l1_num) + int(l2_num))[::-1]
        node = ListNode(int(listnode[0]))
        cur_node = node
        for ln in listnode[1:]:
            new_node = ListNode(int(ln))
            node.next = new_node
            node = node.next
        return cur_node
        
        
            
        
        
