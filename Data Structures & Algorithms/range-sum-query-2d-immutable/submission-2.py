class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.arr=[]
        i=0
        sum=0
        while i<len(matrix):
            rarr=[]
            j=0
            sum=0
            while j<len(matrix[0]):
                
                sum=sum+matrix[i][j]
                rarr.append(sum)
                j+=1

            self.arr.append(rarr)
            i+=1






    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total=0
        for i in range(row1,row2+1):
            if col1==0:
                total+=self.arr[i][col2]-0
            else:
                total+=self.arr[i][col2]-self.arr[i][col1-1]
        
            
        return total



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)