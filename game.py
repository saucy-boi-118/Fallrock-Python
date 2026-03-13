#import functions
import pygame
import random
import functions



# init pygame
pygame.init()

# change logo
pygame.display.set_icon(pygame.image.load("kitten.jpeg"))

# change name
pygame.display.set_caption("Falling Rocks", "lock")

# init screen
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
running = True
keys = pygame.key.get_pressed

# game variables

# player
p = pygame.Vector2(250,375) # player

# gravity
gravity = 150
dt = clock.get_time() / 1000

# coin
coin_pos = pygame.Vector2(random.randint(50, 450), 390)

# rocks

# rock 1
rock1velo = 0
rock1_pos = pygame.Vector2(random.randint(35, 465), -35)

# rock 2
rock2velo = 0
rock2_pos = pygame.Vector2(random.randint(35, 465), -35)

# score
font = pygame.font.Font(None, 115)
score = 0
scoreT = font.render(f"{score}", True, "#CCCAC0")

# pre game variables
gameOn = False
death = False

# highscore

try:
    highscore = int(functions.getHighScore())
except:
    highscore = 0

font = pygame.font.Font(None, 50)
highscoreT = font.render(f"{highscore}", True, "#C0BEBE")

# place holders
placeholder = font.render("PRESS 'S' To Play", True, "black")
placeholder2 = font.render("press 'S' to play again", True, "black")

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
    
    screen.fill("#6D85D3")


    # game code ----------------->

    # pre game
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        gameOn = True

    # start screen
    if gameOn == False:
        pygame.draw.circle(screen, "grey", (250,250), 175)
        pygame.draw.circle(screen, "black", (250,250), 175, width=25)
        font = pygame.font.Font(None, 45)
        placeholder = font.render("PRESS 'S' To Play", True, "black")
        screen.blit(placeholder, (250-(placeholder.get_width()/2),250))
    
    # if player dies
    if death == True:
        gameOn = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            gameOn = True
            death = False
            score = 0
            rock1_pos.y = -20
            rock2_pos.y = -20
        pygame.draw.circle(screen, "grey", (250,250), 175)
        pygame.draw.circle(screen, "black", (250,250), 175, width=25)
        font = pygame.font.Font(None, 35)
        placeholder2 = font.render("PRESS 'S' To Play Again", True, "black")
        screen.blit(placeholder2, (250-(placeholder2.get_width()/2),250))

    # game is startes
    if gameOn == True:
        # player controls // player

        # gravity for rocks
        
        # rock 1
        rock1velo += gravity * dt
        if (rock1velo > 675): 
            rock1velo -= 20
        rock1_pos.y += rock1velo * dt
        if rock2_pos.y > 550:
            rock2_pos = pygame.Vector2(random.randint(10, 490), random.randint(-50, -35))
            rock2velo = 0

        # rock 2
        rock2velo += gravity * dt
        if (rock2velo > 675): 
            rock2velo -= 20
        rock2_pos.y += rock1velo * dt
        if rock2_pos.y > 550:
            rock2_pos = pygame.Vector2(random.randint(10, 490), random.randint(-50, -35))
            rock2velo = 0


        # collision detect coin -- > player
        if (functions.collideCircs(p, coin_pos, 25, 10)):
            veloY = 0
            coin_pos = pygame.Vector2(random.randint(50, 450), 390)
            score += 1

        # player controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            p.x -= 7
        if keys[pygame.K_d]:
            p.x += 7
        if (p.x > 510): 
            p.x = -10
        if (p.x < -10): 
            p.x = 510

        # collision detect rocks --- > player
        if (functions.collideCircs(p, rock1_pos, 25, 25)): # rock 1
            score -= 1
            rock1_pos = pygame.Vector2(random.randint(10, 490), random.randint(-50, -35))
            rock1velo = 0
            death = True
        
        if (functions.collideCircs(p, rock2_pos, 25, 30)): # rock 2
            score -= 1
            rock2_pos = pygame.Vector2(random.randint(10, 490), random.randint(-50, -35))
            rock2velo = 0
            death = True
        
        # cap score
        if (score < 0):
            score = 0

        # player
        pygame.draw.circle(screen, "#8A7F8D", p, 25)
        pygame.draw.circle(screen, "black", p, 25, width=5)

        # rock
        pygame.draw.circle(screen, "grey", rock1_pos, 25) # rock 1
        pygame.draw.circle(screen, "black", rock1_pos, 25, width=5)
        
        pygame.draw.circle(screen, "grey", rock2_pos, 30) # rock 2
        pygame.draw.circle(screen, "black", rock2_pos, 30, width=5)

        # background
        pygame.draw.rect(screen, "#3DDB57", pygame.Rect(0,400,500,500))
        pygame.draw.rect(screen, "black", pygame.Rect(0,400,500,500), width=5)

        # coin
        pygame.draw.circle(screen, "#F3F024", coin_pos, 10)
        pygame.draw.circle(screen, "black", coin_pos, 10, width=5)

        # score
        pygame.draw.circle(screen, "#F3F024", (50, 50), 25)
        pygame.draw.circle(screen, "black", (50, 50), 25, width=5)
        font = pygame.font.Font(None, 100)
        scoreT = font.render(f"{score}", True, "#000000")
        screen.blit(scoreT, (100-(scoreT.get_width()/2), 20))


        # highscore text and changing
        if (score > highscore):
            highscore = score
        with open("highscore.txt", "w") as f:
            f.write(str(highscore))
        
        font = pygame.font.Font(None, 50)
        highscoreT = font.render(f"High Score: {highscore}", True, "#000000")
        screen.blit(highscoreT, (350-(highscoreT.get_width()/2), 35))
    
    



    # ---------------------------->

    pygame.display.flip()
    clock.tick(60)
    dt = clock.get_time() / 1000

pygame.quit()