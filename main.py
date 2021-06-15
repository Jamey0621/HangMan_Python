# Lets make HangMan!! lets start by getting random
import random

# now lets set up the bord

HANGMAN_PICS = ['''
  +----+
       |
       |
       |
=========''', '''
  +----+
  O    |
       |
       |
=========''', '''
  +----+
  O    |
  |    |
       |
=========''', '''
  +----+
  O    |
 /|    |
       |
=========''', '''
  +----+
  O    |
 /|\   |
       |
=========''', '''
  +----+
  O    |
 /|\   |
 /     |
=========''', '''
  +----+
  O    |
 /|\   |
 / \   |
=========''', '''
''']
# lets set up words to use
words = 'time clean snap later bye cry lime slime play application unstable crime fine shine cat bat tap lap ' \
        'nap fap sat tap long crime fling team crazy ghost demon '.split()


# This function returns a random string from the passed list of strings
def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
        print()

        blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:
        print(letter, end=' ')
        print()


def getGuess(alreadyGuessed):
    while True:
        print('Give me a letter')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('You can only do one letter at a time bud')
        elif guess is alreadyGuessed:
            print('You have already used that letter')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Only letters are in the word')
        else:
            return guess


def playAgain():
    print('Do you want to play another round --|| YES or NO ||--')
    return input().lower().startswith('y')


print('H A N G M A N')
missedLetters = ' '
correctLetters = ' '
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            if foundAllLetters:
                ('NICE your are right the word is ' + secretWord + ' YOU WON!')
                gameIsDone = True
        else:
            missedLetters = missedLetters + guess

            if len(missedLetters) == len(HANGMAN_PICS) - 1:
                displayBoard(missedLetters, correctLetters, secretWord)
                print('You are dead!/nAfter ' + str(len(missedLetters)) + 'missed guesses, and you had ' + str(
                    len(correctLetters)) + ' correct letters. The word was ' + secretWord + ' Good try tho')
                gameIsDone = True

            if gameIsDone:
                if playAgain():
                    missedLetters = ''
                    correctLetters = ''
                    gameIsDone = False
                    secretWord = getRandomWord(words)
                else:
                    break
