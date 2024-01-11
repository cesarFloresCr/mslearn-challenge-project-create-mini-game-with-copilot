# write 'hello world to the console'
# print('hello world')


user_count = 0
user_game = True

while user_game:

    # ask the user for and entrance 'rock, paper or scissors' if not that, ask again.

    print('Please choose either rock, paper or scissors')
    user_choice = input()
    while user_choice != 'rock' and user_choice != 'paper' and user_choice != 'scissors':
        print('Please choose either rock, paper or scissors')
        user_choice = input()

    # create a logic for the computer to choose between 'rock, paper or scissors'
    # import the random module
    import random
    # create a list of options
    options = ['rock', 'paper', 'scissors']
    # create a variable to store the random choice
    computer_choice = random.choice(options)
    # print the computer choice
    print(computer_choice)

    # create a logic to compare the user choice and the computer choice rocks beats scissors, scissors beats paper, paper beats rock
    # if the user choice is rock and the computer choice is scissors, print 'you win'
    if user_choice == 'rock' and computer_choice == 'scissors':
        print('you win')
        user_count += 1
    # if the user choice is scissors and the computer choice is paper, print 'you win'
    if user_choice == 'scissors' and computer_choice == 'paper':
        print('you win')
        user_count += 1
    # if the user choice is paper and the computer choice is rock, print 'you win'
    if user_choice == 'paper' and computer_choice == 'rock':
        print('you win')
        user_count += 1
    # if the user choice is scissors and the computer choice is rock, print 'you lose'
    if user_choice == 'scissors' and computer_choice == 'rock':
        print('you lose')
    # if the user choice is paper and the computer choice is scissors, print 'you lose'
    if user_choice == 'paper' and computer_choice == 'scissors':
        print('you lose')
    # if the user choice is rock and the computer choice is paper, print 'you lose'
    if user_choice == 'rock' and computer_choice == 'paper':
        print('you lose')

    # if the user choice is the same as the computer choice, print 'it's a tie'
    if user_choice == computer_choice:
        print('it\'s a tie')
    #ask the user if they want to play again in a if else statement. if they say yes, the game starts again, if they say no, the game ends. and if the user enter an invalid option, ask again.
    print('Do you want to play again?')
    user_answer = input()
    while user_answer != 'yes' and user_answer != 'no':
        print('Do you want to play again?')
        user_answer = input()
    if user_answer == 'yes':
        user_game = True
    else:
        user_game = False
        print('Thanks for playing')
        print('You won ' + str(user_count) + ' times')