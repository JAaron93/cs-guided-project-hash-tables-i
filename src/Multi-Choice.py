'''
What is the average time complexity of the following operations on a hash table:

    - lookup
    - insert
    - delete
'''

# Answer:
# O(1)

'''
What are the primary weaknesses of a hash table?
'''

# Answer:
# If you have the key, you can quickly retrieve the value. However, if you have the value and need to get the keys, that is a slow O(n) operation.

'''
What is the most common strategy for dealing with hash collisions?
'''

# Answer:
# Not storing the value directly at an index of the hash table's array. Instead, the array index stores a pointer to a linked list. Each node in the linked list stores a key, value, and a pointer to the next item in the linked list.