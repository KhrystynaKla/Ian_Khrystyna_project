from user import User 
import pygame
import math


def review_dropped_words(user, window):
    undropping = True
    window.fill((255, 255, 255))
    font = pygame.font.Font('freesansbold.ttf', 18)
    # Handle empty lists at the beginning
    while user.dropped_words and user.dropped_words[0] == ['']:
        user.dropped_words = user.dropped_words[1:]

    copy_dropped_words = user.dropped_words
    
    # print(copy_dropped_words)  # Debugging print

    ukr_dropped_words = [word[1] for word in copy_dropped_words]
    page_num = 0
    num_pages = math.ceil(len(ukr_dropped_words) / 9)

    for i in range(num_pages):
        window.fill((255, 255, 255))
        display_words = ukr_dropped_words[( 9 * i ) : ( 9 * (i + 1) )]
        still_thinking = True
        for index, word in enumerate(display_words):
            text = font.render(str(1 + index) + '. ' + word, True, (0, 255, 0), (0, 0, 128))
            textRect = text.get_rect()
            x = 200  # Adjusted x-coordinate
            y = (40 * index) + 30
            textRect.center = (x, y)
            if still_thinking:
                window.blit(text, textRect)
        font1 = pygame.font.Font('freesansbold.ttf', 16)
        text5 = font1.render('Press the numbers to undrop words; press Space when done', True, (0, 255, 0), (0, 0, 128))
        textRect5 = text5.get_rect()
        textRect5.center = (850 // 2, 440)    
        window.blit(text5, textRect5)
        pygame.display.update()

        while still_thinking and undropping:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    undropping = False
                for n in range(9):
                    button = getattr(pygame, 'K_' + str(n + 1))
                    if event.type == pygame.KEYUP and event.key == button:
                        print(n)  # Handle number key press
                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                    if i ==num_pages-1:
                        undropping=False
                    still_thinking = False
        
    return undropping
                
                
    