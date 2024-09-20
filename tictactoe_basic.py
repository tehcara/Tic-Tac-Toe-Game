import random
import tkinter as tk
from tkinter import ttk

### Tic-tac-toe layout ###
game_board = {6: '', 7: '', 8: '',
              3: '', 4: '', 5: '',
              0: '', 1: '', 2: ''}

game_buttons = [] # nested list; corresponds to game_board keys
for row in range(3):
    row_of_buttons = []
    for col in range(3):
        button_number = row*3 + col # num from set 0-2, 3-5, 6-8
        row_of_buttons.append(button_number) # tack num to row list
    game_buttons.append(row_of_buttons) # tack row list to button list

total_games = 0
game_over = False # initialise game as not over

button_list = [] # button references

### Game completetion messages ###
win_message = 'Yay! You won!'
lose_message = 'Aw. Computer won.'
draw_message = 'Meh. It\'s a draw.'

def new_game():
    global move_counter, current_player, current_board, game_over, total_games
    move_counter = 0
    current_player = 'X' # always start with player X
    current_board = game_board.copy() # clean copy of game board
    for button_row in game_buttons:
        for button_num in button_row:
            button = button_list[button_num]
            button.config(text='') # clear the game buttons
    msg_label.config(text='') # clear the game message
    if game_over==True:
        total_games = total_games+1
        ct_label.configure(text=f'You\'ve played {total_games} games! Playing next game #{total_games+1}...')
    game_over = False # reset finished game

def computer_ai():
    return random.randint(0, 8)

### Winning lines ###
# 012, 345, 678, 048, 246, 036, 147, 258
winning_lines = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],
                 [2,4,6],[0,3,6],[1,4,7],[2,5,8]]

def check_for_win(board):
    w = winning_lines
    if 5<= move_counter <=9:
        for i in range(8):
            if board[w[i][0]]==board[w[i][1]]==board[w[i][2]]!='':
                if board[w[i][0]]=='X':
                    msg_label.configure(text=win_message)
                    return True
                elif board[w[i][0]]=='O':
                    msg_label.configure(text=lose_message)
                    return True
    return False

### Player move ###
def make_a_move(move_number):
    global current_player, move_counter, game_over
    if game_over:
        return # return nothing if game finished
    current_player = 'X'
    if current_board[move_number]=='':
        current_board[move_number]=current_player
        button_list[move_number].configure(text=current_player)
        button_list[move_number].configure(style='played.TButton')
        move_counter += 1
        if check_for_win(current_board):
            game_over = True # end game
        elif move_counter == 9: # player X could draw
            msg_label.configure(text=draw_message)
            game_over = True # end game
        else: 
            make_computer_move()

### Computer move ###
def make_computer_move():
    global current_player, move_counter, game_over
    current_player = 'O'
    move=computer_ai()
    while current_board[move] != '':
        move=computer_ai()
    current_board[move]=current_player
    button_list[move].configure(text=current_player)
    button_list[move].configure(style='ai.TButton')
    move_counter += 1
    if check_for_win(current_board):
        game_over = True # end game

def launch_game():
    global total_games
    root = tk.Tk()
    style = ttk.Style()
    style.configure('.', font= ('Courier', 16))
    style.configure('TLabel', wraplength=450)
    style.configure('played.TButton', foreground='blue')
    style.configure('ai.TButton', foreground='red')
    root.title('Tic-tac-toe Game')
    root.geometry('500x400')

    ### Grid layout row 0 ###
    rules_label = ttk.Label(root, text='Click any button in the game grid to play a move. You need 3 matching symbols in a row to win.')
    rules_label.grid(row=0, columnspan=3, padx=10, pady=10, sticky='nsew')
    ### Grid layout rows 1-3 ###
    for row in range(3):
        for col in range(3):
            player_move = row*3 + col
            button = ttk.Button(root, text='')  
            button_list.append(button)
            button.configure(command=lambda pm=player_move: make_a_move(pm))
            button.grid(row=row+1, column=col, padx=10, pady=10, ipady=5, sticky='nsew')
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

    new_game() # initialise first game
    root.mainloop()

if __name__=='__main__':
    launch_game()