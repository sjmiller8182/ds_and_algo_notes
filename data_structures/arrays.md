# Arrays

An array is a linear collection of data that are accessed by index starting at 0.

## Types of Arrays

* **Static** - Allocates a fixed amount of memeory equal to the requested size. Changing the size of the array requires reallocating memeory and copying the array.
* **Dynamic** - Allocates more than the requested memeory (commonly twice the requested amount). Appending the array is O(1) until the allocated memory is full. On the next append action, a new memory segment is allocated (again, generally twice what is required) and the array is copied to the new allocation, which is O(n). Since the copy operation is infrequent, appending at the end is generally O(1) for dynamic arrays.

## Operations and Complexity

* access element at given index: O(1)
* update element at given index: O(1)
* insert value at beginning or middle: O(n) - requires shifting down N elements
* insert value at end
    * static array (like C++): O(n)
    * dynamic array (like python): O(1) - generally (See dynamic arrays)
* remove value at beginning or middle: O(n) - requires shifting up N elements
* remove value at end: O(n)
* copy: O(n)
* traverse: O(n)

## Implementation

In python, the `list` object is a dynamic array.
