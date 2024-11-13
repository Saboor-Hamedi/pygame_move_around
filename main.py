import pygame 
import random
# initialize window
pygame.init()

# window size 
width  =  800
height =  600


# set up the display 
screen =  pygame.display.set_mode((width,  height))
clock  =  pygame.time.Clock()
running  = True
dt = 0


# initial position for circle_radius
initial_x = 400
initial_y = 500
circle_radius = 10
screen_color = (67, 46, 84)
circle_color = (232, 188, 185)
collision_color = (255, 0, 0)
random_color = (75, 67,118)
def position(x=0,y=0):
     return  pygame.Vector2(x,y)

player_pos = position(initial_x, initial_y)

shapes = []
# Define a buffer zone to avoid placing shapes too close to the circle's initial position
buffer_zone_height = 100
buffer_zone_width = 50
for _ in range(30):

    rect_width = random.randint(20, 100)
    rect_height = random.randint(20,100)
    rect_x = random.randint(0,width - rect_width )
    rect_y = random.randint(buffer_zone_width,height - rect_height - buffer_zone_height)
    shapes.append((rect_x,rect_y, rect_width, rect_height))


def draw_shapes(screen):
    for shape in shapes:
        pygame.draw.rect(screen, random_color,shape)


def check_collision(new_pos):
    player_circle = pygame.Rect(new_pos.x - circle_radius, new_pos.y - circle_radius, circle_radius* 2, circle_radius*2)

    for shape in shapes:
        if player_circle.colliderect(shape):
            return True
    return False
# run the app
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    screen.fill(screen_color)

    # random shape
    draw_shapes(screen)
    pygame.draw.circle(screen,circle_color, player_pos, circle_radius) # make red circle


    # move the circle
    keys = pygame.key.get_pressed()
    new_pos = player_pos.copy()

    # change circle color 
    
    if keys[pygame.K_k] and player_pos.y - circle_radius > 0:
        new_pos.y -= 300 *dt
        # block the circle when touched the shapes
        if not check_collision(new_pos):
            player_pos.y = new_pos.y

    if keys[pygame.K_j] and player_pos.y + circle_radius < screen.get_height():
        new_pos.y +=300 * dt
        if not check_collision(new_pos):
            player_pos.y = new_pos.y

    if keys[pygame.K_l] and player_pos.x + circle_radius < screen.get_width():
        new_pos.x += 300 * dt
        if not check_collision(new_pos):
            player_pos.x = new_pos.x
    if keys[pygame.K_h] and player_pos.x - circle_radius > 0:
        new_pos.x -=300 * dt
        if not check_collision(new_pos):
            player_pos.x = new_pos.x


    pygame.display.flip()
    dt =  clock.tick(60) /1000

pygame.quit()
