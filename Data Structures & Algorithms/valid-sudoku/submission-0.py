class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        di=defaultdict(list)
        dic2=defaultdict(list)
        for ind,i in enumerate(board):
            for j in i:
               if j=='.':
                continue
               if j in di[ind]:
                print('j',j,'ind',di[ind])
                return False
               di[ind].append(j)
        
        for i in range(0,9):
            for j in range(0,9):
                a=board[j][i]
                if a=='.':
                    continue
                if a in dic2[i]:
                    return False
                dic2[i].append(a)

        
        for square in range(9):
            seen=set()
            for i in range(3):
                for j in range(3):
                    row=(square//3) * 3 + i
                    col=(square%3) * 3 + j
                    if board[row][col]=='.':
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        print(seen)
        return True
            
