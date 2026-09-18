class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total=(len(nums1)+len(nums2))
        if( total %2==0):
            m1=total//2-1
            m2=total//2
        else:
            m1=total//2
            m2=total//2
        n=0
        i=0
        j=0
        prev=[]
        curr=0
        while(n<=m2):
            if(i==len(nums1)):
                prev.append(nums2[j])
                j=j+1
                n=n+1
            elif(j==len(nums2)):
                prev.append(nums1[i])
                i=i+1
                n=n+1
            elif(nums1[i]<nums2[j]):
                prev.append(nums1[i])
                i=i+1
                n=n+1
            else:
                prev.append(nums2[j])
                j=j+1
                n=n+1
        if(total %2==0):
            return((prev[m1]+prev[m2])/2)
        else:
            return(prev[m1])





        