import pygame
import sys
import random
import os

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gra")


WHITE = (0, 0, 0)
PINK = (255,192,203)

font = pygame.font.SysFont("Arial", 28)

point_sound = pygame.mixer.Sound("point.wav")
lose_life_sound = pygame.mixer.Sound("lose.wav")

state = "menu"


pygame.mixer.music.load("background.wav")  
pygame.mixer.music.set_volume(0.05)  
pygame.mixer.music.play(-1)


def load_high_scores():
    if os.path.exists("highscores.txt"):
        with open("highscores.txt", "r") as f:
            lines = f.readlines()
            return [int(line.strip()) for line in lines if line.strip().isdigit()]
    else:
        return []

def save_high_scores(scores):
    with open("highscores.txt", "w") as f:
        for score in scores:
            f.write(str(score) + "\n")

high_scores = load_high_scores()


def draw_text(text, x, y):
    txt = font.render(text, True, WHITE)
    screen.blit(txt, (x, y))

def menu_screen():
    screen.fill(PINK)
    draw_text("MENU GŁÓWNE", 250, 100)
    draw_text("1. Start gry", 250, 180)
    draw_text("2. Zasady gry", 250, 230)
    draw_text("3. Najlepsze wyniki", 250, 280)
    draw_text("4. Zakończ", 250, 330)
    pygame.display.flip()

def game_loop():
    global high_scores,score, lives, state
    player_rect = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 60, 50, 30)
    enemy_rect = pygame.Rect(random.randint(0, WIDTH - 40), 0, 40, 40)
    velocity = 7
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill(PINK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_rect.x -= velocity
            if player_rect.x < 0:
                player_rect.x = 0
        if keys[pygame.K_RIGHT]:
            player_rect.x += velocity
            if player_rect.x > WIDTH - player_rect.width:
                player_rect.x = WIDTH - player_rect.width

        enemy_rect.y += 5

        if player_rect.colliderect(enemy_rect):
            point_sound.play()
            score += 10
            enemy_rect.x = random.randint(0, WIDTH - enemy_rect.width)
            enemy_rect.y = 0

        if enemy_rect.y > HEIGHT:
            lose_life_sound.play()
            lives -= 1
            enemy_rect.x = random.randint(0, WIDTH - enemy_rect.width)
            enemy_rect.y = 0
            if lives == 0:
                high_scores.append(score)
                high_scores.sort(reverse=True)
                del high_scores[5:] 
                save_high_scores(high_scores) 
                state = "menu"
                return

        pygame.draw.rect(screen, WHITE, player_rect)
        pygame.draw.rect(screen, (255,20,147), enemy_rect)
        draw_text(f"Punkty: {score}", 10, 10)
        draw_text(f"Życia: {lives}", 10, 50)

        pygame.display.flip()
        clock.tick(60)

def rules_screen():
    screen.fill(PINK)
    draw_text("Zasady gry:", 100, 100)
    draw_text("Poruszaj się lewo/prawo, łap spadające kwadraty.", 100, 150)
    draw_text("Za każdego złapanego dostajesz 10 pkt.", 100, 190)
    draw_text("Jeśli kwadrat spadnie na dół, tracisz życie.", 100, 230)
    draw_text("Masz 3 życia. Powodzenia!", 100, 270)
    draw_text("Wciśnij ESC, by wrócić.", 100, 320)
    pygame.display.flip()

def high_scores_screen():
    global high_scores
    screen.fill(PINK)
    draw_text("Najlepsze wyniki:", 100, 100)
    for i, s in enumerate(high_scores):
        draw_text(f"{i+1}. {s} pkt", 100, 150 + i * 40)
    draw_text("Wciśnij ESC, by wrócić.", 100, 350)
    pygame.display.flip()

while True:
    if state == "menu":
        menu_screen()
    elif state == "game":
        game_loop()
    elif state == "rules":
        rules_screen()
    elif state == "highscores":
        high_scores_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if state == "menu":
                if event.key == pygame.K_1:
                    score = 0
                    lives = 3
                    state = "game"
                elif event.key == pygame.K_2:
                    state = "rules"
                elif event.key == pygame.K_3:
                    state = "highscores"
                elif event.key == pygame.K_4:
                    pygame.quit()
                    sys.exit()
            else:
                if event.key == pygame.K_ESCAPE:
                    state = "menu"
