import pygame

# Initialize Pygame
pygame.init()

# Screen Dimensions
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 640
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Vinland Warriors: Poke Village")

# --- Vinland Saga Inspired Palette ---
BG_COLD_SKY = (140, 150, 160)      # Overcast cold sky
GRASS_MUTED = (45, 55, 35)         # Dark desaturated grass
DIRT_PATH = (90, 75, 55)           # Muted earth
VIKING_BLUE = (60, 90, 130)        # Viking tunic blue
WOLF_CHARCOAL = (70, 75, 80)       # Dark wolf fur
TREE_GREEN = (30, 45, 30)          # Deep pine green
HOUSE_BROWN = (85, 55, 35)         # Weathered wood
UI_BROWN = (50, 35, 25)            # Dark UI wood
WHITE_TEXT = (230, 230, 230)
HEALTH_RED = (150, 30, 30)
HEALTH_GREEN = (30, 130, 40)

class VikingPlayer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 50
        self.speed = 5
        self.health = 15
        self.max_health = 15

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed
        # Keep player on screen
        self.x = max(20, min(SCREEN_WIDTH - 60, self.x))
        self.y = max(70, min(SCREEN_HEIGHT - 70, self.y))

    def draw(self, surface):
        # Draw Viking body (Tunic & Shield representation)
        body_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(surface, VIKING_BLUE, body_rect, border_radius=6)
        # Helmet detail
        helmet_rect = pygame.Rect(self.x + 5, self.y - 8, 30, 12)
        pygame.draw.rect(surface, (150, 150, 160), helmet_rect, border_radius=3)
        
        # Health Bar
        bar_w = self.width
        pygame.draw.rect(surface, HEALTH_RED, (self.x, self.y - 25, bar_w, 6))
        curr_w = int(bar_w * (self.health / self.max_health))
        pygame.draw.rect(surface, HEALTH_GREEN, (self.x, self.y - 25, curr_w, 6))

class VillainWolf:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 55
        self.height = 35
        self.health = 20
        self.max_health = 20

    def draw(self, surface):
        # Draw Wolf body
        wolf_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(surface, WOLF_CHARCOAL, wolf_rect, border_radius=10)
        # Glowing red eyes
        pygame.draw.circle(surface, (220, 20, 20), (self.x + 12, self.y + 10), 3)

        # Health Bar
        bar_w = self.width
        pygame.draw.rect(surface, HEALTH_RED, (self.x, self.y - 20, bar_w, 6))
        curr_w = int(bar_w * (self.health / self.max_health))
        pygame.draw.rect(surface, HEALTH_GREEN, (self.x, self.y - 20, curr_w, 6))

# Initialize Game Objects
player = VikingPlayer(200, 350)
wolf = VillainWolf(700, 350)

# Game Loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement Input
    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_LEFT] or keys[pygame.K_a]: dx = -1
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]: dx = 1
    if keys[pygame.K_UP] or keys[pygame.K_w]: dy = -1
    if keys[pygame.K_DOWN] or keys[pygame.K_s]: dy = 1
    
    if dx != 0 or dy != 0:
        player.move(dx, dy)

    # Render Background
    screen.fill(BG_COLD_SKY)

    # Draw ground pattern
    for r in range(50, SCREEN_HEIGHT, 40):
        for c in range(0, SCREEN_WIDTH, 40):
            pygame.draw.rect(screen, GRASS_MUTED, (c, r, 38, 38))

    # Draw environment props (Houses & Trees as atmospheric blocks)
    # Longhouse in center
    pygame.draw.rect(screen, HOUSE_BROWN, (420, 220, 140, 90), border_radius=8)
    # Trees around village
    pygame.draw.circle(screen, TREE_GREEN, (100, 150), 35)
    pygame.draw.circle(screen, TREE_GREEN, (850, 160), 35)
    pygame.draw.circle(screen, TREE_GREEN, (250, 520), 30)
    pygame.draw.circle(screen, TREE_GREEN, (750, 500), 30)

    # Draw Characters (Sorted by Y position for depth)
    characters = [player, wolf]
    characters.sort(key=lambda char: char.y)
    for char in characters:
        char.draw(screen)

    # Top UI Header Bar
    ui_rect = pygame.Rect(0, 0, SCREEN_WIDTH, 50)
    pygame.draw.rect(screen, UI_BROWN, ui_rect)
    pygame.draw.line(screen, (30, 20, 15), (0, 50), (SCREEN_WIDTH, 50), 4)

    font = pygame.font.Font(None, 32)
    title_text = font.render("Poke Village — Defend Against the Wolf!", True, WHITE_TEXT)
    screen.blit(title_text, (20, 12))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()