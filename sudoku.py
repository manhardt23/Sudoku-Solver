
import random
from random import shuffle
counter = 0


def gen_board() -> list:
    blank = []
    for i in range(10):     #creating blank board of 0's
        if i < 9:
            blank.append([0,0,0,0,0,0,0,0,0])
    #board2 = solver(blank)
    return blank


def print_board(bo):
    # Printing the game board to be able to view properly
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -") # split by three horizontaily 

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")    # split by three vertically
            
            if j == 8:
                print(bo[i][j])

            else:
                print(str(bo[i][j]) + " ", end="")


def count_solver(bo) -> bool:
    global counter
    find = find_zero(bo)    # finding the location of zero
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if count_solver(bo):
                counter += 1
                return True

            bo[row][col] = 0

    return False

def valid(bo, num, pos)-> bool:
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    
    for i in range(len(bo)):    
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
        
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True

def find_zero(bo) -> tuple:
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None


def generate(bo):
    bo[0] = random.sample(range(1,10),9)
    count_solver(bo)
    all_cells = [(i, j) for i in range(9) for j in range(9)]
    num_filled_cells = random.randint(30, 40)
    cells_to_keep = random.sample(all_cells, num_filled_cells)
    for i, j in set(all_cells) - set(cells_to_keep):
        bo[i][j] = 0
    return bo
    

def main():
    board2 = gen_board()
    generate(board2)
    print_board(board2)

    count_solver(board2)
    print("______________________________\n")
    print_board(board2)


if __name__ == "__main__":
    main()