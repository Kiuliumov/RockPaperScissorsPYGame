import random
file_path = "game_stats.txt"
try:
    with open(file_path, "r") as file:
        data = file.read().split(',')
        wins, draws, losses = map(int, data)
except FileNotFoundError:
    wins, draws, losses = 0, 0, 0
game_outcome = ''
user_input = input('Enter a choice(rock, paper or scissors)')
possible_moves = ['rock','paper','scissors']
wins = 0
losses = 0
if user_input != possible_moves:
    print('Choose a valid move!\nThe valid moves are rock,paper or scissors!')
else:
 computer_move = random.choice(possible_moves)
 print(f'You chose {user_input}\n The computer chose {computer_move}')
 if computer_move == user_input:
    print("It's a draw")
    game_outcome = 'draw'
 elif computer_move == 'rock':
    if user_input == 'scissors':
        game_outcome = 'lose'
        print('You lose!')
    elif user_input == 'paper':
        game_outcome = 'win'
        print('You win!')
 elif computer_move == 'paper':
     if user_input == 'scissors':
         game_outcome = 'win'
         print('You win!')
     elif user_input == 'rock':
         game_outcome = 'lose'
         print('You lose!')
 elif computer_move == 'scissors':
     if user_input == 'rock':
         game_outcome = 'lose'
         print('You lose!')
     elif user_input == 'paper':
         game_outcome = 'win'
         print('You win!')
with open(file_path, "w") as file:
    file.write(f"{wins},{draws},{losses}")



print(f"Current Stats: Wins - {wins}, Losses - {losses}")