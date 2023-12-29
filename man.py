import random

def hangman():
    words = ['python', 'java', 'csharp', 'javascript', 'ruby', 'php', 'cplusplus', 'swift', 'objective-c', 'golang']
    word = random.choice(words)
    word_list = list(word)
    word_guessed = ['_'] * len(word)
    word_display = "".join(word_guessed)
    letters_guessed = []
    letters_to_guess = set('abcdefghijklmnopqrstuvwxyz')
    guessed = False
    tries = 0

    print('Welcome to Hangman!')
    print('The word to guess has', len(word), 'letters.')

    while not guessed:
        print('Word to guess:', word_display)
        print('Letters to guess:', letters_to_guess)
        print('Letters guessed:', letters_guessed)
        letter = input('Please guess a letter: ').lower()

        if letter in letters_guessed:
            print('You have already guessed the letter', letter)
        elif letter in word_list:
            indices = [i for i, ltr in enumerate(word_list) if ltr == letter]
            for i in indices:
                word_guessed[i] = letter
            word_display = "".join(word_guessed)
            if '_' not in word_display:
                guessed = True
                print('Congratulations! You guessed the word correctly!')
            else:
                print('Good guess!')
        else:
            print('Oops! That letter is not in the word.')
            letters_to_guess.remove(letter)
            tries += 1
            if tries == 7:
                guessed = True
                print('You have run out of tries. The word was', word)

    play_again = input('Do you want to play again? (yes/no): ').lower()
    if play_again == 'yes':
        hangman()
    else:
        print('Thanks for playing!')

hangman()
