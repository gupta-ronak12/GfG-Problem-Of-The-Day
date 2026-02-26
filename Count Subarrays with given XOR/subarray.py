class Solution:
    def subarrayXor(self, arr, k):
        res = 0
        prefXOR = 0
        mp = {}
        for val in arr:
            prefXOR ^= val
            if prefXOR == k:
                res += 1
            res += mp.get(prefXOR ^ k, 0)
            mp[prefXOR] = mp.get(prefXOR, 0) + 1

        return res