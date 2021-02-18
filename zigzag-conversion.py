from collections import defaultdict


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        s_dict = defaultdict(list)
        pointer = 1
        flag = -1
        for _s in s:
            s_dict[pointer].append(_s)
            if pointer == numRows or pointer == 1:
                flag *= -1
            pointer += flag
        ans = ''
        for s in sorted(s_dict.keys()):
            ans += ''.join(s_dict[s])
        return ans


