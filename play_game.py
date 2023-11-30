import pygame



def play_game(user, list_of_words, window):
    # Initialize game variables
    playing = True
    background_image1 = pygame.image.load('backgrounds/ukrainian flags.png')
    background_image1 = pygame.transform.scale(background_image1, (850, 500))
    background_image2 = pygame.image.load('backgrounds/American flags.png')
    background_image2 = pygame.transform.scale(background_image2, (850, 500))

    # Loop through each word in the list
    for index, word in enumerate(list_of_words):
        still_thinking = True
        if word in user.dropped_words:
            still_thinking=False
        flipped = True # Flag to track whether the card is flipped

        # Continue the loop while the user is still thinking and the game is ongoing
        while still_thinking and playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                    flipped = not flipped # Toggle the card flip
                elif event.type == pygame.KEYUP and event.key == pygame.K_1:
                    # Handle user's response for Easy
                    if word not in [userword[0] for userword in user.words]:
                        user.add_word(word)
                    user.self_assess( word, 1)
                    still_thinking = not still_thinking
                    if word == list_of_words[-1]:
                        playing = False
                # Similar handling for keys 2, 3, X
                elif event.type == pygame.KEYUP and event.key == pygame.K_2:
                    if word not in [userword[0] for userword in user.words]:
                        user.add_word(word)
                    user.self_assess( word, 2)
                    still_thinking = not still_thinking
                    if word == list_of_words[-1]:
                        playing = False
                elif event.type == pygame.KEYUP and event.key == pygame.K_3:
                    if word not in [userword[0] for userword in user.words]:
                        user.add_word(word)
                    user.self_assess( word, 3)
                    still_thinking = not still_thinking
                    if word == list_of_words[-1]:
                        playing = False
                elif event.type == pygame.KEYUP and event.key == pygame.K_x:
                    if word not in [userword[0] for userword in user.words]:
                        user.add_word(word)
                    user.drop_word(word)
                    still_thinking = not still_thinking
                    if word == list_of_words[-1]:
                        playing = False
                

            window.fill((255, 255, 255))  # Clear the window

            # Render text on the card
            font = pygame.font.Font('freesansbold.ttf', 42)
            font2 = pygame.font.Font('freesansbold.ttf', 18)
            text1 = font.render(list_of_words[index][1], True, (0, 0, 0))
            text2 = font2.render(list_of_words[index][3], True, (0, 0, 0))
            textRect1 = text1.get_rect()
            textRect2 = text2.get_rect()
            textRect1.center = (850 // 2, 500 // 2.5)
            textRect2.center = (850 // 2, 500 // 3 * 1.8)

            # Render text on the back of the card
            text3 = font.render(list_of_words[index][0], True, (0, 0, 0))
            text4 = font2.render(list_of_words[index][2], True, (0, 0, 0))
            textRect3 = text3.get_rect()
            textRect4 = text4.get_rect()
            textRect3.center = (850 // 2, 500 // 2.5)
            textRect4.center = (850 // 2, 500 // 3 * 1.8)

            # Display the appropriate background and text based on the card's state (flipped or not)
            if flipped:
                window.blit(background_image1, (0, 0))
                window.blit(text1, textRect1)
                window.blit(text2, textRect2)
            else:
                window.blit(background_image2, (0, 0))
                window.blit(text3, textRect3)
                window.blit(text4, textRect4)

            # Display control instructions at the bottom of the window
            font1 = pygame.font.Font('freesansbold.ttf', 16)
            text5 = font1.render('Controls: 1 - Easy to remember  2 - I kinda know it  3 - Nope  X - Drop word  SPACE - Flip card', True, (0, 0, 0), (254, 255, 217))
            textRect5 = text5.get_rect()
            textRect5.center = (850 // 2, 440)
            window.blit(text5, textRect5)

            pygame.display.update()


    return playing
