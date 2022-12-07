from curses.ascii import isalnum
from hashlib import new
from turtle import left


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        There are two solutions to this problem. One we do it by reversing the str 
        and the other by using pointers
        """

        """
        Solution 1
        Create a new_str that will store the characters from the original str
        We are taking up memory for creating new_str object and the reverse of new_str at the end
        which can be improved
        Time complexity: O(n)
        """
        # new_str = ''
        # for char in s:
        #     # Considering the question has special characters and spaces we want
        #     # avoid, check if the char is alpha numeric
        #     if char.isalnum():
        #         new_str += char.lower()
        # # Check the newly created str which contains just lower alphabets and numbers
        # # with the reversed newly created str
        # return new_str == new_str[::-1]

        """
        Solution 2
        This solution uses left and right pointer to check for each index using while loop
        which saves the memory.
        Space Complexity: O(1)
        """
        # Create pointers which are indexes to help us compare characters from both sides
        # Left pointer increments whereas right pointer decrements
        left_pointer, right_pointer = 0, len(s) - 1
        while left_pointer < right_pointer:
            # Create a while loop for iterating left pointer until it reach a alnum char
            # and until left pointer is less than right pointer
            while left_pointer < right_pointer and not s[left_pointer].isalnum():
                # Increment the left pointer by 1
                left_pointer += 1
            # Create a while loop for iterating right pointer until it reacher a alnum character
            # and until it reaches a position of 1
            while right_pointer >= 1 and not s[right_pointer].isalnum():
                # Decrement the right pointer by 1
                right_pointer -= 1
            # In situations where there is no alnum char just other chars and
            # at this stage after execution of while loop on both left pointer
            # and right pointer indicates that it is an empty space which is a palindrome
            # []
            if not s[left_pointer].isalnum() or not s[right_pointer].isalnum():
                return True
            # If the character at left pointer and char at right pointer are not equal
            if s[left_pointer].lower() != s[right_pointer].lower():
                return False
            # Increment the left pointer by 1 and decrement the right pointer by 1
            left_pointer, right_pointer  = left_pointer + 1, right_pointer - 1
        return True
    
    def alpha_num(self, c: str) -> bool:
        """
        There can be instances where the interviewer would not like us to use the alnum() method
        to check if a char is alnum and would want us to implement something of our own.
        We can check if a character is alpha numeric or not using by using "ord" function which 
        return use the asic number.
        """
        return (
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')
        )

sol = Solution()
print(sol.isPalindrome(".,"))
