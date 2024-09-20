'''Basic tic-tac-toe aka noughts-and-crosses game by Caroline Lau Campbell. 
Originally, it was fully text-based but has been refreshed to use Tkinter.'''

import random
import tkinter as tk
from tkinter import ttk

### Tic-tac-toe layout ###
game_board = {6: '', 7: '', 8: '',
              3: '', 4: '', 5: '',
              0: '', 1: '', 2: ''}

game_buttons = [] 
'''Nested list representing the game board buttons, used to map button clicks 
to positions in the game_board.'''
for row in range(3):
    row_of_buttons = []
    for col in range(3):
        button_number = row*3 + col # Number from set 0-2, 3-5, 6-8.
        row_of_buttons.append(button_number) # Append number to row list.
    game_buttons.append(row_of_buttons) # Append row list to button list.

total_games = 0 # Initialise total_games counter.
game_over = False # Initialise game_over flag.

button_list = [] # Button references.

### Game completion messages ###
win_message = 'Yay! You won! :)'
lose_message = 'Aw. The computer won. :('
draw_message = 'Meh. It\'s a draw. :/'

def new_game():
    """Set up a new game. Reset move counter and current player, get clean 
    board, clear text on game buttons, reset game message, increment total 
    games played, and reset game_over flag.
    """    
    global move_counter, current_player, current_board, game_over, total_games
    move_counter = 0 # Reset move_counter.
    current_player = 'X' # Always start with player X.
    current_board = game_board.copy() # Clean copy of the game board.
    for button_row in game_buttons:
        for button_num in button_row:
            button = button_list[button_num]
            button.config(text='') # Reset the game buttons.
    msg_label.config(text='') # Reset the game message.
    if game_over:
        total_games = total_games+1 # Increment total_games played counter.
        ct_label.configure(text=f'You\'ve played {total_games} games! '+
                           f'Playing next game #{total_games+1}...')
    game_over = False # Reset game_over flag; set new game as not over.

def computer_ai():
    """Pseudo-AI to simulate the computer's move.

    Returns:
        int: Pseudo-random int from 0 to 8.
    """    
    return random.randint(0, 8)

### Winning lines ###
# 012, 345, 678, 048, 246, 036, 147, 258
winning_lines = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],
                 [2,4,6],[0,3,6],[1,4,7],[2,5,8]]

def check_for_win(board):
    """Evaluate whether a game has been won.

    Args:
        board (dict): Current state of the game board.

    Returns:
        bool: True or False, depending on whether the game was won.
    """    
    w = winning_lines # The nested list of winning combinations.
    if 5<= move_counter <=9: # 5+ moves to win a game, max 9 moves to draw.
        for i in range(8):
            if board[w[i][0]]==board[w[i][1]]==board[w[i][2]]!='':
                if board[w[i][0]]=='X': # Player wins.
                    msg_label.configure(text=win_message)
                    return True
                elif board[w[i][0]]=='O': # Computer wins.
                    msg_label.configure(text=lose_message)
                    return True
    return False

### Player move ###
def make_a_move(move_number):
    """Handle player's move, derived from whichever button was clicked. Check 
    whether game was won/finished. If game is still in progress and the player 
    has just moved, trigger the computer's move.

    Args:
        move_number (int): Index of button list.

    Returns:
        None: Stops doing anything if game is finished.
    """    
    global current_player, move_counter, game_over
    if game_over:
        return # Return nothing if game is finished.
    current_player = 'X' # X always represents the player.
    if current_board[move_number]=='': # Check move is playable.
        current_board[move_number]=current_player # Play the move.
        button_list[move_number].configure(text=current_player) # Button text.
        button_list[move_number].configure(style='played.TButton')
        '''NB: The played.TButton style visually reinforces the player's 
        moves by the application of colour. This is in addition to the 
        button's text - X.'''
        move_counter += 1 # Increment move_counter.
        if check_for_win(current_board):
            game_over = True # End game.
        elif move_counter == 9: # Draw at 9 moves with no winner.
            '''NB: As the player only plays odd numbered turns, only the 
            player can reach a draw state - at max moves, 9.'''
            msg_label.configure(text=draw_message)
            game_over = True # End game.
        else: 
            make_computer_move() # Trigger computer's move.

### Computer move ###
def make_computer_move():
    """Handle the computer's move by generating a random move using 
    computer_ai and ensure it's a valid move. Check whether the game was 
    won/finished.
    """    
    global current_player, move_counter, game_over
    current_player = 'O' # O always represents the computer.
    move=computer_ai() # Generate computer's move.
    while current_board[move] != '': # Validate the move is playable.
        move=computer_ai() # Repeat move generation till it's valid.
    current_board[move]=current_player # Play the move.
    button_list[move].configure(text=current_player) # Button text.
    button_list[move].configure(style='ai.TButton')
    '''NB: The ai.TButton style visually reinforces the computer's 
    moves by the application of colour. This is in addition to the 
    button's text - O.'''
    move_counter += 1 # Increment move_counter.
    if check_for_win(current_board): # Check if game is won/finished.
        game_over = True # End game.

def launch_game():
    """Initialise window and create the widgets. Setup the first game.
    """    
    global total_games
    root = tk.Tk()
    style = ttk.Style()
    style.configure('.', font= ('Courier', 16)) # Default font.
    style.configure('TLabel', wraplength=450)
    style.configure('played.TButton', foreground='blue') # Player colour.
    style.configure('ai.TButton', foreground='red') # Computer colour.
    root.title('Tic-tac-toe Game')
    root.geometry('500x400')

    ### Grid layout row 0 ###
    rules_label = ttk.Label(root, text='Click any button in the game grid '+
                            f'to play a move. You need 3 matching symbols '+
                            f'in a row to win.')
    rules_label.grid(row=0, columnspan=3, padx=10, pady=10, sticky='nsew')
    ### Grid layout rows 1-3 ###
    for row in range(3):
        for col in range(3):
            player_move = row*3 + col
            button = ttk.Button(root, text='')  
            button_list.append(button) # Store button reference.
            button.configure(command=lambda pm=player_move: make_a_move(pm))
            button.grid(row=row+1, column=col, padx=10, 
                        pady=10, ipady=5, sticky='nsew')
    ### Grid layout row 4 ###
    global msg_label
    msg_label = ttk.Label(root, text='game msgs go here')
    msg_label.grid(row=4, columnspan=3, padx=10, pady=10, sticky='nsew')
    ### Grid layout row 5 ###
    global ct_label
    ct_label = ttk.Label(root, text=f'You have played {total_games} games.')
    ct_label.grid(row=5, columnspan=3, padx=10, pady=10, sticky='nsew')
    ### Grid layout row 6 ###
    new_game_button = ttk.Button(root, text='New Game', command=new_game)
    new_game_button.grid(row=6, column=0, padx=10, pady=10, sticky='nsew')
    quit_button = ttk.Button(root, text='Quit', command=lambda: root.quit())
    quit_button.grid(row=6, column=2, padx=10, pady=10, sticky='nsew')

    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)
    root.grid_rowconfigure(4, weight=1)
    root.grid_rowconfigure(5, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)

    new_game() # Initialise the first game.
    root.mainloop()

if __name__=='__main__':
    launch_game()