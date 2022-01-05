# Depth First Search

Just like what it sounds like: go down each branch as deep as possible before coming back up to explore other branches.


```python
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(V + E) time | O(V) space
    def depthFirstSearch(self, array):
		array.append(self.name)
        for child in self.children:
			child.depthFirstSearch(array)
		return array

graph = Node("A")

```