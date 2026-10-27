class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        dict_map = {}
        for i in nums:
            if i %2 == 0:
                if i in dict_map:
                    dict_map[i] += 1
                else:
                    dict_map[i] = 1
        max_freq = 0
        ans = -1
        
        for num, count in dict_map.items():
            if count > max_freq:
                max_freq = count
                ans = num
            elif count == max_freq and num < ans:
                ans = num 
        return ans