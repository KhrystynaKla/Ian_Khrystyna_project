import pygame

def play_game(user, list_of_words, window):
    playing = True

    for index, word in enumerate(list_of_words):

        if word not in [userword[0] for userword in user.words]:
            user.add_word(word)


        still_thinking = True
        if word in user.dropped_words:
            still_thinking=False
        flipped = True

        while still_thinking and playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                    flipped = not flipped
                elif event.type == pygame.KEYUP and event.key == pygame.K_1:
                    user.self_assess( word, 1)
                    still_thinking = not still_thinking
                    if word == list_of_words[-1]:
                        playing = False
                elif event.type == pygame.KEYUP and event.key == pygame.K_2:
                    user.self_assess( word, 2)
                    still_thinking = not still_thinking
                    if word == list_of_words[-1]:
                        playing = False
                elif event.type == pygame.KEYUP and event.key == pygame.K_3:
                    user.self_assess( word, 3)
                    still_thinking = not still_thinking
                    if word == list_of_words[-1]:
                        playing = False
                elif event.type == pygame.KEYUP and event.key == pygame.K_x:
                    user.drop_word(word)
                    still_thinking = not still_thinking
                    if word == list_of_words[-1]:
                        playing = False
                

            window.fill((255, 255, 255))  # Clear the window

            font = pygame.font.Font('freesansbold.ttf', 32)

            text1 = font.render(list_of_words[index][1], True, (0, 255, 0), (0, 0, 128))
            text2 = font.render(list_of_words[index][3], True, (0, 255, 0), (0, 0, 128))

            textRect1 = text1.get_rect()
            textRect2 = text2.get_rect()

            textRect1.center = (850 // 2, 500 // 3)
            textRect2.center = (850 // 2, 500 // 3 * 2)

            text3 = font.render(list_of_words[index][0], True, (0, 255, 0), (0, 0, 128))
            text4 = font.render(list_of_words[index][2], True, (0, 255, 0), (0, 0, 128))

            textRect3 = text3.get_rect()
            textRect4 = text4.get_rect()

            textRect3.center = (850 // 2, 500 // 3)
            textRect4.center = (850 // 2, 500 // 3 * 2)

            if flipped:
                window.blit(text1, textRect1)
                window.blit(text2, textRect2)
            else:
                window.blit(text3, textRect3)
                window.blit(text4, textRect4)

            font1 = pygame.font.Font('freesansbold.ttf', 16)

            text5 = font1.render('Controls: 1 - Easy to remember  2 - I kinda know it  3 - Nope  X - Drop word  SPACE - Flip card', True, (0, 255, 0), (0, 0, 128))
            
            textRect5 = text5.get_rect()
            textRect5.center = (850 // 2, 440)
            
            window.blit(text5, textRect5)

            pygame.display.update()


    return playing
