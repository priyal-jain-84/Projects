# Sudoku project using backtracking method  # 



board=[
      [7,3,0,9,5,0,0,0,0],
      [2,0,0,6,7,0,5,8,0],
      [0,0,5,0,1,0,4,0,0],
      [1,9,0,0,6,3,2,0,5],
      [0,4,0,0,0,0,6,0,0],
      [5,6,8,2,0,7,0,0,0],
      [0,2,0,0,8,1,3,0,0],
      [0,0,1,0,0,9,7,6,0],
      [0,7,0,5,2,0,8,0,9]
      ]

# to print the board in a good and understandable manner
def print_board(boa):

    for i in range (len(boa)):
        if i%3==0 and i!=0:
            print("-------------------------------")

        for j in range(len(boa)):
            if j%3 == 0 and j!= 0:
                print(" | ",end="")

            if j==8:
                print(boa[i][j])
            else:
                print(str(boa[i][j]) + " ", end=" ")






# to find all the empty elements in the board

def find_empty(boa):
    for i in range (len(boa)):
        for j in range(len(boa)):
            if boa[i][j]==0:
                return (i,j)


# to check if the value is valid for any position

def valid(boa,pos,num):
    
    # to check whether the no. is appearing in the given row..

    for i in range(len(boa)):
        if boa[pos[0]][i]== num:
            return False
                                

    
    # to check whether the no. is appearing in the given column..

    for i in range(len(boa)):
        if boa[i][pos[1]] == num:
            return False
        
    # to check whether the no. is appearing in the given square box..

    x0 = (pos[1] // 3 ) * 3
    y0 = (pos[0] // 3 ) * 3

    for i in range (0,3):
        for j in range(0,3):
            if boa[y0+i][x0+j] == num:
                return False

    # if non of the condition is false then the value is valid so it will return True

    return True


# fuction which uses all this function and return the final solution

def solution(boa):
    find =find_empty(boa)
    if not find:
        return True
    else:
        row,column = find

    for i in range(0,10):
        if valid (boa,(row,column),i):
            boa[row][column] = i
            
            if solution(boa):
                return True
            
            boa[row][column]=0

    return False
print("Question Board\n____________________________\n")
print_board(board)
solution (board)
print("\nSolution Board\n____________________________\n")
print_board(board)






