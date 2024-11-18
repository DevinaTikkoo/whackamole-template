import random

import pygame

square_size = 32
#32*16=512
screen_height = 512
#32*20=640
screen_width = 640

mole_x = 0
mole_y = 0

def draw_lines(screen,color,square_size):
    #vertical lines drawn every 32 x-values
    for x in range(0,screen_width, square_size):
        pygame.draw.line(screen,color,(x,0),(x,screen_height))
    #horizontal lines drawn every y-value
    for y in range(0, screen_height,square_size):
        pygame.draw.line(screen,color,(0,y),(screen_width, y))

def did_click_mole(mouse_x,mouse_y,mole_x,mole_y,square_size):
    #check which square the mouse is in
    grid_x = mouse_x//square_size
    grid_y = mouse_y//square_size
    if grid_x == mole_x and grid_y == mole_y:
        return True
    else:
        return False

def main():
    mole_x = 0
    mole_y = 0
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                #initialize mouse positions
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    #check if mouse and mole touch and then move mole to random grid
                    if did_click_mole(mouse_x,mouse_y,mole_x,mole_y,square_size):
                        mole_x = random.randrange(20)
                        mole_y = random.randrange(16)
        #make background
            screen.fill("tan")

        #draw grid
            draw_lines(screen,(0,0,0),square_size)

        #mole in position
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x*square_size, mole_y*square_size)))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
