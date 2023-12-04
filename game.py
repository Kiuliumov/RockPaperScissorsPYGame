import random
user_input = input('Enter a choice(rock, paper or scissors)')
possible_moves = ['rock','paper','scissors']
if user_input != possible_moves:
    print('Choose a valid move!\nThe valid moves are rock,paper or scissors!')
else:
 computer_move = random.choice(possible_moves)
 print(f'You chose {user_input}\n The computer chose {computer_move}')
 if computer_move == user_input:
    print("It's a draw")
 elif computer_move == 'rock':
    