board = [" "] * 9
player = "X"

def display_board():
    print(board[0],"|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|",board[7], "|", board[8])

def check_winner():
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    for a,b,c in wins:
        if board[a]== board[b]== board[c] !=" ":
            return board[a]
        return None
    
while True:
    display_board()
    position = int(input("Enter position(1-9): ")) -1
    if board[position] == " " :
     board[position] = player
    else:
        print("Position already taken!")
        continue
    winner = check_winner()
    if winner:
        display_board()
        print(winner, 'wins!')
        break
    if " " not in board:
         display_board()
         print("It is a draw!")
         break
    if player == "X":
         player ="0"
    else:
         player ="X"
