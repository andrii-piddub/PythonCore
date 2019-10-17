import pygame, sys, time, random

game_level = 10

screen_width = 960
screen_height = 480

check_errors = pygame.init()
if check_errors[1] > 0:
    print(  'You program have {} error  when you  initialising game'.format (check_errors[1]))
    sys.exit(-1) 
else:
    print('[+] Game successfully initialised')

pygame.display.set_caption('Snake_in_2D')

game_surface = pygame.display.set_mode((screen_width, screen_height))

control_frames = pygame.time.Clock()

snake_head = [200, 100]
snake_body = [[200, 100], [200-10, 100], [200-(2*10), 100],[200-(3*10),100], [200-(4*10),100], [200-(5*10),100] ]

apple_pos = [random.randrange(1, (screen_width//10)) * 10, random.randrange(1, (screen_height//10)) * 10]


dark_blue = pygame.Color(0, 0, 204)
yellow = pygame.Color(255, 255, 0)
green = pygame.Color(0, 204, 0)
blue = pygame.Color(0, 0, 255)

food_spawn = True

direction = 'RIGHT'
changing_to = direction

points = 0


def show_points(choice, color, font, size):
    '''Function to display point in game'''
    points_font = pygame.font.SysFont(font, size)

    points_surface = points_font.render('Points : ' + str(points), True, color)
    points_rect = points_surface.get_rect()
    if choice == 1:
        points_rect.midtop = (screen_width/10, 15)
    else:
        points_rect.midtop = (screen_width/2, screen_height/1.5)
    game_surface.blit(points_surface, points_rect)

def game_over():
    '''function to display surface after ending game'''
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('The End the of the game ', True, green)   
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (screen_width/2, screen_height/4)
    game_surface.fill(dark_blue)
    game_surface.blit(game_over_surface, game_over_rect)
    show_points(0, green, 'times', 40)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()
    sys.exit()


while True:
    '''all main operation and action in game'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):
                changing_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changing_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changing_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changing_to = 'RIGHT'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
    if changing_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if changing_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if changing_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if changing_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    '''Moving our snake'''
    if direction == 'UP':
        snake_head[1] -= 10
    if direction == 'DOWN':
        snake_head[1] += 10
    if direction == 'LEFT':
        snake_head[0] -= 10
    if direction == 'RIGHT':
        snake_head[0] += 10
    snake_body.insert(0, list(snake_head))
    print(snake_head)
    # print(snake_body)
    if snake_head[0] == apple_pos[0] and snake_head[1] == apple_pos[1]:
        points += 1
        food_spawn = False
    else:
        snake_body.pop()
    if not food_spawn:
        apple_pos = [random.randrange(1, (screen_width//10)) * 10, random.randrange(1, (screen_height//10)) * 10]
    food_spawn = True
    game_surface.fill(dark_blue)
    for pos in snake_body:
        pygame.draw.rect(game_surface, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_surface, yellow, pygame.Rect(apple_pos[0], apple_pos[1], 10, 10))
    ''' Getting out of borders'''
    if snake_head[0] < 0 or snake_head[0] > screen_width-10:
        game_over()
    if snake_head[1] < 0 or snake_head[1] > screen_height-10:
        game_over()
    
    for block in snake_body[1:]:
        if snake_head[0] == block[0] and snake_head[1] == block[1]:
            game_over()

    show_points(1, yellow, 'consolas', 20)
    pygame.display.update()
    control_frames.tick(game_level)