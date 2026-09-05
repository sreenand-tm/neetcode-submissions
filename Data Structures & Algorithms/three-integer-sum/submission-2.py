class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        out = []

        for i in range(len(nums)):

            k = i + 1
            j = len(nums) - 1

            while k < j:

                if nums[i] + nums[j] + nums[k] == 0:

                    triplet = [nums[i], nums[j], nums[k]]

                    if triplet not in out:
                        out.append(triplet)

                    k = k + 1
                    j = j - 1

                elif nums[i] + nums[j] + nums[k] > 0:
                    j = j - 1

                else:
                    k = k + 1

        return out
