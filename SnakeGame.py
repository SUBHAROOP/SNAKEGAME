# snake game
#by roots
#imports
import pygame, sys, random, time
check_errors=pygame.init()
if check_errors[1]>0:
    print("(!)Had {0} initializing errors,existing...".format(check_errors[1]))
    sys.exit(-1)
else:    
     print("(+)Pygame successfully intialized!")
# Play surface
playSurface=pygame.display.set_mode((720,460))
pygame.display.set_caption('Snake game!')
# color
red=pygame.Color(255,0,0)#game over
green=pygame.Color(0,255,0)#snake food
black=pygame.Color(0,0,0)#score
white=pygame.Color(255,255,255)#background
brown=pygame.Color(165,42,42)#food
#FPS CONTROLLER
fpsController=pygame.time.Clock()
snakePos=[100,50]
snakeBody=[[100,50],[90,50],[80,50]]
foodPos=[random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn=True
#direction
direction='RIGHT'
changeto=direction

score = 0
# Game over Function
def  gameOver():
     myFont = pygame.font.SysFont('monaco',72)
     GOsurf=myFont.render('Game Over!',True,red)
     GOrect=GOsurf.get_rect()
     GOrect.midtop=(360,15)     
     playSurface.blit(GOsurf,GOrect)
     showScore(0)
     pygame.display.flip()
     time.sleep(4)
     pygame.quit()
     sys.exit()
def showScore(choice=1):    
    sFont = pygame.font.SysFont('monaco',24)
    Ssurf=sFont.render('Score:{0}'.format(score),True,black)
    Srect=Ssurf.get_rect()
    if choice == 1:
        Srect.midtop =(80, 10)
    else:
         Srect.midtop =(360, 120)
    playSurface.blit(Ssurf,Srect)
    
# Main logic of the game
while 1:
     for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto= 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto= 'LEFT'     
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto= 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto= 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
    # validation direction
     if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
     if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
     if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
     if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    # Update snake positon    
     if direction == 'RIGHT':
        snakePos[0] += 10
     if direction == 'LEFT':
        snakePos[0] -= 10    
     if direction == 'UP':
        snakePos[1] -= 10    
     if direction == 'DOWN':
        snakePos[1] += 10
    # Snake Body Mechanism
     snakeBody.insert(0,list(snakePos))
     if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodSpawn =False
     else:
         snakeBody.pop()
     if  foodSpawn ==False:
         foodPos=[random.randrange(1,72)*10,random.randrange(1,46)*10]
     foodSpawn=True
     playSurface.fill(white)
     for pos in snakeBody:
        pygame.draw.rect(playSurface,green,
        pygame.Rect(pos[0],pos[1],10,10))
        pygame.draw.rect(playSurface,brown,
        pygame.Rect(foodPos[0],foodPos[1],10,10))
   # Bound
        if snakePos[0] > 710 or snakePos[0] < 0:
            gameOver()
        if snakePos[1] > 450 or snakePos[1] < 0:
            gameOver()
        for block in snakeBody[1:]:
            if snakePos[0] == block[0] and snakePos[1] == block[1]:
                gameOver()
    
        showScore()
        pygame.display.flip()

        fpsController.tick(42)
    
    
