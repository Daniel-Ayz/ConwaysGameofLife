import pygame

# colors
col_alive = (255, 255, 215)
col_background = (10, 10, 40)
col_grid = (30, 30, 60)
# size of the matrix
size = 100
# size of each cell on the grid
cellS = 6


# create the board of the next iteration and returns it
def nextBoard(board):
    next = [[0] * size for _ in range(size)]
    for row in range(size):
        for col in range(size):
            next[row][col] = calcLife(row, col, board)
    return next


# updates the board.
def update(surface, currentBoard, live=False):
    nxt = currentBoard
    if live:
        nxt = nextBoard(currentBoard)
    for row in range(size):
        for col in range(size):
            color = col_alive if nxt[row][col] == 1 else col_background
            pygame.draw.rect(surface, color, (col * cellS, row * cellS, cellS - 1, cellS - 1))

    return nxt


# calculates if the cell will be alive or dead in the next iteration
def calcLife(row, col, board):
    p = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    count = 0
    for x, y in p:
        if 0 <= row + y < size and 0 <= col + x < size and board[row + y][col + x] == 1:
            count += 1
    if board[row][col] == 1:
        if count < 2:
            return 0
        elif 2 <= count <= 3:
            return 1
        else:
            return 0
    else:
        if count == 3:
            return 1
        else:
            return 0


# initialize an empty board
def init():
    board = [[0] * size for _ in range(size)]
    return board


# main
def main():
    pygame.init()

    surface = pygame.display.set_mode((size * cellS, size * cellS))

    pygame.display.set_caption("John Conway's Game of Life")

    board = init()
    surface.fill(col_grid)
    update(surface, board)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    board = update(surface, board)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                board[pos[1] // cellS][pos[0] // cellS] = 1
                board = update(surface, board)
                pygame.display.update()

        surface.fill(col_grid)

        if running:
            board = update(surface, board, True)
            pygame.display.update()


if __name__ == "__main__":
    main()
