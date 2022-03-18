import numpy as np

class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_to_head(self, val):
        node = ListNode(val, self.head)
        self.head = node
        if self.tail is None:
            self.tail = self.head

    def insert_to_tail(self, val):
        node = ListNode(val, None)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def delete(self, node):
        if node == self.head:
            self.head = self.head.next
        else:
            p = self.head
            q = None
            while p is not node:
                q = p
                p = p.next

            q.next = p.next

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def reverse(self):
        p = self.head
        if p is None:
            return

        q, r = None, p.next
        while r is not None:
            p.next = q
            q = p
            p = r
            r = r.next

        p.next = q
        self.head = p

    def __str__(self):
        s = '->'
        p = self.head
        while p is not None:
            s += str(p.val) + '->'
            p = p.next

        s += '|'
        return s

class Stack:
    def __init__(self):
        self.list = List()

    def push(self, val):
        self.list.insert_to_head(val)

    def pop(self):
        if self.list.is_empty():
            return None
        else:
            return self.list.delete(self.list.head)

    def is_empty(self):
        return self.list.is_empty()

    def __str__(self):
        s = ''
        p = self.list.head
        while p is not None:
            s += str(p.val) + '\n'
            p = p.next

        return s

class Queue:
    def __init__(self):
        self.list = List()

    def enqueue(self, val):
        self.list.insert_to_tail(val)

    def dequeue(self):
        if self.list.is_empty():
            return None
        else:
            return self.list.delete(self.list.head)

    def is_empty(self):
        return self.list.is_empty()

    def __str__(self):
        s = ''
        p = self.list.head
        while p is not None:
            s += str(p.val) + '-'
            p = p.next

        return s[::-1]

class TreeNode:
    def __init__(self, val, parent, right, left):
        self.val = val
        self.parent = parent
        self.right = right
        self.left = left

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val, None, None, None)
        else:
            p = self.root
            q = None
            while p is not None:
                q = p
                if p.val > val:
                    p = p.left
                else:
                    p = p.right

            node = TreeNode(val, q, None, None)
            if q.val > val:
                q.left = node
            else:
                q.right = node

    def delete(self, node):
        if node.left is None or node.right is None:
            p = node
        else:
            p = self.next(node)

        if p.left is not None:
            q = p.left
        else:
            q = p.right

        if q is not None:
            q.parent = p.parent

        if p.parent is None:
            self.root = q
        else:
            if p == p.parent.left:
                p.parent.left = q
            else:
                p.parent.right = q

        if p != node:
            node.val = p.val

        return p

    def search(self, val):
        if self.root is None:
            return None
        else:
            p = self.root
            while p is not None:
                if p.val == val:
                    return p
                elif p.val > val:
                    p = p.left
                else:
                    p = p.right

            return None

    def next(self, node):
        if node.right is not None:
            return self.min(node.right)
        else:
            p = node.parent
            q = node
            while p is not None and p.right == q:
                q = p
                p = p.parent

            return p

    def min(self, node):
        p = node
        q = None
        while p is not None:
            q = p
            p = p.left

        return q

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    def dfs(self, s):
        if s is not None:
            print(s.val)
            self.dfs(s.left)
            self.dfs(s.right)

    def bfs(self):
        q = Queue()
        if not self.is_empty():
            q.enqueue(self.root)

        while not q.is_empty():
            node = q.dequeue()
            print(node.val)
            q.enqueue(node.left)
            q.enqueue(node.right)


class MaxHeap:
    def __init__(self, n):
        self.arr = np.empty(n)
        self.size = 0
        self.n = n

    def insert(self, val):
        if self.size < self.n:
            self.arr[self.size] = val
            i = self.size
            parent = (i - 1) // 2
            while i > 0 and self.arr[parent] < self.arr[i]:
                self.arr[i], self.arr[parent] = self.arr[parent], self.arr[i]
                i = parent
                parent = (i - 1) // 2

            self.size += 1

    def delete_max(self):
        if self.size > 0:
            max = self.arr[0]
            self.arr[0] = self.arr[self.size - 1]
            self.size -= 1
            self.heapify()
            return max
        else:
            return None

    def max(self):
        return self.arr[0]

    def heapify(self):
        i = 0
        while i < self.size:
            left = 2 * i + 1
            right = 2 * i + 2
            if left < self.size and self.arr[left] > self.arr[i]:
                largest = left
            else:
                largest = i

            if right < self.size and self.arr[right] > self.arr[largest]:
                largest = right

            if largest != i:
                self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
                i = largest
            else:
                break
