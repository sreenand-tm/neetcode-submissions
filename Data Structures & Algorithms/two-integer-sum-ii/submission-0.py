class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        ans = []

        for i in range(len(numbers)):

            if numbers[i] + numbers[j] == target:
                ans.append(i + 1)
                ans.append(j + 1)
                return ans

            while numbers[i] + numbers[j] > target:
                j = j - 1

                if numbers[i] + numbers[j] == target:
                    ans.append(i + 1)
                    ans.append(j + 1)
                    return ans

        return ans
