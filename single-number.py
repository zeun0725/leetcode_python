from collections import Counter
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for cnt in Counter(nums).items():
            if cnt[1]==1:
                return cnt[0]
