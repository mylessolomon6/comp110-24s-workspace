"""Practicing Node."""

from __future__ import annotations

class Node:

    date: int
    next: Node

    def __init__(self, data: int, next: Node):
        self.data = data
        self.next = next

node_c: Node = Node(7, None)
node_b: Node = Node(6, node_c)
node_a: Node = Node(5, node_b)

print(node_a.data)
print(node_b.data)
    #node_b IS node.a.next
print(node_c.data)
print(node_a.next.next.data) # node_c IS node.a.next.next
print(node_c.next)
