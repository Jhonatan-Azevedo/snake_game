import  pygame
import sys
from snake import Snake
from food import Food
import time

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 15)

pygame.init()
screen_size = (300, 400)
screen = pygame.display.set_mode(screen_size)

time_clock = pygame.time.Clock()

points = 0

snake = Snake()
food = Food()
position_food = food.position

while True:
    screen.fill((7, 4, 35))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d :
                snake.change_direction('RIGHT')
            
            if event.key == pygame.K_UP or event.key == pygame.K_w :
                snake.change_direction('TOP')
            
            if event.key == pygame.K_DOWN or event.key == pygame.K_s :
                snake.change_direction('BOTTOM')
            
            if event.key == pygame.K_LEFT or event.key == pygame.K_a :
                snake.change_direction('LEFT')
    
    position_food = food.generate_new_food()
    if snake.move(position_food):
        food.already_ate = True
        points += 1

    if snake.check_collision():
        points_view = my_font.render(f'Points: {points}', True, (255, 255, 255))
        screen.blit(points_view, (10, 10))

        looser = my_font.render('Game over!', True, (255, 255, 255))
        screen.blit(looser, (110, 180))
        pygame.display.flip()

        time.sleep(2)
        pygame.quit()
        sys.exit()

    points_view = my_font.render(f'Points: {points}', True, (255, 255, 255))
    screen.blit(points_view, (10, 10))

    # Draw snake
    for pos in snake.body:
        pygame.draw.rect(screen, 
                         pygame.Color(255, 204, 0), 
                         pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw food
    pygame.draw.rect(screen, pygame.Color(255, 0, 0), 
                     pygame.Rect(position_food[0], position_food[1], 10, 10))
    
    # update screen for each frame
    pygame.display.update()

    # FPS
    time_clock.tick(20)