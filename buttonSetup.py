import pygame

pygame.init()

class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.clicked = False

#buttons
playButton = Button(150, 220, pygame.image.load('./pictures/play.png'), 0.7 )
settingsButton = Button(150, 320, pygame.image.load('./pictures/settings.png'), 0.7 )
exitButton = Button(150, 420, pygame.image.load('./pictures/exit.png'), 0.7 )
muteButton = Button(500, 450, pygame.image.load('./pictures/mute.png'), 0.7 )
backButton = Button(500, 550, pygame.image.load('./pictures/back.png'), 0.7 )
resetButton = Button(500, 350, pygame.image.load('./pictures/reset.png'), 0.7 )
mainMenuButton = Button(500, 350, pygame.image.load('./pictures/backToMenu.png'), 0.7 )