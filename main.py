import pygame

print("Starting pygame...")

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Don't mess with the stars")

clock = pygame.time.Clock()
running = True

print("Window should be open now.")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((20, 20, 40))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print("Closed.")
