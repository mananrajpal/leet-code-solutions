from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Solution 1: Iterartive Method
        In the iterative method we use two pointers curr and prev.
        The prev pointer is set to None and curr is set to head.
        We use while loop to iterate over the list by re-assiging the curr.next to previous
        and curr to prev and curr to curr.next using a temp variable. In the end prev becomes
        the head and can be returned
        Time complexity is O(n) and space complexity is O(1)
        """
        # # Initiate the previous and curr pointer
        # prev, curr = None, head

        # # Iterate until curr becomes None
        # while curr:
        #     # Store the reference of next from curr node in a temporary variable
        #     next = curr.next

        #     # Remove the original connection between the head and its next node to 
        #     # now the next pointing towards None which is previous in this instance
        #     curr.next = prev
            
        #     # Set the previous to the curr node
        #     prev = curr

        #     # Set the curr node to one which was next in the original list
        #     curr = next
        
        # # At the end of the while loopm curr node will be set to None and prev node 
        # # will be set to the first node which was the last node in the orginial list
        # # At the end the previous will the head node which we can return
        # return prev

        """
        Solution 2: Recursive Solution
        In the recursive solution method, we
        Time complexity is O(n) and space complexity O(n)
        """
        # Base Case
        if head is None:
            return None
        
        # Create a new variable that will hold reference to the new head, which
        # in this instance will be the last node of the original linked list
        # Lets set it to head for now
        new_head = head

        # We want to do a recursive call for each node that has pointer to next node
        if head.next:
            # Do a recursive call until the end is reached in which instance the last node
            # will become the new_head and will be passed on to the previous stacked calls
            # Example: Original Linked List [1, 2, 3] with 1 being the head, with our code
            # new_head will hold reference to node 3
            new_head = self.reverseList(head.next)

            # Now that the new_head is established, in each recursive step we want set the 
            # head to next value of its next node.
            # Example: Original Linked List [1, 2]. Since the next node is 2 we want to set 1
            # at the node(2).next = 1 so the new linked list will be [2, 1] with node 2 having
            # .next value set to node 1 and thus will be reverse the list
            head.next.next = head


        # Considering that we are reversing the list we want to break any connections of original linked list
        # otherwise with the reverse linked list with pointer from original linked list will cause recursive pointers
        # Example: Original Linked List [1, 2] has 1.next = 2 and 2.next = None but once the list is reversed with 
        # the code above the Reversed Linked List [2, 1] should have 1.next = None otherwise 2.next = 1 (from 
        # the new reversed list) and 1.next = 2 (from the original list)
        head.next = None

        # Return the newhead temp variable that holds references to the node that is the new head
        return new_head

node1 = ListNode(val=1)
node2 = ListNode(val=2)
node1.next = node2

sol = Solution()
result = sol.reverseList(node1)
val_list = []
while True:
    if result:
        val_list.append(result.val)
        result = result.next
    else:
        break
print(val_list)