class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
       rows=len(grid)
       col=len(grid[0])
       count=0 
       
       
       for r in range(rows-2):
         for c in range(col-2):
            if self.magicsquare(grid,r,c):
                count+=1
       return count

    def magicsquare(self,grid,r,c):
        if grid[r+1][c+1] !=5:
            return False
        
        seen=set()
        for i in range(r,r+3):
            for j in range(c,c+3):
                val=grid[i][j]
                if val<1 or val > 9 or val in seen:
                    return False
                seen.add(val) 


        for i in range(3):
            if sum(grid[r+i][c:c+3] )!=15:
                return False
        
        for j in range(3):
            if grid[r][c+j] + grid[r+1][c+j] + grid[r+2][c+j] !=15:
                return False

        # Diagonals
        if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15:
            return False
        if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15:
            return False

        return True

            

