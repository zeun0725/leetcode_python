# https://leetcode.com/problems/reorder-data-in-log-files/submissions/
from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = [log for log in logs if log[-1].isalpha()]
        letter_logs.sort(key=lambda x: (x.split(' ')[1:], x.split(' ')[0]))
        letter_logs += [log for log in logs if log not in letter_logs]
        return letter_logs