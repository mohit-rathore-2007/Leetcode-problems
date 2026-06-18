class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for char in s:
            if ("a" <= char <= "z") or ("A" <= char <= "Z") or ("0" <= char <="9"):
                new += char.lower()

        return new == new [::-1]