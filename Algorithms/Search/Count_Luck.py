#!/usr/local/bin/python3
def isPath(forest, row, col):
    if row > len(forest) or col > len(forest[0]) or row < 0 or col < 0:
        return False
    elif forest[row][col] == '.' or forest[row][col] == '*':
        return True
    else:
        return False

def findPath(forest, row, col, path):
    if not isPath(forest, row, col):
        return False
    if forest[row][col] == '*':
        return True
    
    leftPath = False
    rightPath = False
    upPath = False
    downPath = False
    forest[row][col] == 'O'
    
    downPath = findPath(forest, row+1, col, path.append("down"))
    rightPath = findPath(forest, row, col+1, path.append("right"))
    upPath = findPath(forest, row-1, col, path.append("up"))
    leftPath = findTurns(forest, row, col-1, path.append("left"))
    

    else:
        return false
        
    
def main():
    numCase = int(input())
    for i in range(numCase):
        num_row, num_col = map(int, input().split(" "))
        st_row = 0
        st_col = 0
        forest = list()
        turns = 0
        path = list()
        
        for i in range(num_row):
            line = input()
            if 'M' in line:
                st_row = i
                st_col = line.index('M')
            forest.append([c for c in line])
            
        guess = int(input())   
            
        print(forest)

if __name__ == "__main__":
    print("HI")
    main()

        
