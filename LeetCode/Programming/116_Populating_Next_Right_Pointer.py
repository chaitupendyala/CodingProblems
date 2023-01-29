from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        queue1, queue2 = [], []
        queue1.append(root)
        queue2.append(root.left)
        queue2.append(root.right)
        while len(queue1) != 0 or len(queue2) != 0:
            for i in range(len(queue1)-1):
                if queue1[i] and queue1[i].left:
                    queue2.append(queue1[i].left)
                if queue1[i] and queue1[i].right:
                    queue2.append(queue1[i].right)
                if queue1[i]:
                    queue1[i].next = queue1[i+1]
            if len(queue1) > 1:
                if queue1[-1] and queue1[-1].left:
                    queue2.append(queue1[-1].left)
                if queue1[-1] and queue1[-1].right:
                    queue2.append(queue1[-1].right)
            queue1 = queue2
            queue2 = []
        return root