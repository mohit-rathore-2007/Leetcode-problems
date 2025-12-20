class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)


        if s_len != t_len:
            return False

        else:
            s_lst = list(s)
            t_lst = list(t)

            s_lst.sort()
            t_lst.sort()

            if s_lst == t_lst:
                return True
            else:
                return False