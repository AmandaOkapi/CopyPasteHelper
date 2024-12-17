import pygame
import sys
import pyperclip

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50
BUTTON_COLOR = (100, 200, 100)
BUTTON_HOVER_COLOR = (150, 250, 150)
BG_COLOR = (30, 30, 30)
FPS = 60


# Font
font = pygame.font.Font(None, 24)

# Function to draw the button
def draw_copy_indicator(screen, x, y, width, height, text):
    color = (130,0,215)
    pygame.draw.rect(screen, color, (x, y, width, height))

    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

# Function to draw the button
def draw_button(screen, x, y, width, height, diplay_text, copy_text):
    clicked =False
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    # Check if the mouse is hovering over the button
    if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
        color = BUTTON_HOVER_COLOR
        if mouse_pressed[0]:  # Left mouse button pressed
            print(f"{diplay_text} clicked")
            handle_button_click(copy_text)
            clicked =True
    else:
        color = BUTTON_COLOR

    # Draw the button
    pygame.draw.rect(screen, color, (x, y, width, height))

    # Draw the text on the button
    text_surface = font.render(diplay_text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)
    return clicked

def handle_button_click(text):
    pyperclip.copy(text)

def main():
    # Create a resizable window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Resizable Window with Button")

    delimiter = "-"
    text =[
        "Copy me!",
        "among-ඞ",
        "shrug-¯\_(ツ)_/¯"
    ]
    #process
    display_text =[]
    copy_text =[]
    
    for s in text:
        lst = s.split(delimiter)
        display_text.append(lst[-1] if len(lst)<1 else lst[0])
        copy_text.append(lst[-1])

    # Main loop
    clock = pygame.time.Clock()
    running = True
    is_focused = True
    
    falling=False
    fallSpd=2.5
    fallPos=0 

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                # Adjust screen size
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)




        # Clear the screen
        screen.fill(BG_COLOR)
        clicked =False
        # Draw the button
        for i in range(len(display_text)):
            if(draw_button(screen, 10, (BUTTON_HEIGHT +20)*i , BUTTON_WIDTH, BUTTON_HEIGHT, display_text[i], copy_text[i])):
                clicked=True

        if(clicked):
            fallPos=0
            draw_copy_indicator(screen, screen.get_width()//2, screen.get_height() -80 -fallPos, BUTTON_WIDTH, BUTTON_HEIGHT, "Copied")
            falling =True
        elif falling:
            fallPos -=fallSpd
            draw_copy_indicator(screen, screen.get_width()//2, screen.get_height() -80 -fallPos, BUTTON_WIDTH, BUTTON_HEIGHT, "Copied")
            if (screen.get_height() - 80 -fallPos > screen.get_height() ): 
                falling =False

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    # Quit Pygame
    pygame.quit()
    sys.exit()


main()