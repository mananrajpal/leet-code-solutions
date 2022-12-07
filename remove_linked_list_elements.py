from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Solution 1: Iteration
        This solution requires us to create a dummy node which has a next value to head which 
        in this instance is -1. Using two pointers, initiating one pointer (prev) pointing to dummy node to deal
        with cases where the head can be the val required to be removed such that dummy node with pointer(prev) can have
        its .next value can point towards that node whose .val != val required.
        The second pointer curr is basically replica of head node which iterates over the entire Linked List.
        In each iteration if curr.val == val keep iterating the pointer of prev node to the curr node until a node 
        is reached whose .val != val which than sets the prev pointer to the curr pointer
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Create a dummy node with which we can get the head of the Linked List 
        # using dummy.next() at the end
        dummy_node = ListNode(-1, head)

        # Initiate the second pointer variable, refering to the -1 dummy node object initially
        prev, curr = dummy_node, head
        while curr:
            # Initially when the prev variable is still referencing the -1 node,
            # its .next value will keep incrementing until a node is reached where
            # that nodes.val != val which is required to be removed, in which instance
            # prev is set to the new node i.e. refers to the new node but initially
            # its .next connected the node at -1 to whatever node whose val != required_val
            if curr.val != val:
                prev = curr
            else:
                prev.next = curr.next
            # Keep on incrementing the head to the next node until the end where it becomes None
            curr = curr.next
        return dummy_node.next

        # """
        # Solution 2: Recursion
        # The solution again starts with base case which is to return None once the end is reached.
        # The sub-problem of the solution is to either return the head.next if head.val == val else head
        # which will be assigned to head.next so that 
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # """
        # # Base Case
        # if head is None:
        #     return None

        # # The sub-problem of this solution is to reach the end
        # # and if the head.val != val, return head otherwise return head.next
        # head.next = self.removeElements(head.next, val)
        # return head.next if head.val == val else head

node5 = ListNode(val=4)
node4 = ListNode(val=3, next=node5)
node3 = ListNode(val=2, next=node4)
node2 = ListNode(val=1, next=node3)
node1 = ListNode(val=1, next=node2)
sol = Solution()
result = sol.removeElements(node1, 1)
val_list = []
while True:
    if result:
        val_list.append(result.val)
        result = result.next
    else:
        break
print(val_list)