import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Garden Planting Game")
font = pygame.font.SysFont("Arial", 24)

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 105, 180)
ORANGE = (255, 140, 0)
LIGHT_GREEN = (144, 238, 144)

# Base Plant Class
class Plant:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self._watered = False

    def get_position(self):
        return self.__x, self.__y

    def set_position(self, x, y):
        self.__x = x
        self.__y = y

    def is_watered(self):
        return self._watered

    def water(self):
        self._watered = True

    def draw(self, surface):
        raise NotImplementedError("Subclasses must implement draw method")


# Subclasses
class Tulip(Plant):
    def draw(self, surface):
        x, y = self.get_position()
        pygame.draw.rect(surface, BROWN, (x - 2, y, 4, 20))
        if self.is_watered():
            pygame.draw.polygon(surface, PINK, [(x, y - 15), (x - 10, y), (x + 10, y)])
            pygame.draw.polygon(surface, PINK, [(x - 7, y - 10), (x - 3, y), (x - 11, y)])
            pygame.draw.polygon(surface, PINK, [(x + 7, y - 10), (x + 3, y), (x + 11, y)])
        else:
            pygame.draw.circle(surface, BROWN, (x, y), 7)


class Sunflower(Plant):
    def draw(self, surface):
        x, y = self.get_position()
        pygame.draw.rect(surface, BROWN, (x - 2, y, 4, 20))
        if self.is_watered():
            pygame.draw.circle(surface, ORANGE, (x, y), 18)
            pygame.draw.circle(surface, YELLOW, (x, y), 12)
            pygame.draw.circle(surface, BROWN, (x, y), 6)
        else:
            pygame.draw.circle(surface, BROWN, (x, y), 7)


# Instruction Screen
def show_instructions():
    screen.fill(WHITE)
    lines = [
        "Welcome to the Garden Planting Game!",
        "Press T for Tulip or S for Sunflower.",
        "Click anywhere to plant the selected flower.",
        "Press W to water all flowers to make them bloom.",
        "Click 'Start' to begin."
    ]
    for i, line in enumerate(lines):
        text = font.render(line, True, (0, 0, 0))
        screen.blit(text, (50, 80 + i * 40))

    start_btn = pygame.Rect(300, 450, 200, 50)
    pygame.draw.rect(screen, GREEN, start_btn)
    btn_text = font.render("Start", True, WHITE)
    screen.blit(btn_text, (start_btn.x + 70, start_btn.y + 10))
    pygame.display.flip()
    return start_btn

# Main Game
def main():
    clock = pygame.time.Clock()
    plants = []
    running = True
    in_intro = True
    current_type = "Tulip"

    start_button = show_instructions()

    while in_intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    in_intro = False
            elif event.type == pygame.KEYDOWN:
                in_intro = False

    while running:
        screen.fill(LIGHT_GREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    current_type = "Tulip"
                elif event.key == pygame.K_s:
                    current_type = "Sunflower"
                elif event.key == pygame.K_w:
                    for plant in plants:
                        plant.water()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if current_type == "Tulip":
                    plants.append(Tulip(x, y))
                elif current_type == "Sunflower":
                    plants.append(Sunflower(x, y))

        for plant in plants:
            plant.draw(screen)

        type_text = font.render(f"Current Plant: {current_type}", True, (0, 60, 0))
        screen.blit(type_text, (10, 10))

        if any(p.is_watered() for p in plants):
            bloom_text = font.render("Your garden is blooming!", True, (0, 100, 0))
            screen.blit(bloom_text, (250, 40))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
