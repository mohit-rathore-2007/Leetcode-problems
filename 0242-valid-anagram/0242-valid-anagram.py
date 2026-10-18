class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            

        s_lst = sorted(s)
        t_lst = sorted(t)
            
        return s_lst == t_lst