class Solution(object):
    def isPalindrome(self, x):
        num_str = str(x)

        reversed_s = num_str[::-1]

        if num_str == reversed_s:
            return True
        else:
            return False