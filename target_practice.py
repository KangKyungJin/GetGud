import pygame
import random

#initialize pygame
pygame.init()

#gets the user's display information
displayInfo = pygame.display.Info()

#setting window size to be user's display resolution
window = pygame.display.set_mode([displayInfo.current_w, displayInfo.current_h])

#runs till exited
running = True
while running:

    #if user clicks window close or presses the escape key, exits program
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and pygame.K_ESCAPE:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            if target.collidepoint(x, y):
                print('clicked target')

    #sets background color to be white
    window.fill((200,200,200))

    #sets random x (within 720 pixels) coordinate for circle location
    randX = random.randint(280, displayInfo.current_w- 280)

    #sets random y (within 480 pixels) coordinate for circle location
    randY = random.randint(120, displayInfo.current_h - 120)

    #sets random radius
    randR = random.randint(25, 75)

    #draws our target on window
    target = pygame.draw.circle(window, (0, 168, 0), (displayInfo.current_w - randX, displayInfo.current_h - randY), randR)

    #updates display on window
    pygame.display.flip()

    pygame.time.wait(750)

pygame.quit()


