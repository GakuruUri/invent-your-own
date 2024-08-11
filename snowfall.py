import pygame
import random


# Initialize
pygame.init()


# Chosen colours will be used
# To display the output
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]


# Specify the screen size.
SIZE = [400, 400]
screen = pygame.display.set_mode(SIZE)

# Caption for output window
pygame.display.set_caption("Snowy")

snowFall = []

for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    snowFall.append([x, y])

# Create an object to create time
clock = pygame.time.Clock()

# Loop till close button is pressed
done = False

while not done:

    # User did something
    for event in pygame.event.get():

        # If user clicked close
        if event.type == pygame.QUIT:

            # Flag that we are done so we exit the loop.
            done = True

    screen.fill(WHITE)

    for i in range(len(snowFall)):
        pygame.draw.circle(screen, GREEN, snowFall[i], 2)

        snowFall[i][1] += 1
        if snowFall[i][1] > 400:
            y = random.randrange(-50, -10)
            snowFall[i][1] = y

            x = random.randrange(0, 400)
            snowFall[i][0] = x

    pygame.display.flip()
    clock.tick(20)
pygame.quit()



























