import pygame
import minimax
from game import Game

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (245, 245, 66)
blue = (66, 99, 245)
light_blue = (66, 99, 245)
dark_blue = (150, 150, 255)

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

pygame.init()
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Connect Four')
clock = pygame.time.Clock()

font = pygame.font.SysFont('comicsansms', 72)

computer = minimax.Computer()
game = Game()
result = -1
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_r:
                game = Game()
                result = -1
        elif event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            for i in range(7):
                if 100 * (i + 1) < x < 100 * (i + 2) and i in game.moves:
                    game.play(i)
                    if game.moves:
                        game.play(computer.search(game, 8))
                    if not game.moves:
                        result = game.find_win()

    screen.fill(light_blue)

    for i in range(1, 8):
        pygame.draw.line(screen, white, (100, 100 * i), (800, 100 * i))

    for i in range(1, 9):
        pygame.draw.line(screen, white, (100 * i, 100), (100 * i, 700))

    for i in range(6):
        for j in range(7):
            if game.board[0] & 1 << j * 7 + 5 - i:
                pygame.draw.circle(screen, yellow, (150 + 100 * j, 150 + 100 * i), 35)
            elif game.board[1] & 1 << j * 7 + 5 - i:
                pygame.draw.circle(screen, red, (150 + 100 * j, 150 + 100 * i), 35)

    if result != -1:
        if result == 0:
            text = font.render('Player 1 wins!', True, black)
            screen.blit(text, (SCREEN_WIDTH/2 - text.get_width()//2, SCREEN_HEIGHT/2 - text.get_height()//2))
        elif result == 1:
            text = font.render('Player 2 wins!', True, black)
            screen.blit(text, (SCREEN_WIDTH/2 - text.get_width()//2, SCREEN_HEIGHT/2 - text.get_height()//2))
        else:
            text = font.render('Tie!', True, black)
            screen.blit(text, (SCREEN_WIDTH/2 - text.get_width()//2, SCREEN_HEIGHT/2 - text.get_height()//2))

    pygame.display.flip()
