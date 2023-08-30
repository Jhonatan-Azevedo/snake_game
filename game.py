import  pygame
import sys
from snake import Snake
from food import Food
from pyautogui import confirm

def start(nivel):
    pygame.font.init()
    pygame.display.set_caption('Snake_game by:@dev-azevedo')
    my_font = pygame.font.SysFont('Comic Sans MS', 15)

    base_nivel = nivel
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
            base_nivel += 1
            points += 1

        if snake.check_collision():
            looser = my_font.render('Game over!', True, (255, 255, 255))
            screen.blit(looser, (10, 10))
            # pygame.display.flip()

            if restart():
                snake.body = [[80, 50], [70, 50], [60,50]]
                snake.position = [80, 50] 
                snake.direction='RIGHT'
                points = 0
                base_nivel = nivel
            else:
                pygame.quit()
                return sys.exit()

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
        time_clock.tick(base_nivel)

def restart():
    resp = confirm(text='Game over', title='Welcome Snake_game', buttons=['Reset', 'Quit'])
    if resp == 'Quit': 
        return False
    if resp == 'Reset':
        return True

resp = confirm(text='Choose the level', title='Welcome Snake_game', buttons=['Ease', 'Medium', 'Hard', 'Cancel'])

if resp != 'Cancel':
    fps = 20
    if resp == 'Ease':
        fps = 15

    if resp == 'Medium':
        fps = 20
    
    if resp == 'Hard':
        fps = 25

    if resp != None:
        start(fps)