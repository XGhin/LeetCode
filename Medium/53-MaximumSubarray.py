class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        SomaMaxima = float('-inf')
        SomaAtual = 0
        
        for num in nums:
            SomaAtual += num
            
            if SomaAtual > SomaMaxima:
                SomaMaxima = SomaAtual
            
            if SomaAtual < 0:
                SomaAtual = 0
        
        return SomaMaxima