import random
from user import User
from __init__ import CONN, CURSOR
import pygame
from word_list import vocab_list

# Function to generate a list of 4 random words from the given list,
# including one given value and 3 others randomly picked from the list.
def generate_random_list(word_list, given_value):
    options = [word for word in word_list if word != given_value]
    random_words = random.sample(options, 3)
    result = [given_value] + random_words
    random.shuffle(result)
    return result


# Function to initiate a quiz with a list of words.
def call_quiz(words_list, user, window):
    window.fill((255, 255, 255))
    background_image = pygame.image.load('backgrounds/Drop words.png')
    background_image = pygame.transform.scale(background_image, (850, 500))
    window.blit(background_image, (0, 0))
    in_quiz= True
    font = pygame.font.Font('freesansbold.ttf', 42)
    font1 = pygame.font.Font('freesansbold.ttf', 18)
    font2 = pygame.font.Font('freesansbold.ttf', 16)

    # Create a copy of words excluding dropped ones
    copy_of_words = [word for word in words_list if word not in user.dropped_words]
    if len(copy_of_words)==0:
        return False
    if len(copy_of_words)>=10:
        copy_of_words=copy_of_words[:10]

    # Loop through each word in the quiz
    for word in copy_of_words:
        # Generate choices for the current word
        choices= generate_random_list(user.timeless_words(), word)
        correct_index=choices.index(word)
        window.blit(background_image, (0, 0))
        still_thinking = True

        # Render question and answer choices
        text = font.render(word[1], True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (425, 120)
        text1 = font1.render('1. '+choices[0][0]+'       2. '+ choices[1][0], True, (0, 0, 0))
        text2 = font1.render('3. '+choices[2][0]+'       4. '+ choices[3][0], True, (0, 0, 0))
        textRect1 = text1.get_rect()
        textRect2 = text2.get_rect()
        textRect1.center = (425, 250)
        textRect2.center = (425, 300)
        text3 = font2.render('Select number matching the correct answer', True, (0, 255, 0), (0, 0, 128))
        textRect3 = text3.get_rect()
        textRect3.center = (850 // 2, 440)    
        window.blit(text3, textRect3)
        
        if still_thinking:
            window.blit(text, textRect)
            window.blit(text1, textRect1)
            window.blit(text2, textRect2)
        pygame.display.update()

        # Wait for user input to select the correct answer
        while still_thinking and in_quiz:
            for event in pygame.event.get():
                correct_answer = getattr(pygame, 'K_' + str(correct_index+1))
                if event.type == pygame.QUIT:
                    in_quiz = False
                if event.type == pygame.KEYUP and event.key == correct_answer:
                    still_thinking=False
                    if copy_of_words.index(word)==len(copy_of_words)-1:
                        in_quiz=False
    
    return in_quiz
                    

