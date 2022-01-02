"""
LinkedList DS
"""

from typing import Any, Iterable, Union

class Node:
    """
    Node class for S/D linkedlist
    """
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:
        n = self.next.value if self.next is not None else None
        prev = self.prev.value if self.prev is not None else None
        return "Node: value: " + str(self.value) \
            + ", next: " + str(n) \
            + ", prev: " + str(prev)
    
    def __str__(self) -> str:
        return self.__repr__()


class LinkedList:
    """
    A linked list
    """
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def to_list(self):
        output = []
        node = self.head
        while node is not None:
            output.append(node.value)
            node = node.next
        return output

    def pprint(self):
        print("LinkedList:", self.to_list())

    def _coerce_to_node(self, value):
        if isinstance(value, Node):
            return value
        else:
            return Node(value)

    def _get_tail(self) -> Node:
        if self.head is None:
            return self.head
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            return node

    def push_front(self, new_node: Union[Node, Any]):
        node = self._coerce_to_node(new_node)
        
        old_head = self.head
        node.next = old_head
        self.head = node
        
    def push_back(self, new_node: Union[Node, Any]):
        self.size += 1
        if self.head is None:
            self.head = self._coerce_to_node(new_node)
        else:
            node = self._get_tail()
            node.next = self._coerce_to_node(new_node)

    def pop_front(self):
        if self.head is None:
            return self.head

        popped = self.head.value
        self.head = self.head.next
        return popped
    
    def pop_back(self):
        if self.head is None:
            return self.head

        if self.head.next is None:
            return self.head

        node = self.head
        while node.next is not None:
            prev = node
            node = node.next
        popped = node.value
        prev.next = None
        return popped

    def nth_from_end(self, n):
        if n >= len(self):
            raise IndexError()
        else:
            current_node = self.head
            for _ in range(0, len(self) - 1 - n):
                current_node = current_node.next
            return current_node.value

    def reverse(self):
        if self.head is None:
            return None

        previous = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous
            previous = current_node
            current_node = next_node
        self.head = previous



def create_linked_list(values: Iterable):
    """
    Create a linked list from an iterable
    """

    ll = LinkedList()

    for value in values:
        ll.push_back(value)

    return ll
