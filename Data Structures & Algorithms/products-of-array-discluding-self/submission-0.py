class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                product *= nums[i]

        answer = [0] * len(nums)

        if zeros > 1:
            return answer

        for i in range(len(nums)):
            if zeros == 1:
                if nums[i] == 0:
                    answer[i] = product
                else:
                    answer[i] = 0
            else:
                answer[i] = product // nums[i]

        return answer