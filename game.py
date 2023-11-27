import pygame
from word_list import vocab_list
pygame.init()
window = pygame.display.set_mode([850,850])

playing = True

font = pygame.font.Font('freesansbold.ttf', 32)

text=font.render(vocab_list[0][0],True, (0,255,0),(0,0,128))

textRect=text.get_rect()

textRect.center=(850//2,850//3)

while playing:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing =False

    window.fill((255, 255, 255))
    # window.blit(image, (0,0))
    window.blit(text,textRect)
    pygame.display.update()


pygame.quit()