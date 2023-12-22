
# Import External Librarys
import pygame
import random
import math

# Create Player
class Player:
    def __init__(self, radius: int, pos: pygame.Vector2):
        self.radius = radius
        self.pos = pos
        self.bullet_pos = pos

    def wallDetect(self):
        if self.pos.x <= 20:
            self.pos.x = 20
        elif self.pos.x >= 700:
            self.pos.x = 700

    def moveLeft(self):
        self.pos.x -= 5

    def moveRight(self):
        self.pos.x += 5

    def shootBullet(self):
        self.bullet_pos.y -= 5
class Target:
    def __init__(self,):

        self.radius = random.randrange(5, 20)
        self.pos = pygame.Vector2(random.randrange(0, 720), random.randrange(0, 500))
        self.color = pygame.Vector3(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))

        self.move = pygame.Vector2(random.randrange(-2, 2), random.randrange(-2, 2))


    def moveCircle(self):
        self.pos += self.move
        if self.pos.x <= 0 or self.pos.x >= 720:
            self.move.x *= -1

        if self.pos.y <= 0 or self.pos.y >= 500:
            self.move.y *= -1




target_list = []
def createTargets():
    for i in range(5):
        target_list.append(Target())

createTargets()



# pygame Run
pygame.init()

screen = pygame.display.set_mode((720, 540))
clock = pygame.time.Clock()
running = True
dt = 0

radius_of_player = 100
circle_movement = 300*dt
growth_factor = 0.5

lose = False
win = False

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height()-20)
player = Player(20, player_pos)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
    #     player_pos.y -= player_movement
    # if keys[pygame.K_s]:
    #     player_pos.y += player_movement
    if keys[pygame.K_a]:
        player.moveLeft()
    if keys[pygame.K_d]:
        player.moveRight()
    if keys[pygame.K_SPACE]:
        player.shootBullet()
        pygame.draw.circle(screen, "white", player.bullet_pos, 5)




    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # stage draw
    pygame.draw.line(screen, "grey", (0, 498), (720, 498), 2)

    # draw player
    player.wallDetect()
    pygame.draw.circle(screen, "white", player.pos, player.radius)


    # draw food
    for target in target_list:
        target.moveCircle()
        pygame.draw.circle(screen, target.color, target.pos, target.radius)


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60

    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()