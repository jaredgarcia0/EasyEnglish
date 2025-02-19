import pygame
import random
import csv

# Constants
WIDTH, HEIGHT = 1100, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Easy_English")

SPANISH = 0
ENGLISH = 1

# COLORS
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
AQUA = (0, 255, 255)
BLACK = (0, 0, 0)
HOVER_COLOR = (200,200,200) # Light gray for hover effect

# frames per second so it will run at the same speed on every computer
FPS = 60


# Fonts
pygame.font.init()
FONT = pygame.font.SysFont('Comicsans', 35)

# Game options
menu_options = [
    FONT.render("1. Adjectives", True, BLACK),
    FONT.render("2. Communication", True, BLACK),
    FONT.render("3. Food", True, BLACK),
    FONT.render("4. Health", True, BLACK),
    FONT.render("5. Orientation", True, BLACK),
    FONT.render("6. Personal Info", True, BLACK),
    FONT.render("7. Sentences", True, BLACK),
    FONT.render("8. Shopping", True, BLACK),
    FONT.render("9. Surrounding", True, BLACK),
    FONT.render("10. Time", True, BLACK),
    FONT.render("11. Transportation", True, BLACK),
    FONT.render("12. Verbs", True, BLACK),
]


def draw_menu(mouse_pos):
    # Fill the background
    WIN.fill(AQUA)

    # Load and display the logo
    try:
        logo = pygame.image.load("logo.png")
        logo = pygame.transform.scale(logo, (200, 200))  # Resize logo
        WIN.blit(logo, (WIDTH // 2 - logo.get_width() // 2, 20))  # Center the logo
    except FileNotFoundError:
        print("Error: logo.png not found. Make sure it's in the same directory.")
        title_text = FONT.render('Welcome to Easy English', True, BLACK)
        WIN.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))

    # Render Subtitle
    game_mode = FONT.render('Choose a Game Mode', True, BLACK)
    WIN.blit(game_mode, (WIDTH // 2 - game_mode.get_width() // 2, 215))

    # Variables for column positioning
    left_column_x = WIDTH // 4  # X-coordinate for the left column
    right_column_x = (WIDTH * 3) // 4  # X-coordinate for the right column
    start_y = 300  # Starting Y-coordinate for options
    line_spacing = 90  # Space between each option vertically
    rect_padding = 10  # Padding around text for the rectangle

    # Split the options into two columns
    mid_index = len(menu_options) // 2
    left_column = menu_options[:mid_index]
    right_column = menu_options[mid_index:]

    # Draw the left column
    y_position = start_y
    for option in left_column:
        # Calculate rectangle dimensions
        rect_width = option.get_width() + rect_padding * 2
        rect_height = option.get_height() + rect_padding * 2
        rect_x = left_column_x - rect_width // 2
        rect_y = y_position - rect_padding

        # check if mouse is hovering over this option
        if rect_x <= mouse_pos[0] <= rect_x + rect_width and rect_y <= mouse_pos[1] <= rect_y + rect_height:
            pygame.draw.rect(WIN, HOVER_COLOR, (rect_x, rect_y, rect_width, rect_height)) # Highlight on hover
        else:
            pygame.draw.rect(WIN, WHITE, (rect_x, rect_y, rect_width, rect_height))  # Normal state

        # Draw rectangle and text
        # pygame.draw.rect(WIN, WHITE, (rect_x, rect_y, rect_width, rect_height))  # White rectangle
        pygame.draw.rect(WIN, BLACK, (rect_x, rect_y, rect_width, rect_height), 2)  # Black border
        WIN.blit(option, (left_column_x - option.get_width() // 2, y_position))
        y_position += line_spacing

    # Draw the right column
    y_position = start_y
    for option in right_column:
        # Calculate rectangle dimensions
        rect_width = option.get_width() + rect_padding * 2
        rect_height = option.get_height() + rect_padding * 2
        rect_x = right_column_x - rect_width // 2
        rect_y = y_position - rect_padding

        # Check if the mouse is hovering over this option
        if rect_x <= mouse_pos[0] <= rect_x + rect_width and rect_y <= mouse_pos[1] <= rect_y + rect_height:
            pygame.draw.rect(WIN, HOVER_COLOR, (rect_x, rect_y, rect_width, rect_height))  # Highlight on hover
        else:
            pygame.draw.rect(WIN, WHITE, (rect_x, rect_y, rect_width, rect_height))  # Normal state


        # Draw rectangle and text
        # pygame.draw.rect(WIN, WHITE, (rect_x, rect_y, rect_width, rect_height))  # White rectangle
        pygame.draw.rect(WIN, BLACK, (rect_x, rect_y, rect_width, rect_height), 2)  # Black border
        WIN.blit(option, (right_column_x - option.get_width() // 2, y_position))
        y_position += line_spacing

    # Update the display
    pygame.display.update()

# # Helper function to draw text
# def draw_text(text, x, y, color=BLACK):
#     rendered_text = FONT.render(text, True, color)
#     screen.blit(rendered_text, (x, y))

def handle_click(mouse_pos):
    start_y = 300
    line_spacing = 90
    rect_padding = 10
    mid_index = len(menu_options) // 2

    left_column_x = WIDTH // 4
    for i, option in enumerate(menu_options[:mid_index]):
        rect_width = option.get_width() + rect_padding * 2
        rect_height = option.get_height() + rect_padding * 2
        rect_x = left_column_x - rect_width // 2
        rect_y = start_y + i * line_spacing - rect_padding

        if rect_x <= mouse_pos[0] <= rect_x + rect_width and rect_y <= mouse_pos[1] <= rect_y + rect_height:
            print(f"Option {i+1} clicked!")

    right_column_x = (WIDTH * 3) // 4
    for i, option in enumerate(menu_options[mid_index:]):
        rect_width = option.get_width() + rect_padding * 2
        rect_height = option.get_height() + rect_padding * 2
        rect_x = right_column_x - rect_width // 2
        rect_y = start_y + i * line_spacing - rect_padding

        if rect_x <= mouse_pos[0] <= rect_x + rect_width and rect_y <= mouse_pos[1] <= rect_y + rect_height:
            print(f"Option {i+mid_index+1} clicked!")



# def read_csv_file(filename):
#     '''reads csv files and separetes the values'''

#     with open(filename, 'r') as csv_file:
#         reader = csv.reader(csv_file)
#         for row in reader:
#             row = 
            




def main():
    # Loop that creates the window of the game and exits the window
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_click(mouse_pos)

        draw_menu(mouse_pos)

    pygame.quit()


if __name__ == '__main__':
    main()
