# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        current_node = A
        prev_node = None
        while current_node is not None:
            forward_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = forward_node
        return prev_node
