import time
def score_board(names_scores):
    print("<"*25, ">"*25)
    print(" "*17, "EL BKA2 LEL AKWA")
    print(names_scores[0][0], ":", names_scores[0][1])
    print(names_scores[1][0], ":", names_scores[1][1])
    print("<" * 25, ">" * 25)
def prt_grid(grid):
    print(" ", "_" * 59, sep="")
    print("|", " " * 19, "|", " " * 19, "|", " " * 19, "|", sep="")
    print("|", " " * 7, grid[0], " " * 7, "|", " " * 7, grid[1], " " * 7, "|", " " * 7, grid[2], " " * 7, "|")
    print("|", " " * 19, "|", " " * 19, "|", " " * 19, "|", sep="")
    print(" ", "_" * 59, sep="")

    print(" ", "_" * 59, sep="")
    print("|", " " * 19, "|", " " * 19, "|", " " * 19, "|", sep="")
    print("|", " " * 7, grid[3], " " * 7, "|", " " * 7, grid[4], " " * 7, "|", " " * 7, grid[5], " " * 7, "|")
    print("|", " " * 19, "|", " " * 19, "|", " " * 19, "|", sep="")
    print(" ", "_" * 59, sep="")

    print(" ", "_" * 59, sep="")
    print("|", " " * 19, "|", " " * 19, "|", " " * 19, "|", sep="")
    print("|", " " * 7, grid[6], " " * 7, "|", " " * 7, grid[7], " " * 7, "|", " " * 7, grid[8], " " * 7, "|")
    print("|", " " * 19, "|", " " * 19, "|", " " * 19, "|", sep="")
    print(" ", "_" * 59, sep="")

def ck_win(grid):
    if grid[0] == grid[1] and grid[0] == grid[2]:
        return 1
    if grid[3] == grid[4] and grid[4] == grid[5]:
        return 1
    if grid[6] == grid[7] and grid[7] == grid[8]:
        return 1

    if grid[0] == grid[3] and grid[3] == grid[6]:
        return 1
    if grid[1] == grid[4] and grid[4] == grid[7]:
        return 1
    if grid[2] == grid[5] and grid[5] == grid[8]:
        return 1

    if grid[0] == grid[4] and grid[4] == grid[8]:
        return 1
    if grid[2] == grid[4] and grid[4] == grid[6]:
        return 1

    for i in range(len(grid)):
        if grid[i] != 'X' and grid[i] != 'O':
            return 3
    return -1
def play(names_scores, dor):
    score_board(names_scores)
    turn = dor
    grid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    win = ck_win(grid)
    while win == 3:
        prt_grid(grid)
        if turn == 2:
            turn = 0
        print("YA", names_scores[turn][0], "2L3AB YALA")
        n = int(input())
        if n > 9 or n < 1 or grid[n - 1] == 'X' or grid[n - 1] == 'O':
            print("2MSHY MEN HENA")
            time.sleep(5)
        else:
            grid[n - 1] = names_scores[turn][2]
            win = ck_win(grid)
            if win == 1:
                break
            turn += 1
    if win == 1:
        print("3AASH YA GAMEEEEEED")
        time.sleep(5)
        names_scores[turn][1] += 1
    play(names_scores, turn)

name_1 = input("enter your name ya man: ")
name_2 = input("enter your enta kman: ")
l1 = [name_1, 0, 'X']
l2 = [name_2, 0, 'O']
names_scores = [l1, l2]
play(names_scores, 0)

