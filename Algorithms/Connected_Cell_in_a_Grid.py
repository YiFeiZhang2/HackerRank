#!/usr/local/bin/python3
def findNumCells (cells, row_ind, col_ind, rowlen, collen):
    if row_ind < rowlen and col_ind < collen and row_ind >=0 and col_ind >= 0:
        #print(row_ind)
        #print(col_ind)
        if cells[row_ind][col_ind] == 0 or cells[row_ind][col_ind] == 2:
            return 0
        else:
            cells[row_ind][col_ind] = 2
            left_size = findNumCells(cells, row_ind-1, col_ind, rowlen, collen)
            right_size = findNumCells(cells, row_ind+1, col_ind, rowlen, collen)
            up_size = findNumCells(cells, row_ind, col_ind-1, rowlen, collen)
            down_size = findNumCells(cells, row_ind, col_ind+1, rowlen, collen)
            up_left = findNumCells(cells, row_ind-1, col_ind-1, rowlen, collen)
            down_left = findNumCells(cells, row_ind+1, col_ind-1, rowlen, collen)
            up_right = findNumCells(cells, row_ind-1, col_ind+1, rowlen, collen)
            down_right = findNumCells(cells, row_ind+1, col_ind+1, rowlen, collen)
            return 1 + left_size + right_size + up_size + down_size + up_left + down_left + up_right + down_right
    else:
        return 0
   
def main():
    rowlen, collen = int(input()), int(input())
    cells = [list(map(int, input().split(" "))) for _ in range(rowlen)]
    #print(cells[0])
    maxlen = 0

    for row_ind in range(rowlen):
        for col_ind in range(collen):
            if cells[row_ind][col_ind] == 1:
                currlen = findNumCells(cells, row_ind, col_ind, rowlen, collen)
                if currlen > maxlen:
                    maxlen = currlen
                
    print(maxlen)
    
if __name__ == "__main__":
    main()



