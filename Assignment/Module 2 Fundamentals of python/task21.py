# How memory is managed in Python? 
"""
Memory management in Python is handled automatically, which makes it easier for developers to focus on writing code without worrying about manual memory allocation and deallocation. 
Here are the key aspects of how Python manages memory:

Private Heap Space:
Python uses a private heap space for memory management. 
All Python objects and data structures are stored in this heap. 
The Python interpreter takes care of managing this private heap.


Memory Allocation: When a new object is created, Python dynamically allocates memory for it. 
The amount of memory allocated depends on the object type and size.

Reference Counting: Python uses a technique called reference counting to keep track of objects in memory. 
Each object has a reference count that indicates how many references point to it. 
When an object reference count drops to zero, it means the object is no longer in use and can be deallocated.

Garbage Collection: In addition to reference counting, Python has a built-in garbage collector that helps manage memory. 
The garbage collector periodically checks for objects that are no longer referenced and frees up the memory occupied by them. 
This helps in reclaiming memory that might not be immediately freed by reference counting alone.

Memory Fragmentation: Python manages memory fragmentation by keeping track of free memory blocks and allocating memory from these blocks when needed.
This helps in efficiently utilizing memory and reducing fragmentation.


"""

