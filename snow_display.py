import pygame
import random

magenta = [71, 23, 63]
icyblue  = [220, 246, 252]
darkblue = [17, 9, 54]
display_size = [300,550]
screen = pygame.display.set_mode(display_size)
pygame.display.set_caption("White Christmas!")
global snow

def main():
    snowfall_position()
 
def snowfall_position():
    snow = []
    for _ in range(55):
        x = random.randrange(0, 350)
        y = random.randrange(0, 550)
        snow.append([x, y])
    timer = pygame.time.Clock()             # allows to keep track of time                    
    occurence = False
    while not occurence:                             # snowfall happens until display closed
        for i in pygame.event.get():  
            if i.type == pygame.QUIT:  
                occurence = True
        screen.fill(magenta)
        for i in range(len(snow)):
            pygame.draw.circle(screen, icyblue, snow[i], 2)
    
            snow[i][1] += 1.5
            if snow[i][1] > 550:
                y = random.randrange(-40, -15)
                snow[i][1] = y
            
                x = random.randrange(0, 550)
                snow[i][0] = x
        pygame.display.flip()
        timer.tick(26)
    pygame.quit()

if __name__ == "__main__":
    main()