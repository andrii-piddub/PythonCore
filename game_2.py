import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("My first game")
#clock = pygame.time.Clock()

x=50
y=50
r = 40
done = True
clock = pygame.time.Clock()

while  done:
    pygame.time.delay(100)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=False
    player_position = pygame.mouse.get_pos()
    x = min(player_position[0]+r,500-r)
    y = r    
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (255,0,0), (x, y),r)
    
    
    pygame.display.update()
  #clock.tick(60)