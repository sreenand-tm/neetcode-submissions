class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        maxw=0
        while(i<j):
            water=(j-i)*min(heights[i],heights[j])
            if(water>maxw):
                maxw=water
            if(heights[i]<heights[j]):
                i=i+1
            else:
                j=j-1
        return maxw


        