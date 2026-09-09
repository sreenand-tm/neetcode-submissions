class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            k = (l + r) // 2

            if target == nums[k]:
                return k

            elif target > nums[k]:
                l = k + 1

            else:
                r = k - 1

        return -1