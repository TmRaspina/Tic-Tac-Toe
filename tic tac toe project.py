import random

def initialize_board():
    # ایجاد صفحه بازی
    return [[' ' for _ in range(3)] for _ in range(3)]

def display_board(board):
    # نمایش صفحه بازی
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_win(board, player):
    # بررسی برنده شدن بازیکن
    win_cond = [[(0, 0), (0, 1), (0, 2)],
                [(1, 0), (1, 1), (1, 2)],
                [(2, 0), (2, 1), (2, 2)],
                [(0, 0), (1, 0), (2, 0)],
                [(0, 1), (1, 1), (2, 1)],
                [(0, 2), (1, 2), (2, 2)],
                [(0, 0), (1, 1), (2, 2)],
                [(0, 2), (1, 1), (2, 0)]]
    
    for cond in win_cond:
        if all(board[r][c] == player for r, c in cond):
            return True
    return False

def check_draw(board):
    # بررسی مساوی شدن بازی
    return all(cell != ' ' for row in board for cell in row)

def player_move(board, player):
    # حرکت بازیکن
    while True:
        try:
            move = int(input(f"Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("Cell already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter a number between 1 and 9.")

def minimax(board, depth, is_maximizing):
    # الگوریتم Minimax برای حرکت بهینه کامپیوتر
    if check_win(board, 'O'):
        return 1
    elif check_win(board, 'X'):
        return -1
    elif check_draw(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[row][col] = ' '
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[row][col] = ' '
                    best_score = min(best_score, score)
        return best_score

def computer_move(board):
    # حرکت کامپیوتر
    best_score = float('-inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'O'
                score = minimax(board, 0, False)
                board[row][col] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    board[best_move[0]][best_move[1]] = 'O'

def main():
    board = initialize_board()
    display_board(board)
    
    while True:
        player_move(board, 'X')
        display_board(board)
        if check_win(board, 'X'):
            print("You win!")
            break
        if check_draw(board):
            print("It's a draw!")
            break
        computer_move(board)
        display_board(board)
        if check_win(board, 'O'):
            print("Computer wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()