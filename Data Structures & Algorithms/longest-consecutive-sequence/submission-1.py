class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        cpy=list(set(nums))
        cpy.sort()

        size=len(cpy)
        count=1
        max_count=1

        i=0

        while i+1<size:

            if cpy[i]+1==cpy[i+1]:
                count=count+1

            else:
                count=1

            if count>max_count:
                max_count=count

            i=i+1

        return max_count