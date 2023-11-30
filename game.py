import pygame
from user import User
from play_game import play_game
from word_list import vocab_list
from undrop_the_word import review_dropped_words
from quiz import call_quiz
from random import shuffle, sample

pygame.init()

# Function to get user name
def get_user_name():
    screen = pygame.display.set_mode((850, 500))
    pygame.display.set_caption("Enter Your Name")

    font = pygame.font.Font(None, 36)
    input_box = pygame.Rect(100, 50, 200, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    text = ''
    active = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((255, 255, 255))
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()

# Get user name
user_name = get_user_name()
menu_window = pygame.display.set_mode([850, 500])
background_image = pygame.image.load('Stand with Ukraine Poster Landscape.png')
background_image = pygame.transform.scale(background_image, (850, 500))

window = pygame.display.set_mode([850, 500])

def menu_call(user_name):
    on_menu=True
    while on_menu:
        if user_name not in [user.name for user in User.get_all_users()]:
            current_user = User(user_name)
            current_user.create()
            use_this_list = vocab_list[:10]
        else:
            for user in User.get_all_users():
                if user.name == user_name:
                    current_user = user
                    use_this_list = current_user.list_of_words_to_review()

        font = pygame.font.Font('freesansbold.ttf', 32)

        text1 = font.render('PRESS 1 TO STUDY', True, (0, 0, 0))
        text2 = font.render('PRESS 2 TO SEE DROPPED WORDS', True, (0, 0, 0))
        text3 = font.render('PRESS 3 TO TAKE A QUIZ', True, (0, 0, 0))

        textRect1 = text1.get_rect()
        textRect2 = text2.get_rect()
        textRect3 = text3.get_rect()

        textRect1.center = (850 // 2, 500 // 3)
        textRect2.center = (850 // 2, 500 // 6 * 3+20)
        textRect3.center = (850 // 2, 500 // 3 * 2+20)
        

        menu_window.blit(background_image, (0, 0))
        # menu_window.fill((255, 255, 255))  # Clear the menu window
        menu_window.blit(text1, textRect1)
        if current_user.words:
            menu_window.blit(text2, textRect2)
            menu_window.blit(text3, textRect3)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on_menu = False
            elif event.type == pygame.KEYUP and event.key == pygame.K_1:
                on_menu = False
                playing(current_user, use_this_list)
            elif event.type == pygame.KEYUP and event.key == pygame.K_2:
                on_menu = False
                undropping(current_user)
            elif event.type == pygame.KEYUP and event.key == pygame.K_3:
                shuffled_list = sample(current_user.timeless_words(), len(current_user.timeless_words()))
                on_menu = False
                playing_quiz(shuffled_list, current_user)

def ask_about_quiz(current_user, use_this_list):
    still_thinking=True
    while still_thinking:
        font = pygame.font.Font('freesansbold.ttf', 24)
        text1 = font.render('PRESS 1 TO CHECK WORDS THAT YOU LEARNT', True, (0, 0, 0))
        text2 = font.render('PRESS 2 TO GO BACK TO THE MAIN MENU', True, (0, 0, 0))

        textRect1 = text1.get_rect()
        textRect2 = text2.get_rect()

        textRect1.center = (850 // 2, 500 // 3)
        textRect2.center = (850 // 2, 500 // 3*2)

        menu_window.blit(background_image, (0, 0))
        # menu_window.fill((255, 255, 255))  # Clear the menu window
        menu_window.blit(text1, textRect1)
        menu_window.blit(text2, textRect2)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                still_thinking=False
            elif event.type == pygame.KEYUP and event.key == pygame.K_1:
                shuffled_list = sample(use_this_list,len(use_this_list))
                still_thinking=False
                playing_quiz(shuffled_list, current_user)
            elif event.type == pygame.KEYUP and event.key == pygame.K_2:
                still_thinking=False





def playing(current_user, use_this_list):
    playing=True
    while playing:
        playing = play_game(current_user, use_this_list, window)
        window.fill((255, 255, 255))
        pygame.display.update()
    ask_about_quiz(current_user, use_this_list)
    menu_call(user_name)
    

def undropping(current_user):
    undropping=True
    while undropping:
        undropping=review_dropped_words(current_user, window)
        window.fill((255, 255, 255))
        pygame.display.update()
    menu_call(user_name)

def playing_quiz(word_list, current_user):
    in_quiz=True
    while in_quiz:
        in_quiz=call_quiz(word_list, current_user, window)
        window.fill((255, 255, 255))
        pygame.display.update()
    menu_call(user_name)

menu_call(user_name)
pygame.quit()


