from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Solution is using two pointers. Since head of the new Linked List can be from either of the two
        given Linked List, we create a dummy node and whatever node is the smallest of the two given 
        list is set to as the next of dummy node which we return at the end as the head.
        """
        dummy_node: ListNode =  ListNode()
        curr = dummy_node
        
        # Create a while loop that executes until one of the list finishes and the other remains
        # as it is quite possible that two list can of same length and can be of different length
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
        
        # Since the while loop terminates if one of the list node reaches None, it is possible that
        # other list has nodes that still need to be iterated upon but since they are already sorted
        # we dont need to iterate till the end, we can just set the .next val of our last node i.e. current var
        # to the next node of the list node
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        return dummy_node.next
        

# Linked List 1
# [1, 4, 5, 6]
node7 = ListNode(val=6)
node6 = ListNode(val=5, next=node7)
node5 = ListNode(val=4, next=node6)
node4 = ListNode(val=1, next=node5)

# Linked List 2
# [1, 2, 3]
node3 = ListNode(val=3)
node2 = ListNode(val=2, next=node3)
node1 = ListNode(val=1, next=node2)
sol = Solution()
result = sol.mergeTwoLists(node1, node4)
val_list = []
while True:
    if result:
        val_list.append(result.val)
        result = result.next
    else:
        break
print(val_list)