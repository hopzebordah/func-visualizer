import pygame, sys, math, time
from funcInputTool import getInput

def init():
    global W, H
    W, H = 1000, 500

    global BLACK, WHITE
    BLACK = (0,   0,   0)
    WHITE = (255, 255, 255)

    global x_offset, frequency, ampIncrement
    x_offset = 0
    frequency = 5430
    ampIncrement = 3
    
    global func
    func = math.sin

    frequency, ampIncrement, func = getInput(frequency, ampIncrement, func)

    global lineThickness
    lineThickness = 2

    global framerate
    framerate = 30

    global clock
    clock = pygame.time.Clock()

    global screen
    pygame.display.init()
    screen = pygame.display.set_mode([W, H])
    pygame.display.set_caption('Trig Function Visualizer')

def wipeScreen(color):
    global screen
    screen.fill(color)

def main():
    global x_offset, frequency, ampIncrement
    global func
    
    amplitude = 1
    pause = False  
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_r:
                    ff = False
                    x_offset = 0
                    frequency = 75
                    amplitude = 600
                if event.key == pygame.K_COMMA:
                    frequency -= 20
                elif event.key == pygame.K_PERIOD:
                    frequency += 20

        if not pause:
            plotPoints = []
            for x in range(W):
                y = int(func((x + x_offset)/float(W) * (frequency * math.pi)) * amplitude + H/2)
                plotPoints.append((x, y))
                if x % 10 == 0:
                    if x < W/4: amplitude += ampIncrement
                    elif x < W/2: amplitude -= ampIncrement
                    elif x < W - W/4: amplitude += ampIncrement
                    elif x < W: amplitude -= ampIncrement
        
            wipeScreen(BLACK)
            pygame.draw.lines(screen, WHITE, False, plotPoints, lineThickness)
            pygame.display.flip()

            clock.tick(framerate)

            if x_offset > 4000: x_offset = 0
            else: x_offset += 2        
            
        else:
            frequency, ampIncrement, func = getInput(frequency, ampIncrement, func)
            pause = False
            time.sleep(0.1)
            

        amplitude = 1

if __name__ == '__main__':
    init()
    main()


