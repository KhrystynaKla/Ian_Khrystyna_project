# from user import User
# import pygame
# from play_game import play_game
# from word_list import vocab_list

# pygame.init()
# window = pygame.display.set_mode([850, 500])

# playing = True

# while playing:

#     playing = play_game(User("Ian"), vocab_list, window)
#     window.fill((255, 255, 255)) 
#     pygame.display.update()

# pygame.quit()

import pygame
from user import User, unjoin, unjoin_dropped_words
from play_game import play_game
from word_list import vocab_list

pygame.init()

# Function to get user name
def get_user_name():
    screen = pygame.display.set_mode((400, 200))
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
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()

# Get user name
user_name = get_user_name()

# Initialize game window
window = pygame.display.set_mode([850, 500])

playing = True

while playing:
    if user_name not in [user.name for user in User.get_all_users()]:
        current_user = User(user_name)
        current_user.create()
    else:
        for user in User.get_all_users():
            if user.name==user_name:
                current_user=user
    playing = play_game(current_user, vocab_list, window)
    window.fill((255, 255, 255))
    pygame.display.update()

pygame.quit()
