class Solution:

    def trap(self, height: List[int]) -> int:

        trap = 0
        left = 0
        right = len(height) - 1
        mah1 = 0
        mah2 = 0

        for i in range(len(height)):

            if height[left] <= height[right]:

                if height[left] >= mah1:
                    mah1 = height[left]
                else:
                    trap = trap + mah1 - height[left]

                left += 1

            else:

                if height[right] >= mah2:
                    mah2 = height[right]
                else:
                    trap = trap + mah2 - height[right]

                right -= 1

        return trap