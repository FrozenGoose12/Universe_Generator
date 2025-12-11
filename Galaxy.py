import math, pygame, sys, random
def CosmosGenerator(star_density):
    WHITE = (255, 255, 255)
    YELLOW_WHITE = (255, 234, 202)
    RED = (180, 70, 0)
    ASTRAL_BLUE = (90, 140, 255)
    YELLOW_ORANGE = (255, 210, 120)

    star_scope = int(1000 - (star_density - 1) * 999/99)
    star_density = (screen_info.current_w * screen_info.current_h) // star_scope

    for starborn in range(star_density):
        x = random.randrange(0, screen_info.current_w)
        y = random.randrange(0, screen_info.current_h)

        temperature = random.randint(1, 7)
        if temperature == 1:
            heat = RED
        elif temperature == 2:
            heat = YELLOW_ORANGE
        elif 3 <= temperature <= 5:
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
            glow = 2*starsize + random.randint(5, 9)
            twinkle_surface = pygame.Surface((glow, glow), pygame.SRCALPHA)
            twinkle_surface.set_alpha(50)
            pygame.draw.circle(twinkle_surface, heat,(glow//2, glow//2), glow//2)
            screen.blit(twinkle_surface, (x - (glow//2), y - (glow//2)))

        pygame.draw.circle(screen, heat, (x, y), starsize)
    pygame.display.flip()


def NebulaGenerator(center, nebula_radius, clouds, max_red, max_green, max_blue, gas_alpha):
    cloud_list = []
    starsize = 4
    WHITE = (255, 255, 255)
    for cloud in range(clouds):
        angle = random.random() * math.tau
        distance = abs(random.gauss(0, nebula_radius / 2))

        x = center[0] + math.cos(angle) * distance
        y = center[1] + math.sin(angle) * distance

        color = (
            random.randint(0, max_red),
            random.randint(0, max_green),
            random.randint(0, max_blue)
        )

        radius = random.randint(10, 35)

        cloud_list.append([x, y, radius, color])


    for x, y, r, color in cloud_list:
        gas_surface = pygame.Surface((2 * r, 2 * r), pygame.SRCALPHA)
        gas_surface.set_alpha(gas_alpha)
        pygame.draw.circle(gas_surface, color, (r, r), r)
        screen.blit(gas_surface, (int(x), int(y)))

        starborn = random.randint(1, 20)
        if starborn == 1:
            glow = 2 * starsize + random.randint(5, 9)
            glow_surface = pygame.Surface((glow, glow), pygame.SRCALPHA)
            glow_surface.set_alpha(30)
            pygame.draw.circle(glow_surface, WHITE, (glow // 2, glow // 2), glow // 2)

            starx = int(x) + random.randint(-10, 10)
            stary = int(y) + random.randint(-10, 10)

            screen.blit(glow_surface, (starx - (glow // 2), stary - (glow // 2)))
            pygame.draw.circle(screen, WHITE, (starx, stary), starsize)

    pygame.display.flip()


def SpiralGalaxyGenerator(max_radius = 1000, turns = 3 * math.pi, bigtheta = random.uniform(0, math.pi * 2), density_variation = 3, x_squish = 1, y_squish = 1, bsub = .02, gas_color = (67, 122, 224), gas_alpha = 7, center = (-1, -1)):
    if center == (-1, -1):
        center = (screen_info.current_w // 2, screen_info.current_h // 2)


    a = 1
    b = 1 # spiral intensity
    theta = 0
    print(bigtheta)

    p = x_squish
    q = y_squish
    core_constant = max_radius//10


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

    gas_variation = max_radius//14
    gas_surface = pygame.Surface((max_radius//10, max_radius//10), pygame.SRCALPHA)
    gas_radius = (max_radius//10)//2
    gas_surface.set_alpha(gas_alpha)
    pygame.draw.circle(gas_surface, gas_color, (gas_radius, gas_radius), gas_radius)

    primary_color = 230 + (core_constant / 100 * 25)



    while True:
        while theta < turns:

            c = random.randint(1, 10)
            if c >= 5:
                color = (primary_color, primary_color, primary_color)
            elif c >= 3:
                color = COOLDUST
            else:
                color = PURPLE_WHITE = (235, 220, 255)



            if max_radius >= 200:
                massive = random.randint(1, 4)
                if massive == 4:
                    star_radius = 1
                else:
                    star_radius = 2
            else:
                star_radius = 1

            #positive spiral
            r = a * math.exp(b * theta)
            x = p * r * math.cos(theta)
            y = q * r * math.sin(theta)
            if r > max_radius:
                break
            rotatedx = (math.cos(bigtheta) * x + (-1 * math.sin(bigtheta) * y)) + center[0]
            rotatedy = (math.sin(bigtheta) * x + (math.cos(bigtheta) * y)) + center[1]

            if r >= core_constant//10: #variation
                rotatedx += random.randint(-1 * density_variation, density_variation)
                rotatedy += random.randint(-1 * density_variation, density_variation)

            if r <= core_constant: #bright_core
                color = CORE_WHITE

            if r >= core_constant: #gas
                screen.blit(gas_surface, (rotatedx - gas_radius + random.randint(-1 * gas_variation, gas_variation), rotatedy - gas_radius + random.randint(-1 * gas_variation, gas_variation)))

            pygame.draw.circle(screen, color, (rotatedx, rotatedy), star_radius)





            #negative spiral
            r = (-1 * a) * math.exp(b * theta)
            x = p * r * math.cos(theta)
            y = q * r * math.sin(theta)

            rotatedx = (math.cos(bigtheta) * x + (-1 * math.sin(bigtheta) * y)) + center[0]
            rotatedy = (math.sin(bigtheta) * x + (math.cos(bigtheta) * y)) + center[1]

            if r <= -core_constant//10: #variation
                rotatedx += random.randint(-1 * density_variation, density_variation)
                rotatedy += random.randint(-1 * density_variation, density_variation)

            if r >= -core_constant: #bright_core
                color = CORE_WHITE

            if r <= -core_constant: #gas
                screen.blit(gas_surface, (rotatedx - gas_radius + random.randint(-1 * gas_variation, gas_variation), rotatedy - gas_radius + random.randint(-1 * gas_variation, gas_variation)))

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

if __name__ == "__main__":
    CosmosGenerator(55)
    # SpiralGalaxyGenerator(200, 3 * math.pi, random.uniform(0, math.pi * 2), 5, 1, 1, .02, (180, 160, 255), 10, (1000,700))
    # SpiralGalaxyGenerator(100, 3 * math.pi, random.uniform(0, math.pi * 2), 5, 1, .4, .02, (210, 230, 255), 15,  (111,340))
    # SpiralGalaxyGenerator(30, 2 * math.pi, random.uniform(0, math.pi * 2), 2, 1, .05, .02, (210, 230, 0), 20, (700,500))
    NebulaGenerator((500, 300), 300, 400, 200, 100, 255, 20)
    NebulaGenerator((1000, 600), 600, 1000, 0, 100, 180, 15)
    NebulaGenerator((20, 200), 100, 100, 50, 160, 250, 10)
    NebulaGenerator((1299, 100), 400, 670, 250, 167, 220, 30)

    SpiralGalaxyGenerator(500, 5 * math.pi, .5 , 3, 1, .3, .02, (150, 60, 200), 2, (500,650))
    SpiralGalaxyGenerator(200, 3 * math.pi, 1 , 2, 1, .2, .02, (170, 102, 240), 2, (800,200))
    #bigger radius needs bigger turns
    # bigtheta recommendation = random.uniform(0, math.pi * 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


