"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        cur = head
        while cur:
            clone = Node(cur.val, cur.next)
            cur.next = clone
            cur = clone.next
        cur = head
        while cur:
            if cur.random: cur.next.random = cur.random.next
            cur = cur.next.next
        dummy = Node(0); tail = dummy; cur = head
        while cur:
            clone = cur.next
            cur.next = clone.next
            tail.next = clone; tail = clone
            cur = cur.next
        return dummy.next