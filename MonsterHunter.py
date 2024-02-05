import pygame
import random
import buttonSetup

class Monster:
    def __init__(self, type):
        """
        Initialize a Monster object.

        Parameters:
        - type (str): The type of the monster.

        Returns:
        None
        """
        self.type = type
        if type == "1":
            self.speed = 4
            self.sprite = pygame.transform.scale_by(pygame.image.load('./pictures/monster_pink.png'), 1/5)
        elif type == "2":
            self.speed = 5
            self.sprite = pygame.transform.scale_by(pygame.image.load('./pictures/monster_yellow.png'), 1/6) 
        elif type == "3":
            self.speed = 6
            self.sprite = pygame.transform.scale_by(pygame.image.load('./pictures/monster_red.png'), 1/8)
        self.alive = True
        self.rect = self.sprite.get_rect()
        multiplier = 0
        while multiplier == 0:
            multiplier = random.randint(-1, 1)
        self.vector = [multiplier*self.speed, multiplier*self.speed]
        self.position = [random.randint(0+self.rect.width,1000-self.rect.width), random.randint(0+self.rect.height,500-self.rect.height)]
        self.rect.center = self.position  

def button(button):
    """
    Handle button click events.

    Parameters:
    - button (Button): The button object.

    Returns:
    bool: True if the button is clicked, False otherwise.
    """
    action = False
    mousePos = pygame.mouse.get_pos()
    game_window.blit(button.image, (button.rect.x, button.rect.y))
    if pygame.mouse.get_pressed()[0] == 1 and button.clicked == False:
        if button.rect.collidepoint(mousePos):
            action = True
            button.clicked = True
    if pygame.mouse.get_pressed()[0] == 0:
        button.clicked = False        
    
    return action

def monsterMove(i):
    """
    Move the monster.

    Parameters:
    - i (int): The index of the monster in the monsterList.

    Returns:
    None
    """
    global monsterList
    if monsterList[i].rect.left < win.left:
        monsterList[i].vector[0] = -monsterList[i].vector[0]
    elif monsterList[i].rect.right > win.right:
        monsterList[i].vector[0] = -monsterList[i].vector[0]
    elif monsterList[i].rect.top < win.top or monsterList[i].rect.bottom > win.bottom-100:
        monsterList[i].vector[1] = -monsterList[i].vector[1]

    monsterList[i].rect = monsterList[i].rect.move(monsterList[i].vector)
    monsterList[i].position = monsterList[i].rect.center

def updateMonsterList(round):
    """
    Update the monster list for the given round.

    Parameters:
    - round (int): The current round.

    Returns:
    None
    """
    global monsterList
    for i in range(0, len(monsterRounds[round])):
        monsterList.append(Monster(monsterRounds[round][i]))

def checkNextRound(curTime, round):
    """
    Check if it's time to move to the next round.

    Parameters:
    - curTime (int): The current time.
    - round (int): The current round.

    Returns:
    bool: True if it's time to move to the next round, False otherwise.
    """
    allDead = True
    for i in monsterList:
        if i.alive == True:
            allDead = False
        
    if (pygame.time.get_ticks() - curTime)/1000 > 5 or round == 1:
        return True
    
    return allDead

def shoot(event, mute):
    """
    Handle the shooting event.

    Parameters:
    - event (pygame.event.Event): The event object.
    - mute (bool): True if the sound is muted, False otherwise.

    Returns:
    None
    """
    global monsterList
    global points
    mousePos = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        for i in monsterList:
            if i.rect.collidepoint(mousePos) and i.alive == True:
                i.alive = False
                if mute == False:
                    pygame.mixer.Sound.play(hit)
                points += 50

def showCrosshair():
    """
    Show the crosshair on the screen.

    Parameters:
    None

    Returns:
    None
    """
    mousePos = pygame.mouse.get_pos()
    crosshair = pygame.image.load('./pictures/target.png')
    game_window.blit(crosshair,(mousePos[0] - crosshair.get_width()/2 ,mousePos[1] - crosshair.get_height()/2))

def showGun():
    """
    Show the gun on the screen.

    Parameters:
    None

    Returns:
    None
    """
    gunRect = pygame.image.load('./pictures/gunfire.png').get_rect()
    gunRect.centerx = window_width/2
    gunRect.bottom = 500
    if pygame.mouse.get_pressed()[0] == 1:
        if pygame.mouse.get_pos()[0]<=500:
            game_window.blit(pygame.image.load('./pictures/gunfire.png'), gunRect)
        else: 
            game_window.blit(pygame.transform.flip(pygame.image.load('./pictures/gunfire.png'), True, False), gunRect)
    else:
        if pygame.mouse.get_pos()[0]<=500:
            game_window.blit(pygame.image.load('./pictures/gun.png'), gunRect)
        else: 
            game_window.blit(pygame.transform.flip(pygame.image.load('./pictures/gun.png'), True, False), gunRect)

def showBar(round):
    """
    Show the score and round information bar on the screen.

    Parameters:
    - round (int): The current round.

    Returns:
    None
    """
    game_window.blit(pygame.image.load('./pictures/bar.png'), (0,500))

    scoreImg = font.render(str(points), True, text_col)
    scoreRect = scoreImg.get_rect()
    scoreRect.center = (620, 550)
    game_window.blit(scoreImg, scoreRect)

    roundImg = font.render('{}/{}'.format(str(round-1), str(len(monsterRounds)-1)), True, text_col)
    roundRect = roundImg.get_rect()
    roundRect.center = (930, 550)
    game_window.blit(roundImg, roundRect)

def showScores(highestScore):
    """
    Show the highest score and current score on the screen.

    Parameters:
    - highestScore (int): The highest score.

    Returns:
    None
    """
    game_window.blit(pygame.image.load('./pictures/scoreOverlay.png'), (0, 0))

    highScoreImg = font.render(str(highestScore), True, text_col)
    highScoreRect = highScoreImg.get_rect()
    highScoreRect.center = (620, 75)
    game_window.blit(highScoreImg, highScoreRect)

    scoreImg = font.render(str(points), True, text_col)
    scoreRect = scoreImg.get_rect()
    scoreRect.center = (580, 125)
    game_window.blit(scoreImg, scoreRect)


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
backgroundMainMenu = pygame.image.load('./pictures/mainmenu.png')
pygame.display.set_caption('MonsterHunter')
pygame.display.set_icon(pygame.image.load('./pictures/monster_red.png'))

#Load font
font = pygame.font.SysFont("Ethnocentric", 50)
text_col = (255, 255, 255)

# Load sounds
gunshot = pygame.mixer.Sound('./sounds/gunshot.mp3')
hit = pygame.mixer.Sound('./sounds/kill.mp3')

pygame.mouse.set_visible(False)

# Setting monster queue
monsterRounds = {
    1:"1111223",
    2:"11222233",
    3:"1111222223333",
    4:"3333333333",
    5:""
}

points = 0


def main():
    # starting game state
    global monsterList
    global points
    state = "main menu"
    nextRound = 1
    currentRoundTime = 10000
    mute = False
    winFlag = False

    # set current highest score
    try:
        f = open("score.txt")
        highestScore = f.read()
        f.close()
    except:
        f = open("score.txt", "w")
        f.write('0')
        highestScore = 0
        f.close()

    #start the soundtrack
    pygame.mixer.music.load("./sounds/soundtrack.mp3") 
    pygame.mixer.music.play(-1,0.0)

    # Game loop
    running = True

    while running:
        match(state):
            case 'game':
                
                round = nextRound

                if checkNextRound(currentRoundTime, round):
                    if round > len(monsterRounds)-1:
                        state = 'win'
                    updateMonsterList(round)
                    currentRoundTime = pygame.time.get_ticks()
                    
                    nextRound += 1

                #event handler
                for event in pygame.event.get():
                    #check quit
                    if event.type == pygame.QUIT:
                        running = False
                    
                    shoot(event, mute)

                    #shoot sound
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mute == False:
                        pygame.mixer.Sound.play(gunshot)

                    
                    
                game_window.blit(background, (0, 0))
                # Draw the monsters
                for i in range (0, len(monsterList)):
                    monsterMove(i)
                    
                    if monsterList[i].alive == True:
                        game_window.blit(monsterList[i].sprite, monsterList[i].rect)
                
                # Draw the crosshair
                showBar(round)
                showCrosshair()
                showGun()

            case 'main menu':
                game_window.blit(backgroundMainMenu, (0, 0))
                #event handler
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                    #shoot sound
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mute == False:
                        pygame.mixer.Sound.play(gunshot)

                    
                if button(buttonSetup.playButton):
                    state = 'game'    
                    nextRound = 1
                    round = 1
                    monsterList = []
                    points = 0
                if button(buttonSetup.settingsButton):
                    state = 'settings'
                if button(buttonSetup.exitButton):
                    running = False
                showCrosshair()
                    
            case 'settings':
                game_window.blit(backgroundMainMenu, (0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                    #shoot sound
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mute == False:
                        pygame.mixer.Sound.play(gunshot)

                if button(buttonSetup.backButton):
                    state = 'main menu'
                
                if button(buttonSetup.resetButton):
                    highestScore = 0
                
                if mute == False:
                    if button(buttonSetup.muteButton):
                        pygame.mixer.music.pause()
                        mute = True
                else:
                    if button(buttonSetup.muteButton):
                        pygame.mixer.music.unpause()
                        mute = False

                showCrosshair()
            
            case 'win':
                game_window.blit(background, (0, 0))
                if points > int(highestScore):
                    highestScore = str(points)
                
                showScores(highestScore)

                #event handler
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                    #shoot sound
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mute == False:
                        pygame.mixer.Sound.play(gunshot)

                
                if button(buttonSetup.mainMenuButton):
                    state = 'main menu'

                showBar(round)
                showCrosshair()
                
        # Update the display
        fpsClock.tick(fps)
        pygame.display.flip()

    f = open('score.txt', 'w')
    f.write(str(highestScore))
    f.close()

if __name__ == "__main__":
    main()