# Create the board
board = [' ' for _ in range(9)]

# Function to display the board
def display_board():
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')

# Function to check if the game is over
def is_game_over():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return True
    if board[2] == board[4] == board[6] != ' ':
        return True

    # Check if the board is full
    if ' ' not in board:
        return True

    return False

# Function to play the game
def play_game():
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")
    sign1 = 'X'
    sign2 = 'O'
    current_player = player1
    game_over = False

    while not game_over:
        display_board()
        position = int(input("{} ({}): Enter a position (1-9): ".format(current_player, sign1 if current_player == player1 else sign2)))

        # Check if the position is valid
        while position < 1 or position > 9 or board[position - 1] != ' ':
            print("Invalid position. Please try again.")
            position = int(input("{} ({}): Enter a position (1-9): ".format(current_player, sign1 if current_player == player1 else sign2)))

        board[position - 1] = sign1 if current_player == player1 else sign2

        if is_game_over():
            display_board()
            if ' ' not in board:
                print("It's a tie!")
            else:
                print("{} wins!".format(current_player))
            game_over = True

        current_player = player2 if current_player == player1 else player1

# Start the game
play_game()
