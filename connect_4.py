import pygame
pygame.init()

screen = pygame.display.set_mode((1800, 1400))
screen.fill((255, 255, 255))
black = (0, 0, 0)

def create_board():
    #board
    board_height = 1025
    board_width = 1200
    x = 50; y = 50
    pygame.draw.rect(screen, black, (x, y, board_width, 5))
    pygame.draw.rect(screen, black, (x, y, 5, board_height))
    pygame.draw.rect(screen, black, (x, board_height+y, board_width+5, 5))
    pygame.draw.rect(screen, black, (board_width+x, y, 5, board_height))
    pygame.display.update()

    #circles
    circle_x_factor = 75
    circle_y_factor = 75
    for i in range(6):
        for i in range(7):
            pygame.draw.circle(screen, black, (x+circle_x_factor, y+circle_y_factor), 50)
            circle_x_factor +=175
        circle_x_factor = 75
        circle_y_factor += 175

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    create_board()
pygame.quit()