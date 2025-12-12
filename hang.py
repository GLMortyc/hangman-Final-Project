import random
import pygame
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
words_3 = ['cat', 'dog', 'pet', 'pie', 'god']## will add words soon or find a library
words_4 = ['food', 'coke', 'word', 'band' 'epic']
words_5 = ['blood', 'magic', 'super', 'level' ]
right = []

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Times New Roman', 20)
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    pygame.draw.line(screen, (0, 0, 0), (500, 270), (500, 210), 10)
    pygame.draw.line(screen, (0, 0, 0), (350, 210), (500, 210), 10)
    pygame.draw.line(screen, (0, 0, 0), (350, 210), (350, 500), 10)
    pygame.draw.line(screen, (0, 0, 0), (275, 500), (425, 500), 10)
    pygame.display.flip()
   

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
            pygame.draw.line(screen, (0, 0, 0), (750,600), (800, 600), 10)
            pygame.draw.line(screen, (0, 0, 0), (825,600), (875, 600), 10)
            pygame.draw.line(screen, (0, 0, 0), (900,600), (950, 600), 10)
            letter1 = my_font.render(letters[0], True, (0, 0, 0))
            letter2 = my_font.render(letters[1], True, (0, 0, 0))
            letter3 = my_font.render(letters[2], True, (0, 0, 0))
            pygame.display.flip()
        elif level == 4:
            word = random.choice(words_4)
            letters = list(word)
            pygame.draw.line(screen, (0, 0, 0), (750,600), (800, 600), 10)
            pygame.draw.line(screen, (0, 0, 0), (825,600), (875, 600), 10)
            pygame.draw.line(screen, (0, 0, 0), (900,600), (950, 600), 10)
            pygame.draw.line(screen, (0, 0, 0), (975,600), (1025, 600), 10)
            letter1 = my_font.render(letters[0], True, (0, 0, 0))
            letter2 = my_font.render(letters[1], True, (0, 0, 0))
            letter3 = my_font.render(letters[2], True, (0, 0, 0))
            letter4 = my_font.render(letters[3], True, (0, 0, 0))
            pygame.display.flip()
        elif level == 5:
            word = random.choice(words_5)
            letters = list(word)
            pygame.draw.line(screen, (0, 0, 0), (750,600), (800, 600), 10)
            pygame.draw.line(screen, (0, 0, 0), (825,600), (875, 600), 10)
            pygame.draw.line(screen, (0, 0, 0), (900,600), (950, 600), 10)
            pygame.draw.line(screen, (0, 0, 0), (975,600), (1025, 600), 10)
            pygame.draw.line(screen, (0, 0, 0), (1050,600), (1100, 600), 10)
            letter1 = my_font.render(letters[0], True, (0, 0, 0))
            letter2 = my_font.render(letters[1], True, (0, 0, 0))
            letter3 = my_font.render(letters[2], True, (0, 0, 0))
            letter4 = my_font.render(letters[3], True, (0, 0, 0))
            letter5 = my_font.render(letters[4], True, (0, 0, 0))
            pygame.display.flip()
        while True:
            if fails == 6:
                print(word)
                pygame.time.wait(1000)
                pygame.quit()
                break
            print(alphabet)
            print(right)
            guess = input('Guess: ').lower()
            guesses = list(guess)
            letter = guess.isalpha()
            if letter == True:
                if guess == word:
                    print('Correct')
                    pygame.time.wait(1000)
                    pygame.quit()
                    break
                else:
                    pass
                for guesses in guess:
                    if guesses in letters:
                        try:
                            alphabet.remove(guesses)
                        except ValueError:
                            pass
                        right.append(guesses)
                        letters.remove(guesses)
                        try:
                            if letters[0] in guesses:
                                screen.blit(letter1, (775, 550))
                                pygame.display.update()
                            elif letters[1] in guesses:
                                screen.blit(letter2, (850, 550))
                                pygame.display.update()
                            elif letters[2] in guesses:
                                screen.blit(letter3, (925, 550))
                                pygame.display.update()
                            elif letters[3] in guesses:
                                screen.blit(letter4, (1000, 550))
                                pygame.display.update()
                            elif letters[4] in guesses:
                                screen.blit(letter5, (1075, 550))
                                pygame.display.update()
                        except:
                            pass
                        
                    else:
                        try:
                            for u in guesses:
                                alphabet.remove(u)
                                fails += 1
                                hang(fails)
                        except ValueError:
                            print('Already tried that')
                            pass
                        pass
            else:
                print('not a letter')
                pass

            letters = list(word)

    def hang(fails):
        if fails == 1:
            print('head')
            pygame.draw.circle(screen, (0, 0, 0), (500, 270), 40)
            pygame.display.flip()
        elif fails == 2:
            print('body')
            pygame.draw.line(screen, (0, 0, 0), (500,270), (500, 450), 10)
            pygame.display.flip()
        elif fails == 3:
            print('left arm')
            pygame.draw.line(screen, (0, 0, 0), (500,315), (400, 450), 10)
            pygame.display.flip()
        elif fails == 4:
            print('right arm')
            pygame.draw.line(screen, (0, 0, 0), (500,315), (600, 450), 10)
            pygame.display.flip()
        elif fails == 5:
            print('left leg')
            pygame.draw.line(screen, (0, 0, 0), (500,450), (450, 540), 10)
            pygame.display.flip()
        elif fails == 6:
            print('right leg')
            pygame.draw.line(screen, (0, 0, 0), (500,450), (550, 540), 10)
            pygame.display.flip()

    if __name__ == "__main__":
        main()



    pygame.display.flip()
    dt = clock.tick(60) / 1000


pygame.quit()
