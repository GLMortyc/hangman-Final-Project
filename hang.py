import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
words_3 = ['cat', 'dog', 'pet', 'pie', 'god']## will add words soon
words_4 = ['food', 'coke', 'word', 'band' 'epic']
words_5 = ['blood', 'magic', 'super', 'level', 'piece' ]
right = []

def main():
    while True:
        try:
            level = int(input('Level:'))
            if level >= 3 and level <= 5:
                game(level)
                break
        except ValueError:
            pass

def game(level):
    fails = 0
    if level == 3:
        word = random.choice(words_3)
        letters = list(word)
        while True:
            if fails == 6:
                print(word)
                break
            print(alphabet)
            print(right)
            guess = input('Guess: ')
            guesses = list(guess)
            letter = guess.isalpha()
            if letter == True:
                if guess == word:
                    print('Correct')
                    break
                else:
                    pass
                for guesses in guess:
                    if guesses in letters:
                        right.append(guesses)
                        letters.remove(guesses)
                        try:
                            alphabet.remove(guesses)
                        except ValueError:
                            pass
                    else:
                        try:
                            for guesses in guess:
                                alphabet.remove(guesses)
                                fails += 1
                                hang(fails)
                        except ValueError:
                            print('Already tried that')
                            pass
                        pass
            else:
                print('not a letter')
                pass
    elif level == 4:
        word = random.choice(words_4)
        letters = list(word)
        while True:
            if fails == 6:
                print(word)
                break
            print(alphabet)
            print(right)
            guess = input('Guess: ')
            guesses = list(guess)
            letter = guess.isalpha()
            if letter == True:
                if guess == word:
                    print('Correct')
                    break
                else:
                    pass
                for guesses in guess:
                    if guesses in letters:
                        right.append(guesses)
                        letters.remove(guesses)
                        try:
                            alphabet.remove(guesses)
                        except ValueError:
                            pass
                    else:
                        try:
                            for guesses in guess:
                                alphabet.remove(guesses)
                                fails += 1
                                hang(fails)
                        except ValueError:
                            print('Already tried that')
                            pass
                        pass
            else:
                print('not a letter')
                pass
    elif level == 5:
        word = random.choice(words_5)
        letters = list(word)
        while True:
            if fails == 6:
                print(word)
                break
            print(alphabet)
            print(right)
            guess = input('Guess: ')
            guesses = list(guess)
            letter = guess.isalpha()
            if letter == True:
                if guess == word:
                    print('Correct')
                    break
                else:
                    pass
                for guesses in guess:
                    if guesses in letters:
                        right.append(guesses)
                        letters.remove(guesses)
                        try:
                            alphabet.remove(guesses)
                        except ValueError:
                            pass
                    else:
                        try:
                            for guesses in guess:
                                alphabet.remove(guesses)
                                fails += 1
                                hang(fails)
                        except ValueError:
                            print('Already tried that')
                            pass
                        pass
            else:
                print('not a letter')
                pass

def hang(fails):
    if fails == 1:
        print('head')
    elif fails == 2:
        print('body')
    elif fails == 3:
        print('left arm')
    elif fails == 4:
        print('right arm')
    elif fails == 5:
        print('left leg')
    elif fails == 6:
        print('right leg')

if __name__ == "__main__":
    main()
