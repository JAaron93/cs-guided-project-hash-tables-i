'''
Given a string text, you need to use the characters of text to form as many instances of the word "lambda" as possible.

You can use each character in text at most once.

Write a function that returns the maximum number of instances of "lambda" that can be formed.

Example 1:

Input: text = "mbxcdatlas"
Output: 1
Example 2:

Input: text = "lalaaxcmbdtsumbdav"
Output: 2
Example 3:

Input: text = "sctlamb"
Output: 0
Notes:

text consists of lowercase English characters only
'''

def csMaxNumberOfLambdas(text):
    # I can assign a string to a variable. And iterate over our input string to confirm if it can be filled a certain amount of times. No need to check if each character/letter is being counted and confirming if its all once or more, save for 'a' needing to be twice or double/triple/etc that.
    lambd = 'lambda'
    # Creating empty list to append to
    lambd_lst = []
    for i in lambd:
        # Using .count() method with our iterable as its argument (That is what's being counted) and filling those counts to our empty list
        lambd_lst.append(text.count(i))
        # When ran the first time, this returned the count of each character/letter.
        # Now when we return with the min() function, it returns the lowest number. This works considering that 'a' will always be double that of the other letters, we just need to return the number of times any of the other letters appear. If there's a count of 0 for any of these letters (meaning there aren't enough to letters to spell 'lambda' even once) then that is returned 
    return min(lambd_lst)
