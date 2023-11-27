import pygame
pygame.init()
window = pygame.display.set_mode([850,850])

playing = True

font = pygame.font.Font('freesansbold.ttf', 32)

text=font.render('Tutorials',True, (0,255,0),(0,0,128))

textRect=text.get_rect()

textRect.center=(450//2,450//2)

while playing:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing ==False

    window.fill((255, 255, 255))
    # window.blit(image, (0,0))
    window.blit(text,textRect)
    pygame.display.update()


pygame.quit()