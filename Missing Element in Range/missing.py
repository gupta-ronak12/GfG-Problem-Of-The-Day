class Solution:
    def missingRange(self, arr, low, high):
        
        present = [False] * (high - low + 1)
        
      
        for num in arr:
            if low <= num <= high:
                present[num - low] = True
   
        result = []
        for i in range(high - low + 1):
            if not present[i]:
                result.append(i + low)
        
        return result