class Solution:
    def inversionCount(self, arr):
        
        def merge_sort(left, right):
            if left >= right:
                return 0

            mid = (left + right) // 2

            inv_count = merge_sort(left, mid)
            inv_count += merge_sort(mid + 1, right)

            temp = []
            i, j = left, mid + 1

            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    inv_count += (mid - i + 1)
                    j += 1

            while i <= mid:
                temp.append(arr[i])
                i += 1

            while j <= right:
                temp.append(arr[j])
                j += 1

            arr[left:right + 1] = temp

            return inv_count

        return merge_sort(0, len(arr) - 1)