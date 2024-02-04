import pygame
import sys
import random
import time

# def check_quit(event):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit() 

class Monster:
    def __init__(self, type):
        self.type = type
        if type == "1":
            self.speed = 1
            self.sprite = pygame.transform.scale_by(pygame.image.load('./pictures/monster_pink.png'), 1/3)
        elif type == "2":
            self.speed = 2
            self.sprite = pygame.transform.scale_by(pygame.image.load('./pictures/monster_yellow.png'), 1/4) 
        elif type == "3":
            self.speed = 3
            self.sprite = pygame.transform.scale_by(pygame.image.load('./pictures/monster_red.png'), 1/5)
        self.alive = True
        self.rect = self.sprite.get_rect()
        self.vector = [self.speed, self.speed]
        self.position = [random.randint(0+self.rect.width,1000-self.rect.width), random.randint(0+self.rect.height,500-self.rect.height)]
        self.rect.center = self.position  
    
def monsterMove(i):
    global monsterList
    if monsterList[i].rect.left < win.left:
        monsterList[i].vector[0] = -monsterList[i].vector[0]
    elif monsterList[i].rect.right > win.right:
        monsterList[i].vector[0] = -monsterList[i].vector[0]
    elif monsterList[i].rect.top < win.top or monsterList[i].rect.bottom > win.bottom-100:
        monsterList[i].vector[1] = -monsterList[i].vector[1]

    monsterList[i].rect = monsterList[i].rect.move(monsterList[i].vector)
    monsterList[i].position = monsterList[i].rect.center
        
    
# def monsterDraw():
#     for i in range (0, len(monsterList)):
#         game_window.blit(monsterList[i].sprite, monsterList[i].position)

def updateMonsterList(round):
    global monsterList
    for i in range(0, len(monsterRounds[round])):
        monsterList.append(Monster(monsterRounds[round][i]))
        
def checkNextRound(curTime, firstRound):
    allDead = True
    for i in monsterList:
        if i.alive == True:
            allDead = False
        
    if (pygame.time.get_ticks() - curTime)/1000 > 2 or firstRound == True:
        return True
    
    return allDead

def shoot(event):
    global monsterList
    global points
    mousePos = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        for i in monsterList:
            if i.rect.collidepoint(mousePos):
                i.alive = False
                points += 50

def showCrosshair():
    mousePos = pygame.mouse.get_pos()
    crosshair = pygame.image.load('./pictures/target.png')
    game_window.blit(crosshair,(mousePos[0] - crosshair.get_width()/2 ,mousePos[1] - crosshair.get_height()/2))

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Setup values
window_width = 1000
window_height = 600
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

pygame.mouse.set_visible(False)

# Setting monster queue
monsterRounds = {
    1:"111",
    2:"222",
    3:"333",
    4:''
}

points = 0


def main():
    # starting game state
    state = "game"

    round = 1
    currentRoundTime = 10000
    firstRound = True 

    # Game loop
    running = True

    while running:
        match(state):
            case 'game':
                print(points)
                if checkNextRound(currentRoundTime, firstRound):
                    updateMonsterList(round)
                    firstRound = False
                    currentRoundTime = pygame.time.get_ticks()
                    #tmp
                    if round > 3:
                        state = 'main menu'
                    print(round)
                    round += 1

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    shoot(event)
                    
                game_window.blit(background, (0, 0))
                # Draw the monsters
                for i in range (0, len(monsterList)):
                    monsterMove(i)
                    
                    if monsterList[i].alive == True:
                        game_window.blit(monsterList[i].sprite, monsterList[i].rect)
                
                # Draw the crosshair
                showCrosshair()

            case 'main menu':
                game_window.blit(background, (0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
            

        
        # Update the display
        fpsClock.tick(fps)
        pygame.display.flip()


if __name__ == "__main__":
    main()