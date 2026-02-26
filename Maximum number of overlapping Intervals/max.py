class Solution:
    def overlapInt(self, arr):

        mp = {}

        for start, end in arr:
            mp[start] = mp.get(start, 0) + 1
            mp[end + 1] = mp.get(end + 1, 0) - 1

        count = 0
        ans = 0

        for key in sorted(mp):
            count += mp[key]
            ans = max(ans, count)

        return ans