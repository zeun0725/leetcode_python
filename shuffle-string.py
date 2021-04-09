from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        indices_str = list(zip(s, indices))
        return ''.join([t[0] for t in sorted(indices_str, key=lambda x: x[1])])
