# Start off by importing pygame and random (used to generate random numbers)
 
import pygame
import random

# Initialize pygame

pygame.init()

# Create screen size

screen_width = 1080
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

# Create one player object and at least three enemies using pictures located in folder
# (copy direct name ie .png or .jpg)


player = pygame.image.load("player.jpg")
enemy1 = pygame.image.load("enemy.png")
enemy2 = pygame.image.load("enemy.png")
monster1 = pygame.image.load("monster.jpg")
monster2 = pygame.image.load("monster.jpg")

# Get the width and height of the images in order to do boundary detection
# (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).
# picture used for enemy1 and enemy2 is the same. Get width and height for monster image 

image_height = player.get_height()
image_width = player.get_width()

enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()

enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()

monster1_height = monster1.get_height()
monster1_width = monster1.get_width()

monster2_height = monster2.get_height()
monster2_width = monster2.get_width()

print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

# Store the positions of the player and enemy as variables so that you can change them later. 

playerXPosition = 100
playerYPosition = 50

# Make the enemies start off screen and at a random y position.

enemy1XPosition =  screen_width
enemy1YPosition =  random.randint(0, screen_height - enemy1_height)

enemy2XPosition =  screen_width
enemy2YPosition =  random.randint(0, screen_height - enemy2_height)

monster1XPosition =  screen_width
monster1YPosition =  random.randint(0, screen_height - monster1_height)

monster2XPosition =  screen_width
monster2YPosition =  random.randint(0, screen_height - monster2_height)

# This checks if the up or down key is pressed.

keyUp= False
keyDown = False

# represent real time game play. Loops so screen is constatntly updated, will loop until told otherwise

while 1: 

    screen.fill(0) # Clears the screen.
    screen.blit(player, (int(playerXPosition), int(playerYPosition)))# This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(enemy1, (int(enemy1XPosition), int(enemy1YPosition)))
    screen.blit(enemy2, (int(enemy2XPosition), int(enemy2YPosition)))
    screen.blit(monster1, (int(monster1XPosition), int(monster1YPosition)))
    screen.blit(monster2, (int(monster2XPosition), int(monster2YPosition)))
    
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.

    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            
        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:

            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP: 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
                
    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemies:
    
    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = int(enemy1XPosition)

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = int(enemy2XPosition)

    monster1Box = pygame.Rect(monster1.get_rect())
    monster1Box.top = monster1YPosition
    monster1Box.left = int(monster1XPosition)

    monster2Box = pygame.Rect(monster2.get_rect())
    monster2Box.top = monster2YPosition
    monster2Box.left = int(monster2XPosition)

    # Test collision of the player and enemy1:
    
    if playerBox.colliderect(enemy1Box):
        print("You lose!")
        pygame.quit()
        exit(0)

        
    # Test collision of the player and enemy2:
    
    if playerBox.colliderect(enemy2Box):
        print("You lose!")
        pygame.quit()
        exit(0)
        
    # Test collision of the player and monster1:
    
    if playerBox.colliderect(monster1Box):
        print("You lose!")
        pygame.quit()
        exit(0)
        
    # Test collision of the player and monster2:
    
    if playerBox.colliderect(monster2Box):
        print("You lose!")
        pygame.quit()
        exit(0)
        
# If enemy1, enemy2, monster 1 and monster2 are all off the screen the user wins the game:
    
    if enemy1XPosition < 0 - enemy1_width and enemy2XPosition < 0 - enemy2_width and monster1XPosition < 0 - monster1_width and monster2XPosition < 0 - monster2_width:
    
        # Display wining status to the user: 
        
        print("You win!")
        
        # Quite game and exit window: 
        pygame.quit()
        
        exit(0)

    
    # Make enemies approach the player.
    
    enemy1XPosition -= 0.15
    enemy2XPosition -= 0.15
    monster1XPosition -= 0.15
    monster2XPosition -= 0.15
    
    # ================The game loop logic ends here. =============
  


            
