import pygame
from play_game import play_game
from word_list import vocab_list


pygame.init()
window = pygame.display.set_mode([850, 500])

playing = True

while playing:
    play_game('Ian', vocab_list, window)
    window.fill((255, 255, 255)) 
    pygame.display.update()

pygame.quit()
