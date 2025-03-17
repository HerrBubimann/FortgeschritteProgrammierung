import random

def get_random_word(word_list, start_with_alpaca=True):
    if start_with_alpaca:
        str_alpaca = "alpaca"
        if str_alpaca not in word_list:
            word_list.append(str_alpaca)
        return str_alpaca
    else:
        word_index = random.randint(0, len(word_list) - 1)
        return word_list[word_index]

def display_board(hangmanpics, missed_letters, correct_letters, secret_word):
    print(hangmanpics[len(missed_letters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)): # replace blanks with correctly guessed letters
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]

    for letter in blanks: # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

def get_guess(already_guessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def play_again():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def main():
    """Startet, das Hangaman spiel"""
    hangman_pics = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

    words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

    print('H A N G M A N')
    missed_letters = set()
    correct_letters = set()
    secret_word = get_random_word(words)
    game_is_done = False

    while True:
        display_board(hangman_pics, missed_letters, correct_letters, secret_word)

        guess = get_guess(missed_letters | correct_letters)

        if guess in secret_word:
            correct_letters.add(guess)

            if all(letter in correct_letters for letter in secret_word):
                print(f'Yes! The secret word is "{secret_word}"! You have won!')
                game_is_done = True
        else:
            missed_letters.add(guess)

            if len(missed_letters) == len(hangman_pics) - 1:
                display_board(hangman_pics, missed_letters, correct_letters, secret_word)
                print(f'You have run out of guesses!\nAfter {len(missed_letters)} missed guesses and {len(correct_letters)} correct guesses, the word was "{secret_word}"')
                game_is_done = True

        if game_is_done:
            if play_again():
                missed_letters = set()
                correct_letters = set()
                game_is_done = False
                secret_word = get_random_word(words)
            else:
                break

if __name__ == '__main__':
    main()