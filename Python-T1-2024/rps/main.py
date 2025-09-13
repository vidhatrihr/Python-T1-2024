import random
def get_choices():
    player_choice = input('Enter a choice (rock, paper, scissor): ')
    options = ['rock','paper','scissor']
    computer_choice = random.choice(options)
    choices = {'player': player_choice,'computer': computer_choice}
    return choices

# choices = get_choices()
# print(choices)


def check_win(player, computer):
    # print('you chose ' + player + ',computer' + computer)
    print(f'you chose {player}, computer chose {computer}')
    if player == computer:
        return 'it\'s a tie!'
    elif player == 'rock':
        if computer == 'scissor':
            return 'rock smashes scissor! you won!'
        else:
            return 'paper covers a rock! you lose'
    elif player == 'scissor':
        if computer == 'paper':
            return 'scissor cuts paper! you won!'
        else:
            return 'rock smashes scissor! you lose'
    elif player == 'paper':
        if computer == 'rock':
            return 'paper covers rock! you won!'
        else:
            return 'scissor cuts paper! you lose'

    
    
choices = get_choices()
result = check_win(choices['player'], choices['computer'])
print(result)