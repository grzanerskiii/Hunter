import pygame
import sys
def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

class Monster:
    def __init__(self, monster_type, position):
        self.type = monster_type
        self.position = position
        if monster_type == "pink":
            self.speed = 1
            self.size = 50
            self.sprite = pygame.image.load('./pictures/monster_pink.png')
        elif monster_type == "yellow":
            self.speed = 2
            self.size = 100
            self.sprite = pygame.image.load('./pictures/monster_yellow.png')
        elif monster_type == "red":
            self.speed = 3
            self.size = 150
            self.sprite = pygame.image.load('./pictures/monster_red.png')
        self.rect = self.sprite.get_rect()
        self.rect.center = self.position

def MonsterMove(monster, win):
    vector = [2, 0]
    monster.rect = monster.sprite.get_rect()
    monster.rect = monster.rect.move(vector)
    if monster.rect.left < win.left or monster.rect.right > win.right:
        vector[0] = -vector[0]
    if monster.rect.top < win.top or monster.rect.bottom > win.bottom:
        vector[1] = -vector[1]
    monster.position[0] += vector[0]
    monster.position[1] += vector[1]

def main():
    pygame.init()
    pygame.mixer.init()

    window_width = 1000
    window_height = 500
    game_window = pygame.display.set_mode((window_width, window_height))
    win = game_window.get_rect()

    fpsClock = pygame.time.Clock()
    fps = 60

    background = pygame.image.load('./pictures/background_hell.jpg')
    pygame.display.set_caption('MonsterHunter')
    pygame.display.set_icon(pygame.image.load('./pictures/monster_red.png'))

    running = True
    while running:
        check_quit()

        game_window.blit(background, (0, 0))

        monster1 = Monster("pink", [50, 50])
        monster2 = Monster("yellow", [200, 200])
        monster3 = Monster("red", [400, 400])

        MonsterMove(monster1, win)
        MonsterMove(monster2, win)
        MonsterMove(monster3, win)

        # Draw the monsters after updating their positions
        game_window.blit(monster1.sprite, monster1.position)
        game_window.blit(monster2.sprite, monster2.position)
        game_window.blit(monster3.sprite, monster3.position)

        pygame.display.flip()
        fpsClock.tick(fps)

if __name__ == "__main__":
    main()
