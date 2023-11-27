import pygame
from word_list import vocab_list

pygame.init()
window = pygame.display.set_mode([850, 500])

playing = True
flipped = True

font = pygame.font.Font('freesansbold.ttf', 32)

text1 = font.render(vocab_list[0][1], True, (0, 255, 0), (0, 0, 128))
text2 = font.render(vocab_list[0][3], True, (0, 255, 0), (0, 0, 128))

textRect1 = text1.get_rect()
textRect2 = text2.get_rect()

textRect1.center = (850 // 2, 500 // 3)
textRect2.center = (850 // 2, 500 // 3 * 2)

text3 = font.render(vocab_list[0][0], True, (0, 255, 0), (0, 0, 128))
text4 = font.render(vocab_list[0][2], True, (0, 255, 0), (0, 0, 128))

textRect3 = text3.get_rect()
textRect4 = text4.get_rect()

textRect3.center = (850 // 2, 500 // 3)
textRect4.center = (850 // 2, 500 // 3 * 2)

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            flipped = not flipped

    window.fill((255, 255, 255))  # Fill the window with background color only once

    if flipped:
        window.blit(text1, textRect1)
        window.blit(text2, textRect2)
    else:
        window.blit(text3, textRect3)
        window.blit(text4, textRect4)

    pygame.display.update()

pygame.quit()
