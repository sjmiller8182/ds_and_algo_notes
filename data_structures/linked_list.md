# Linked List

A linked list is a collection of nodes that are connected to each other by references.

## Types of Linked Lists

* **Singlely-Linked** - In a singlely-linked linkedlist, the nodes only contain a refernce to the next node. The linkedlist starts at a node called the "head" and ends at the null reference.
* **Double-Linked** - In a double-linked linkedlist, the nodes contain a reference to the next node and the previous node. The linkedlist object will maintain a reference to the "head" (first) and "tail" (last) nodes.

**Node**

```python
class Node:
    """
    This node supports both single-linked LLs and doubly-linked LLs.
    """
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node
    
    def __repr__(self) -> str:
        n = self.next.value if self.next is not None else None
        prev = self.prev.value if self.prev is not None else None
        return "Node: value: " + str(self.value) \
            + ", next: " + str(n) \
            + ", prev: " + str(prev)
```

**Singley-Linked Linked List**

```python
from typing import List

class LinkedList:
    """
    Singley-linked linked list
    """
    def __init__(self, nodes: List[Node] = None):
        self.head = None

        if nodes:
            for idx in range(len(nodes)):
                # push nodes into linked list in reverse from head
                self.push_head(nodes[len(nodes) - 1 - idx])
    
    def push_end(self, node: Node) -> None:
        if self.head is None:
            self.head = node
        else:
            # scan to end of linked list
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            # at this point current_node will be 
            # the last node in the list becasue
            # current_node.next is None
            # place the new node here
            current.next = node
    
    def push_head(self, node: Node) -> None:
        if self.head is None:
            self.head = node
        else:
            old_head = self.head
            self.head = node
            node.next = old_head
```

## Operations and Complexity

* get value: O(n) T, O(1) S
* set value: O(n) T, O(1) S
* initialize (given elements): O(n) ST
* copy: O(n) ST
* traverse: O(n) T, O(1) S
* insert at head: O(1) ST
* insert at end: O(n) T, O(1) S
