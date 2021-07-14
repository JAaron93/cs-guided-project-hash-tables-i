'''
ou are given a non-empty array of integers.

One element appears exactly once, with every other element appearing at least twice, perhaps more.

Write a function that can find and return the element that appears exactly once.

Example 1:

Input: [1,1,2,1]
Output: 2
Example 2:

Input: [1,2,1,2,1,2,80]
Output: 80
Note: You should be able to develop a solution that has O(n) time complexity.
'''

def csFindTheSingleNumber(nums):
    for n in nums:
        # If every element appears exactly once, we only need to confirm that with this if statement which utilizes
        # the .count() method with our iterable passed into it. This confirms that this element only appears once.
        # We then return n to see which of these elements is only listed once.
        if nums.count(n) == 1:
            return n