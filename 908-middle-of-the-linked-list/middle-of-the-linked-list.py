# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        slow, fast = head, head

        # Move fast pointer 2 steps and slow pointer 1 step
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Slow pointer will now be at the middle node
        return slow

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Test cases
sol = Solution()

# Example 1: [1,2,3,4,5]
head = create_linked_list([1, 2, 3, 4, 5])
middle = sol.middleNode(head)
print(middle.val)  # Output: 3

# Example 2: [1,2,3,4,5,6]
head = create_linked_list([1, 2, 3, 4, 5, 6])
middle = sol.middleNode(head)
print(middle.val)  # Output: 4

        