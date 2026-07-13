class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):

            if int(num[i])%2 != 0:
                result = ""

                for j in range(i+1):
                    result = result +num[j]

                return result 
        return ""
