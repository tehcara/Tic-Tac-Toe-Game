"""
Basic type of Tic Tac Toe game by Caroline Lau Campbell.
This is a 1-player game against the computer.
A dictionary is used to manage the 3x3 game board.
The player must enter an integer from 1 to 9 for each move.
A message will be displayed for win, lose, or draw.
You can play another game. Or, quit after any complete game.
"""
import random

# guide to the numbered moves
game_spaces = {7: '7', 8: '8', 9: '9',
               4: '4', 5: '5', 6: '6',
               1: '1', 2: '2', 3: '3'}

# actual game board template
game_board = {7: ' ', 8: ' ', 9: ' ',
              4: ' ', 5: ' ', 6: ' ',
              1: ' ', 2: ' ', 3: ' '}


def game_grid(spaces):
    """
    Function to print either the numbered move guide or game board
    :param spaces: game_spaces or game_board
    :return: decorative whitespace
    """
    print(spaces[7], spaces[8], spaces[9])
    print(spaces[4], spaces[5], spaces[6])
    print(spaces[1], spaces[2], spaces[3])
    return ' '  # blank string for visual effect; it's just whitespace


def computer_ai():
    """
    Function to generate random move for computer
    :return: random int from 1 to 9
    """
    return random.randint(1, 9)


def check_winner(move_counter, new_board):
    """
    Function to check if anyone has won the game
    :param move_counter: number of moves played in the game
    :param new_board: the game board containing the moves
    :return: true - if someone has won the game
    """
    player_message = 'You won! :o'
    computer_message = 'The computer won. lol'
    if move_counter >= 5:  # player must have moved at least 3 times to start winning
        # chained if-else to check winning row is filled and to praise the winner
        if new_board[7] == new_board[8] == new_board[9] != ' ':
            if new_board[7] == 'X':
                print(player_message)
            elif new_board[7] == 'O':
                print(computer_message)
            return True
        elif new_board[7] == new_board[5] == new_board[3] != ' ':
            if new_board[7] == 'X':
                print(player_message)
            elif new_board[7] == 'O':
                print(computer_message)
            return True
        elif new_board[7] == new_board[4] == new_board[1] != ' ':
            if new_board[7] == 'X':
                print(player_message)
            elif new_board[7] == 'O':
                print(computer_message)
            return True
        elif new_board[4] == new_board[5] == new_board[6] != ' ':
            if new_board[4] == 'X':
                print(player_message)
            elif new_board[4] == 'O':
                print(computer_message)
            return True
        elif new_board[8] == new_board[5] == new_board[2] != ' ':
            if new_board[8] == 'X':
                print(player_message)
            elif new_board[8] == 'O':
                print(computer_message)
            return True
        elif new_board[1] == new_board[2] == new_board[3] != ' ':
            if new_board[1] == 'X':
                print(player_message)
            elif new_board[1] == 'O':
                print(computer_message)
            return True
        elif new_board[1] == new_board[5] == new_board[9] != ' ':
            if new_board[1] == 'X':
                print(player_message)
            elif new_board[1] == 'O':
                print(computer_message)
            return True
        elif new_board[9] == new_board[6] == new_board[3] != ' ':
            if new_board[9] == 'X':
                print(player_message)
            elif new_board[9] == 'O':
                print(computer_message)
            return True


def ask_player_move():
    """
    Function to ask player for move and check if move is valid
    :return: int - if move is digit from 1 to 9
    """
    ask = True
    while ask is True:
        move = input('>>>')
        ask = False if move.isdigit() and 1 <= int(move) <= 9 else True
        if ask is True:
            print('That was not a number from 1 to 9! :( Try again.')
    return int(move)


def new_game():
    """
    Function to call a new round of the game
    :return: nothing
    """
    new_board = game_board
    player_marker = 'X'
    computer_marker = 'O'
    move_counter = 0
    print('The game board looks like this: \n')
    print(game_grid(game_spaces))
    for i in range(10):
        if check_winner(move_counter, new_board):  # check if computer won on last turn
            break
        print('Enter a valid move... from 1 to 9.\n')
        move = ask_player_move()  # player's choice of move
        # move = input('>>>')  # player's choice of move
        if new_board[int(move)] == ' ':
            new_board[int(move)] = player_marker
            print('You have moved...')
            print(game_grid(game_board))
            move_counter += 1
            if check_winner(move_counter, new_board):  # check if player won this turn
                break
        else:
            print('That was not a valid move... try again!')
            print('The game board looks like this... choose a valid move.')
            print(game_grid(game_board))
            continue
        for x in range(10):
            temp_move = computer_ai()
            if new_board[temp_move] == ' ':
                new_board[temp_move] = computer_marker
                print('Computer has moved...')
                print(game_grid(game_board))
                move_counter += 1
                break
            else:
                continue
        if move_counter == 9:  # if game ran out of moves
            print('I forgot... was there meant to be a winner?\nNo? I guess it was a draw. lol')
            break
    print('\nWould you like to play again? :D Enter Y or N')
    another_game = input('>>>')
    if another_game == 'Y' or another_game == 'y':
        new_board.update((k, ' ') for k in new_board)  # reset game board by updating dictionary values
        new_game()
    else:
        print('Why not Y? :\'( wah wah wah')


if __name__ == '__main__':
    print('Would you like to play a game? :) Enter Y or N')
    response = input('>>>')
    if response == 'Y' or response == 'y':
        new_game()
    else:
        print('Why not Y? :\'( wah wah wah')
