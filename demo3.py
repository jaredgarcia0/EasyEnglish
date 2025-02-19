import pygame
import csv
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Fonts
FONT = pygame.font.Font(None, 36)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("English-Spanish Matching Game")

# Load words from CSV file
def load_words(filename):
    words = []
    with open(filename, "r") as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if len(row) >= 2:
                words.append((row[1], row[0]))
    return words

# Game states
MENU = "menu"
GAME = "game"
END = "end"

# Game variables
state = MENU
words = load_words('en-es_adjective.csv')
remaining_words = words[:]
current_word = None
options = []
success_count = 0

# Helper function to draw text
def draw_text(text, x, y, color=BLACK):
    rendered_text = FONT.render(text, True, color)
    screen.blit(rendered_text, (x, y))

# Function to setup the next word in the game
def setup_next_word():
    global current_word, options, remaining_words
    if remaining_words:
        current_word = random.choice(remaining_words)
        remaining_words.remove(current_word)
        options = [current_word[1]] + random.sample([w[1] for w in words if w != current_word], 3)
        random.shuffle(options)
    else:
        global state
        state = END

# Main loop
running = True
setup_next_word()
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == MENU:
            if event.type == pygame.MOUSEBUTTONDOWN:
                state = GAME

        elif state == GAME:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for i, option in enumerate(options):
                    if 150 < x < 650 and 200 + i * 50 < y < 250 + i * 50:
                        if option == current_word[1]:
                            success_count += 1
                            setup_next_word()
                        break

    if state == MENU:
        draw_text("Welcome to the English-Spanish Matching Game!", 100, 100, BLUE)
        draw_text("Click anywhere to start.", 100, 200, BLACK)

    elif state == GAME:
        draw_text(f"Match the English word: {current_word[0]}", 100, 100, BLACK)
        for i, option in enumerate(options):
            pygame.draw.rect(screen, BLUE, (150, 200 + i * 50, 500, 50))
            draw_text(option, 200, 200 + i * 50, WHITE)

        draw_text(f"Score: {success_count}", WIDTH - 200, 20, BLACK)

    elif state == END:
        draw_text("Congratulations! You've matched all the words!", 100, 100, BLUE)
        draw_text(f"Your final score is: {success_count}", 100, 200, BLACK)
        draw_text("Close the game to exit.", 100, 300, BLACK)

    pygame.display.flip()

pygame.quit()
