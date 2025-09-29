# Utilized logic from sudoku.py to display using pygame
import pygame
import random

# pygame setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((500, 600))
clock = pygame.time.Clock()
running = True
dif = 500 / 9
font1 = pygame.font.SysFont("comicsans", 40)

x = 0
y = 0
val = 0


def gen_board() -> list:
    blank = []
    for i in range(10):     #creating blank board of 0's
        if i < 9:
            blank.append([0,0,0,0,0,0,0,0,0])
    return blank


def count_solver(bo) -> bool:
    clock.tick()
    global counter
    find = find_zero(bo)    # finding the location of zero
    if not find:
        return True
    else:
        row, col = find
    pygame.event.pump()
    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            global x,y
            x = row
            y = col

            screen.fill((255, 255, 255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(40)

            if count_solver(bo):
                return True

            bo[row][col] = 0

            screen.fill((255, 255, 255))
         
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(25)

    return False

def solver(bo) -> bool:
    find = find_zero(bo)    # finding the location of zero
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solver(bo):
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
    solver(bo)
    all_cells = [(i, j) for i in range(9) for j in range(9)]
    num_filled_cells = random.randint(30, 40)
    cells_to_keep = random.sample(all_cells, num_filled_cells)
    for i, j in set(all_cells) - set(cells_to_keep):
        bo[i][j] = 0
    return bo

def draw():
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                pygame.draw.rect(screen, "white", (i * dif, j * dif, dif + 1, dif + 1))
                text1 = font1.render(str(grid[i][j]),1, "black")
                screen.blit(text1, (i * dif + 15, j * dif - 3))
    for i in range(9):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, "black", (i * dif, 0,), (i * dif , 500), thick)
        pygame.draw.line(screen, "black", (0, i * dif), (500, i * dif), thick)

def drawVal(val):
    text1 = font1.render(str(val),1, "black")
    screen.blit(text1, (x * dif + 15, y * dif - 3))
def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7)  

grid = gen_board()
generate(grid)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")

        # RENDER YOUR GAME HERE
    pygame.display.set_caption("SUDOKU SOLVER USING BACKTRACKING")
    draw()  # this is the unsloved game board
    draw_box()
    count_solver(grid)
    clock.tick()


    # flip() the display to put your work on screen
    pygame.display.flip()

    #clock.tick(60)  # limits FPS to 60
time =clock.get_time()
print(str(time) + "'s")
pygame.quit()
