import pygame
import sys

def check_quit(event):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

class Monster:
    def __init__(self, type):
        self.type = type
        if type == "pink":
            self.speed = 1
            self.size = 50
            self.sprite = pygame.image.load('./pictures/monster_pink.png')
        
        elif type == "yellow":
            self.speed = 2
            self.size = 100
            self.sprite = pygame.image.load('./pictures/monster_yellow.png')
        elif type == "red":
            self.speed = 3
            self.size = 150
            self.sprite = pygame.image.load('./pictures/monster_red.png')
        self.rect = self.sprite.get_rect()
        self.position = [50, 50]
        self.rect.center = self.position  
    
    def MonsterMove(self,):
            #self.win = win
            vector = [2, 0]
            self.rect = self.sprite.get_rect()
            self.rect = self.rect.move(vector)
            if self.rect.left < win.left:
                vector[0] = -vector[0]
            elif self.rect.right > win.right:
                vector[0] = -vector[0]
            if self.rect.top < win.top or self.rect.bottom > win.bottom:
                vector[1] = -vector[1]

#def createMonsterList():
    
    # Initialize Pygame
pygame.init()
pygame.mixer.init()

# Setup values
window_width = 1000
window_height = 500
fpsClock = pygame.time.Clock()
fps = 60
#background
game_window = pygame.display.set_mode((window_width, window_height))
win = game_window.get_rect()
# monster list
monsterList = []
# Load images
background = pygame.image.load('./pictures/background_hell.jpg')
pygame.display.set_caption('MonsterHunter')
pygame.display.set_icon(pygame.image.load('./pictures/monster_red.png'))
# Setting monster queue

# starting game state
state = "menu"







def main():
    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_window.blit(background, (0, 0))
        # Draw the monsters
        
        
    

        # Update the display
        fpsClock.tick(fps)
        pygame.display.flip()


if __name__ == "__main__":
    main()