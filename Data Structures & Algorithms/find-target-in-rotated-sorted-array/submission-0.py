class Solution:

    def search(self, nums: List[int], target: int) -> int:

        i = 0
        j = len(nums) - 1
        mid = (i + j) // 2
        found = False

        while (i <= j):

            if (nums[mid] == target):
                found = True
                return mid

            elif (nums[i] <= nums[mid]):

                if (nums[i] <= target < nums[mid]):
                    j = mid - 1
                    mid = (i + j) // 2

                else:
                    i = mid + 1
                    mid = (i + j) // 2

            elif (nums[j] >= nums[mid]):

                if (nums[mid] < target <= nums[j]):
                    i = mid + 1
                    mid = (i + j) // 2

                else:
                    j = mid - 1
                    mid = (i + j) // 2

        return -1