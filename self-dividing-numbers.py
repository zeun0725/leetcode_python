class Solution:
    def getDividingNumbers(self, num: str) -> bool:
        for n in num:
            if int(n) == 0 or int(num) % int(n) != 0:
                return False
        return True
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        self_div = []
        for i in range(left, right + 1):
            if i < 10:
                self_div.append(i)
                continue
            flag = self.getDividingNumbers(str(i))
            if flag:
                self_div.append(i)
        return self_div
            
                    
        
