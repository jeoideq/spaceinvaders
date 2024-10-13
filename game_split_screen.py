import pygame 
pygame.init()

WIDTH=1000
HEIGHT=800
TITLE=("GAME")

bullets1=[]
bullets2=[]

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

health1=10
health2=10

p1=pygame.image.load("rocket1.png")
p2=pygame.image.load("rocket2.png")
p1=pygame.transform.scale(p1,(100,100))
p2=pygame.transform.scale(p2,(100,100))
p1=pygame.transform.rotate(p1,90)
p2=pygame.transform.rotate(p2,270)

background=pygame.image.load("space2.png")

class Game(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y


player1=Game(150,150,p1)
player2=Game(600,150,p2)

sprites=pygame.sprite.Group()
sprites.add(player1)
sprites.add(player2)

def handle_bullets():
    global health2,health1
    for bullet in bullets1:
        pygame.draw.rect(screen,"red",bullet,0)
        bullet.x+=5
        if bullet.colliderect(player2.rect):
            health2-=1
            bullets1.remove(bullet)
            
            

    
    for bullet in bullets2:
        
        pygame.draw.rect(screen,"yellow",bullet,0)
        bullet.x-=5
        



run=True
while run:
    screen.blit(background, (0,0))
    sprites.draw(screen)
    pygame.draw.line(screen,"black",(500,0),(500,800),4)
    handle_bullets()


    
    
    font=pygame.font.SysFont("Arial",40)
    message1=font.render("HEALTH"+str(health1), True,"black")
    screen.blit(message1,(50,50))

     
    font=pygame.font.SysFont("Arial",40)
    message2=font.render("HEALTH"+str(health2), True,"black")
    screen.blit(message2,(750,50))

    
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            run=False
    keys=pygame.key.get_pressed()
    if keys [pygame.K_w]:
        player1.rect.y +=5
    if keys [pygame.K_s]:
        player1.rect.y -=5
    if keys [pygame.K_a]:
         player1.rect.x +=5
    if keys [pygame.K_d]:
        player1.rect.x -=5
    if player1.rect.left<0:
        player1.rect.left=0
    if player1.rect.right>500:
        player1.rect.right=500
    if player1.rect.top<0:
        player1.rect.top=0
    if player1.rect.bottom>800:
        player1.rect.bottom=800
    if keys [pygame.K_x]:
        bullet=pygame.Rect(player1.rect.x+100,player1.rect.y+50,10,5)
        bullets1.append(bullet)
        

    keys=pygame.key.get_pressed()
    if keys [pygame.K_UP]:
        player2.rect.y +=5
    if keys [pygame.K_DOWN]:
        player2.rect.y -=5
    if keys [pygame.K_LEFT]:
         player2.rect.x +=5
    if keys [pygame.K_RIGHT]:
        player2.rect.x -=5
    if player2.rect.left<500:
        player2.rect.left=500
    if player2.rect.right>1000:
        player2.rect.right=1000
    if player2.rect.top<0:
        player2.rect.top=0
    if player2.rect.bottom>800:
        player2.rect.bottom=800
    if keys [pygame.K_m]:
        bullet=pygame.Rect(player2.rect.x,player2.rect.y+50,10,5)
        bullets2.append(bullet)



    
    pygame.display.update()

    
        


        








