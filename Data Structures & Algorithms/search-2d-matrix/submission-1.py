class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        col=len(matrix[0])-1
        l=0
        r=rows-1
        while(l<=r):
            k=(l+r)//2
            if(target == matrix[k][col]):
                return True
            elif(target>matrix[k][col]):
                l=k+1
            elif(target<matrix[k][col]):
                r=k-1
        row=l
        if row >= rows:
            return False
        l=0
        r=col-1
        while(l<=r):
            k=(l+r)//2
            if(target == matrix[row][k]):
                return True
            elif(target>matrix[row][k]):
                l=k+1
            elif(target<matrix[row][k]):
                r=k-1
        return False

        