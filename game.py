import random

file_path = "game_stats.txt"

try:
    with open(file_path, "r") as file:
        data = file.read().split(',')
        prev_wins, prev_draws, prev_losses = map(int, data)
except FileNotFoundError:
    prev_wins, prev_draws, prev_losses = 0, 0, 0

game_outcome = ''
user_input = input('Enter a choice (rock, paper, or scissors): ')
possible_moves = ['rock', 'paper', 'scissors']
computer_move = random.choice(possible_moves)
if user_input not in possible_moves:
    print("Choose a valid move!\nThe valid moves are rock, paper, or scissors!")
else:
    print(f'You chose {user_input}\nThe computer chose {computer_move}')

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
            game_outcome = 'win'
            print('You win!')
        elif user_input == 'paper':
            game_outcome = 'lose'
            print('You lose!')

if game_outcome == 'win':
    prev_wins += 1
elif game_outcome == 'draw':
    prev_draws += 1
elif game_outcome == 'lose':
    prev_losses += 1

with open(file_path, "w") as file:
    file.write(f"{prev_wins},{prev_draws},{prev_losses}")

print(f"Current Stats: Wins - {prev_wins}, Draws - {prev_draws}, Losses - {prev_losses}")