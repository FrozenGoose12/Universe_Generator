import math, pygame, sys, random
def CosmosGenerator(star_density):
    WHITE = (255, 255, 255)
    YELLOW_WHITE = (255, 234, 202)
    RED = (180, 70, 0)
    ASTRAL_BLUE = (90, 140, 255)

    star_scope = int(1000 - (star_density - 1) * 999/99)
    star_density = (screen_info.current_w * screen_info.current_h) // star_scope


    for starborn in range(star_density):
        x = random.randrange(0, screen_info.current_w)
        y = random.randrange(0, screen_info.current_h)

        temperature = random.randint(1, 7)
        if temperature == 1:
            heat = RED
        elif 2 <= temperature <= 5:
            heat = WHITE
        elif temperature == 6:
            heat = YELLOW_WHITE
        elif temperature == 7:
            heat = ASTRAL_BLUE

        radii = random.randint(1, 50)
        if 1 <= radii <= 35:
            starsize = 1
        elif 36 <= radii <= 45:
            starsize = 2
        elif 45 <= radii <= 49:
            starsize = 3
        else:
            starsize = 4

        shine = random.randint(1, 20)
        if shine == 7:
            glow = 2*starsize+ random.randint(5, 9)
            twinkle_surface = pygame.Surface((glow, glow), pygame.SRCALPHA)
            twinkle_surface.set_alpha(50)
            pygame.draw.circle(twinkle_surface, heat,(glow//2, glow//2), glow//2)
            screen.blit(twinkle_surface, (x - (glow//2), y - (glow//2)))

        pygame.draw.circle(screen, heat, (x, y), starsize)
    pygame.display.flip()



def SpiralGalaxyGenerator(size = math.e, density_variation = 3, x_squish = 1, y_squish = 1, bsub = .02, gas_color = (67, 122, 224), gas_variation = 50, center = (-1, -1)):
    if center == (-1, -1):
        center = (screen_info.current_w // 2, screen_info.current_h // 2)

    turns = 4 * math.pi
    a = 1
    b = 1 # spiral intensity


    theta = 0
    bigtheta = random.uniform(0, math.pi * 2)
    print(bigtheta)

    p = x_squish
    q = y_squish



    WHITE = (255, 255, 255)
    CORE_WHITE = (255,248,240)
    YELLOW_WHITE = (255, 234, 202)
    PURPLE_WHITE = (235, 220, 255)
    BLUE_WHITE = (245, 251, 255)
    ETHEREAL_MIST = (76, 66, 54)

    RED = (255, 100, 0)
    BLACK = (0, 0, 0)

    ASTRAL_BLUE =  (90, 140, 255)
    NEBULA_BLUE = (40, 80, 180)
    HYDROGEN = (70, 110, 200)

    NEBULA_PURPLE = (200, 80, 200)
    BLUE_PURPLE = (150, 110, 255)
    VIOLET = (180, 160, 255)

    WARMDUST = (255, 220, 180)
    COOLDUST = (210, 230, 255)

    gas_surface = pygame.Surface((50, 50), pygame.SRCALPHA)
    gas_surface.set_alpha(8)
    pygame.draw.circle(gas_surface, gas_color, (25, 25), 25)




    while True:
        while theta < turns:
            c = random.randint(1, 10)
            if 1 <= c <= 3:
                color = COOLDUST
            elif 3 < c <= 6:
                color = BLUE_PURPLE
            elif c == 7:
                color = NEBULA_PURPLE
            elif c == 8:
                color = PURPLE_WHITE
            elif c == 9:
                color = NEBULA_BLUE
            else:
                color = HYDROGEN

            massive = random.randint(1, 4)
            if massive == 4:
                star_radius = 1
            else:
                star_radius = 2


            #positive spiral
            r = a * math.exp(b * theta)
            x = p * r * math.cos(theta)
            y = q * r * math.sin(theta)

            rotatedx = (math.cos(bigtheta) * x + (-1 * math.sin(bigtheta) * y)) + center[0]
            rotatedy = (math.sin(bigtheta) * x + (math.cos(bigtheta) * y)) + center[1]

            if r >= 10:
                rotatedx += random.randint(-1 * density_variation, density_variation)
                rotatedy += random.randint(-1 * density_variation, density_variation)

            if r <= 100:
                color = CORE_WHITE

            if r >= 40:
                screen.blit(gas_surface, (rotatedx-25 + random.randint(-1 * gas_variation, gas_variation), rotatedy-25 + random.randint(-1 * gas_variation, gas_variation)))

            pygame.draw.circle(screen, color, (rotatedx, rotatedy), star_radius)





            #negative spiral
            r = (-1 * a) * math.exp(b * theta)
            x = p * r * math.cos(theta)
            y = q * r * math.sin(theta)

            rotatedx = (math.cos(bigtheta) * x + (-1 * math.sin(bigtheta) * y)) + center[0]
            rotatedy = (math.sin(bigtheta) * x + (math.cos(bigtheta) * y)) + center[1]

            if r <= -10:
                rotatedx += random.randint(-1 * density_variation, density_variation)
                rotatedy += random.randint(-1 * density_variation, density_variation)

            if r >= -100:
                color = CORE_WHITE

            if r <= -40:
                screen.blit(gas_surface, (rotatedx-25 + random.randint(-1 * gas_variation, gas_variation), rotatedy-25 + random.randint(-1 * gas_variation, gas_variation)))

            pygame.draw.circle(screen, color, (rotatedx, rotatedy), star_radius)



            theta += .05
            pygame.display.flip()

        b -= bsub
        if b > 0:
            theta = 0
            continue
        else:
            break



pygame.init()
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_info = pygame.display.Info()
screen = pygame.display.set_mode((screen_info.current_w - 10, screen_info.current_h - 10)) # windowed

pygame.display.set_caption("Galaxy Generator")
clock = pygame.time.Clock()
clock.tick(60)
screen.fill((0, 0, 0))


CosmosGenerator(45)
SpiralGalaxyGenerator(1.4, 30, 1, 1, .02, (136, 201, 249), 70, (500,500))
# SpiralGalaxyGenerator(1000, 1, .4, .02, (255, 180, 255),50, (500, 500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

