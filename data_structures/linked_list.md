# Linked List

A linked list is a collection of nodes that are connected to each other by references.

## Types of Linked Lists

* **Singlely-Linked** - In a singlely-linked linkedlist, the nodes only contain a refernce to the next node. The linkedlist starts at a node called the "head" and ends at the null reference.
* **Double-Linked** - In a double-linked linkedlist, the nodes contain a reference to the next node and the previous node. The linkedlist object will maintain a reference to the "head" (first) and "tail" (last) nodes.

**Node**

```python
class Node:
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

## Operations and Complexity

