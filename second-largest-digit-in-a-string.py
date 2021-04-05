import re

class Solution:
    def secondHighest(self, s: str) -> int:
        s_list = sorted(list(set(re.sub('[a-z]+', '', s))))
        return int(s_list[-2]) if s_list.__len__() >= 2 and s_list[-1].__ne__(s_list[-2]) else -1

