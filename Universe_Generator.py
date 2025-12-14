# Copyright (c) 2025 FrozenGoose12
# Permission is granted to use and modify this file for personal
# and educational purposes only. Commercial use is strictly prohibited
# without written permission from the author.

import math, pygame, sys, random

def exit_check():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

def Shooting_Star(Shooting_Star_rng):
    star_list = []

    x = Shooting_Star_rng.randint(0, screen.get_width())
    y = Shooting_Star_rng.randint(0, screen.get_height())

    dx = Shooting_Star_rng.uniform(-5, 5)
    dy = Shooting_Star_rng.uniform(-5, 5)

    shoot_length = Shooting_Star_rng.randint(50, 150)

    for i in range(shoot_length):
        try:
            previous_color = screen.get_at((int(x), int(y)))
        except IndexError:
            break
        star_list.append((x, y, previous_color))
        x += dx
        y += dy


    for light in star_list:
        trail = Shooting_Star_rng.randint(1, 2)
        if trail == 1:
            color = (255, 255, 255)
        else:
            color = (210, 230, 255)
        pygame.draw.circle(screen, color, (int(light[0]), int(light[1])), 1)
        pygame.display.flip()
        pygame.time.delay(1)

    for light in star_list:
        pygame.draw.circle(screen, light[2], (int(light[0]), int(light[1])), 1)
        pygame.display.flip()
        pygame.time.delay(1)

def CosmosGenerator(Cosmos_rng):
    WHITE = (255, 255, 255)
    YELLOW_WHITE = (255, 234, 202)
    RED = (180, 70, 0)
    ASTRAL_BLUE = (90, 140, 255)
    YELLOW_ORANGE = (255, 210, 120)

    star_density = Cosmos_rng.randint(30, 80)
    star_rate = star_density

    star_scope = int(1000 - (star_density - 1) * 999 / 99)
    star_density = (screen.get_width() * screen.get_height()) // star_scope

    for starborn in range(star_density):
        x = Cosmos_rng.randint(0, screen.get_width())
        y = Cosmos_rng.randint(0, screen.get_height())

        temperature = Cosmos_rng.randint(1, 7)
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

        radii = Cosmos_rng.randint(1, 50)
        if 1 <= radii <= 35:
            starsize = 1
        elif 36 <= radii <= 45:
            starsize = 2
        elif 45 <= radii <= 49:
            starsize = 3
        else:
            starsize = 4

        shine = Cosmos_rng.randint(1, 20)
        if shine == 7:
            glow = 2 * starsize + Cosmos_rng.randint(5, 9)
            twinkle_surface = pygame.Surface((glow, glow), pygame.SRCALPHA)
            twinkle_surface.set_alpha(50)
            pygame.draw.circle(twinkle_surface, heat, (glow // 2, glow // 2), glow // 2)
            screen.blit(twinkle_surface, (x - (glow // 2), y - (glow // 2)))

        pygame.draw.circle(screen, heat, (x, y), starsize)
    pygame.display.flip()
    return [star_rate, star_density]


def NebulaGenerator(center, nebula_radius, clouds, red_range = (0, 255), green_range = (0, 255), blue_range = (0, 255), gas_alpha = 50):
    cloud_list = []
    starsize = 4
    WHITE = (255, 255, 255)
    for cloud in range(clouds):
        angle = Nebula_rng.random() * math.tau
        distance = abs(Nebula_rng.gauss(0, nebula_radius / 2))

        x = center[0] + math.cos(angle) * distance
        y = center[1] + math.sin(angle) * distance

        color = (
            Nebula_rng.randint(red_range[0], red_range[1]),
            Nebula_rng.randint(green_range[0], green_range[1]),
            Nebula_rng.randint(blue_range[0], blue_range[1])
        )

        radius = Nebula_rng.randint(10, 35)

        cloud_list.append([x, y, radius, color])


    for x, y, r, color in cloud_list:
        gas_surface = pygame.Surface((2 * r, 2 * r), pygame.SRCALPHA)
        gas_surface.set_alpha(gas_alpha)
        pygame.draw.circle(gas_surface, color, (r, r), r)
        screen.blit(gas_surface, (int(x), int(y)))

        starborn = Nebula_rng.randint(1, 20)
        if starborn == 1:
            glow = 2 * starsize + Nebula_rng.randint(5, 9)
            glow_surface = pygame.Surface((glow, glow), pygame.SRCALPHA)
            glow_surface.set_alpha(30)
            pygame.draw.circle(glow_surface, WHITE, (glow // 2, glow // 2), glow // 2)

            starx = int(x) + Nebula_rng.randint(-10, 10)
            stary = int(y) + Nebula_rng.randint(-10, 10)

            screen.blit(glow_surface, (starx - (glow // 2), stary - (glow // 2)))
            pygame.draw.circle(screen, WHITE, (starx, stary), starsize)

    pygame.display.flip()


def BlackHoleGenerator(bh_radius, rotation, center):
    size = bh_radius
    size2 = bh_radius
    bigtheta = rotation
    a = 4
    b = 3

    l1 = (234, 228, 240)
    l2 = (221, 212, 222)
    l3 = (231, 224, 236)
    l4 = (193, 172, 175)

    if bh_radius >= 200:
        hole_r = int(size2 * 2.15)
        fr_width = 5
    elif bh_radius >= 40:
        hole_r = int(size2 * 2.2)
        fr_width = 4
    elif bh_radius >= 23:
        hole_r = int(size2 * 2.3)
        fr_width = 4
    elif bh_radius >= 10:
        hole_r = int(size2 * 2.4)
        fr_width = 4
    else:
        hole_r = int(size2 * 2.6)
        fr_width = 4

    # glow
    glow_diameter = 15 * bh_radius
    for i in range(30):
        black_hole_glow_surface = pygame.Surface((glow_diameter, glow_diameter), pygame.SRCALPHA)
        black_hole_glow_surface.set_alpha(3)
        pygame.draw.circle(black_hole_glow_surface, l4, (glow_diameter // 2, glow_diameter // 2), glow_diameter // 2)
        screen.blit(black_hole_glow_surface, (center[0] - glow_diameter // 2, center[1] - glow_diameter // 2))
        glow_diameter -= glow_diameter * .03

    pygame.display.flip()

    # outer top
    theta = 0
    for i in range(size):
        if i > size * .5:
            color = l1
        elif i > size * .3:
            color = l2
        elif i > size * .1:
            color = l3
        else:
            color = l4

        while math.pi >= theta:
            r = size * (a + b * ((abs(math.cos(2 * theta))) ** 2))
            x = (r * math.cos(theta))
            y = (r * math.sin(theta))

            y *= .3

            rotatedx = center[0] - (math.cos(bigtheta) * x + (-1 * math.sin(bigtheta) * y))
            rotatedy = center[1] - (math.sin(bigtheta) * x + (math.cos(bigtheta) * y))

            pygame.draw.circle(screen, color, (rotatedx, rotatedy), fr_width)
            theta += .001
        pygame.display.flip()

        size -= 1
        theta = 0


    # inner hole

    pygame.draw.circle(screen, (0, 0, 0), (center[0], center[1]), hole_r, 0) # black hole
    pygame.draw.circle(screen, (255, 240, 240), (center[0]+1, center[1]-1), hole_r - (hole_r // 8), 1) # inner lense

    warp = hole_r // 4
    for disk in range(warp): # circular disks
        if disk > warp * .5:
            color = l4
            rect = pygame.Rect(center[0] - hole_r, center[1] - hole_r, hole_r * 2, hole_r * 2)
            pygame.draw.arc(screen, color, rect,  (.8 * math.pi)/6 - bigtheta, (5.1 * math.pi)/6 - bigtheta, 1) # top l4
            pygame.draw.arc(screen, color, rect, math.pi - bigtheta, 2 * math.pi - bigtheta, 1) # bottom l4
            hole_r += 1
            continue
        elif disk > warp * .3:
            color = l3
        elif disk > warp * .1:
            color = l2
            rect = pygame.Rect(center[0] - hole_r, center[1] - hole_r, hole_r * 2, hole_r * 2)
            pygame.draw.arc(screen, color, rect, (.8 * math.pi) / 6 - bigtheta, (5.1 * math.pi) / 6 - bigtheta,1)  # top l4
            pygame.draw.arc(screen, color, rect, math.pi - bigtheta, 2 * math.pi - bigtheta, 1)  # bottom l4
            hole_r += 1
            continue
        else:
            color = l1

        hole_r += 1
        pygame.draw.circle(screen, color, (center[0], center[1]), hole_r, 3)
    pygame.display.flip()

    # mid ring
    for i in range(size2 - int(size2//3.25)):
        if i > size2  * .5:
            color = l1
        elif i > size2  * .3:
            color = l2
        elif i > size2  * .1:
            color = l3
        else:
            color = l4

        mringr = size2 * (a + b)
        for x in range(int(-mringr), int(mringr) + 1):
            y = math.sqrt((mringr ** 2) - (x ** 2))
            y *= .13

            rotatedx = center[0] + (math.cos(bigtheta) * x + (-1 * math.sin(bigtheta) * y))
            rotatedy = center[1] + (math.sin(bigtheta) * x + (math.cos(bigtheta) * y))

            pygame.draw.circle(screen, color, (rotatedx, rotatedy), fr_width)
        pygame.display.flip()
        size2 -= 1



def SpiralGalaxyGenerator(max_radius = 1000, turns = 3 * math.pi, bigtheta = random.uniform(0, math.pi * 2), density_variation = 3, x_squish = 1, y_squish = .3, bsub = .02, red_range = (0, 255), green_range = (0, 255), blue_range = (0, 255), gas_alpha = 7, center = (-1, -1)):
    if center == (-1, -1):
        center = (screen.get_width() // 2, screen.get_height() // 2)

    a = 1
    b = 1 # spiral intensity
    theta = 0

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


    primary_color = 230 + (core_constant / 100 * 25)
    if primary_color > 255:
        primary_color = 255


    while True:
        while theta < turns:
            exit_check()
            c = Galaxy_rng.randint(1, 10)
            if c >= 5:
                color = (primary_color, primary_color, primary_color)
            elif c >= 3:
                color = COOLDUST
            else:
                color = PURPLE_WHITE


            if max_radius >= 200:
                massive = Galaxy_rng.randint(1, 4)
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
                rotatedx += Galaxy_rng.randint(-1 * density_variation, density_variation)
                rotatedy += Galaxy_rng.randint(-1 * density_variation, density_variation)

            if r <= core_constant: #bright_core
                color = CORE_WHITE

            if r >= core_constant: #gas
                gas_surface.fill((0, 0, 0, 0))

                gas_color = (
                    Galaxy_rng.randint(red_range[0], red_range[1]),
                    Galaxy_rng.randint(green_range[0], green_range[1]),
                    Galaxy_rng.randint(blue_range[0], blue_range[1])
                )

                pygame.draw.circle(gas_surface, gas_color, (gas_radius, gas_radius), gas_radius)
                screen.blit(gas_surface, (rotatedx - gas_radius + Galaxy_rng.randint(-1 * gas_variation, gas_variation), rotatedy - gas_radius + Galaxy_rng.randint(-1 * gas_variation, gas_variation)))

            pygame.draw.circle(screen, color, (rotatedx, rotatedy), star_radius)





            #negative spiral
            r = (-1 * a) * math.exp(b * theta)
            x = p * r * math.cos(theta)
            y = q * r * math.sin(theta)

            rotatedx = (math.cos(bigtheta) * x + (-1 * math.sin(bigtheta) * y)) + center[0]
            rotatedy = (math.sin(bigtheta) * x + (math.cos(bigtheta) * y)) + center[1]

            if r <= -core_constant//10: #variation
                rotatedx += Galaxy_rng.randint(-1 * density_variation, density_variation)
                rotatedy += Galaxy_rng.randint(-1 * density_variation, density_variation)

            if r >= -core_constant: #bright_core
                color = CORE_WHITE

            if r <= -core_constant: #gas
                gas_surface.fill((0, 0, 0, 0))

                gas_color = (
                    Galaxy_rng.randint(red_range[0], red_range[1]),
                    Galaxy_rng.randint(green_range[0], green_range[1]),
                    Galaxy_rng.randint(blue_range[0], blue_range[1])
                )

                pygame.draw.circle(gas_surface, gas_color, (gas_radius, gas_radius), gas_radius)
                screen.blit(gas_surface, (rotatedx - gas_radius + Galaxy_rng.randint(-1 * gas_variation, gas_variation), rotatedy - gas_radius + Galaxy_rng.randint(-1 * gas_variation, gas_variation)))

            pygame.draw.circle(screen, color, (rotatedx, rotatedy), star_radius)



            theta += .05
            pygame.display.flip()

        b -= bsub
        if b > 0:
            theta = 0
            continue
        else:
            break



def Universe_Generator(Universe_Seed = random.randint(0, 10000), debug = 0):

    Cosmo_rng = random.Random(Universe_Seed + 1) #pre determined seemingly random lists (RNG)
    cosmo_debug = CosmosGenerator(Cosmo_rng)
    if debug == 1:
        print(f"SEED: {Universe_Seed}\nSTAR_RATE: {cosmo_debug[0]}\nSTARS: {cosmo_debug[1]}\n")

    global Nebula_rng
    Nebula_rng = random.Random(Universe_Seed + 2) #pre determined seemingly random lists (RNG)
    for nebula in range(Nebula_rng.randint(3, 6)):

        red_range_start = Nebula_rng.randint(10, 130)
        red_range = (red_range_start, red_range_start + 125)

        green_range_start = Nebula_rng.randint(10, 130)
        green_range = (green_range_start, green_range_start + 10)

        blue_range_start = Nebula_rng.randint(10, 130)
        blue_range = (blue_range_start, blue_range_start + 125)

        proportional = Nebula_rng.randint(100, 500)
        nebula_center = (Nebula_rng.randint(0, screen.get_width()), Nebula_rng.randint(0, screen.get_height()))
        NebulaGenerator(nebula_center, #center
                        proportional, # nebula_radius
                        proportional, # clouds
                        red_range, green_range, blue_range, # colors
                        Nebula_rng.randint(10, 20) # cloud_alpha
                        )

        if debug == 1:
            print(f"NEBULA_NUMBER: {nebula+1}\nNEBULA_CENTER: {nebula_center}\nNEBULA_COLOR_RANGES: ({red_range}, {green_range}, {blue_range})\nNEBULA_RADIUS and CLOUDS: {proportional}\n")


    Black_Hole_rng = random.Random(Universe_Seed + 5)  # pre determined seemingly random lists (RNG)

    singularity = Black_Hole_rng.randint(0, 7)
    if singularity == 0:
        density = Black_Hole_rng.randint(0, 7)
        if density == 0:
            black_hole_radius = Black_Hole_rng.randint(100, 200)
        else:
            black_hole_radius = Black_Hole_rng.randint(10, 99)

        if black_hole_radius > 50:
            supermassive = True
        else:
            supermassive = False

        black_hole_center = (Black_Hole_rng.randint(0, screen.get_width()),
                             Black_Hole_rng.randint(0, screen.get_height()))
        black_hole_rotation = Black_Hole_rng.uniform(-math.pi/2, math.pi / 2)
        BlackHoleGenerator(black_hole_radius, black_hole_rotation, black_hole_center)

        if debug == 1:
            print(
                f"BLACK_HOLE_RADIUS: {black_hole_radius}\nBLACK_HOLE_CENTER: {black_hole_center}\nBLACK_HOLE_ROTATION: {black_hole_rotation}\n")
    else:
        supermassive = False

    if not supermassive:
        global Galaxy_rng
        Galaxy_rng = random.Random(Universe_Seed + 3) # pre determined seemingly random lists (RNG)
        for galaxy in range(Galaxy_rng.randint(1, 5)):
            giga_galaxy = Galaxy_rng.randint(0, 10)
            if giga_galaxy == 7:
                max_radius = Galaxy_rng.randint(480, 1000)
                greed = True
            elif 1 <= giga_galaxy <= 6:
                max_radius = Galaxy_rng.randint(201, 479)
                greed = False
            else:
                max_radius = Galaxy_rng.randint(30, 200)
                greed = False

            if max_radius < 100:
                turns = math.pi * (2 + Galaxy_rng.uniform(.4, .9))
                density_variation = Galaxy_rng.randint(1, 2)
            else:
                turns = Galaxy_rng.uniform(3.5 * math.pi, 6 * math.pi)
                density_variation = Galaxy_rng.randint(2, 10)

            bigtheta = Galaxy_rng.uniform(0, math.pi * 2)
            p = 1
            q = Galaxy_rng.uniform(.1, 2)
            bsub = .02

            galaxy_color = Galaxy_rng.randint(1, 7)
            if galaxy_color == 1: # bluish
                red_range = (0, 140)
                green_range = (40, 140)
                blue_range = (120, 255)
                gas_alpha = Galaxy_rng.randint(5, 12)
            elif galaxy_color == 2: # magenta
                red_range = (120, 180)
                green_range = (0, 80)
                blue_range = (150, 255)
                gas_alpha = Galaxy_rng.randint(7, 13)
            elif galaxy_color == 3: # tealish
                red_range = (0, 180)
                green_range = (120, 255)
                blue_range = (150, 255)
                gas_alpha = Galaxy_rng.randint(3, 10)
            elif galaxy_color == 4: # yellowish orange
                red_range = (180, 230)
                green_range = (110, 160)
                blue_range = (40, 90)
                gas_alpha = Galaxy_rng.randint(5, 10)
            elif galaxy_color == 5: # warm dust
                red_range = (245, 255)
                green_range = (215, 225)
                blue_range = (175, 185)
                gas_alpha = Galaxy_rng.randint(2, 5)
            elif galaxy_color == 6: # pinkish
                red_range = (200, 255)
                green_range = (120, 200)
                blue_range = (120, 200)
                gas_alpha = Galaxy_rng.randint(4, 10)
            elif galaxy_color == 7:
                red_range = (40, 120)
                green_range = (20, 100)
                blue_range = (120, 255)
                gas_alpha = Galaxy_rng.randint(10, 15)


            match galaxy_color:
                case 1:
                    GC = "BLUISH"
                case 2:
                    GC = "MAGENTA"
                case 3:
                    GC = "TEALISH"
                case 4:
                    GC = "YELLOWISH ORANGE"
                case 5:
                    GC = "WARM DUST"
                case 6:
                    GC = "PINKISH"
                case 7:
                    GC = "COSMIC"

            center = (Galaxy_rng.randint(0, screen.get_width()), Galaxy_rng.randint(0, screen.get_height()))

            SpiralGalaxyGenerator(max_radius, # max_radius
                                  turns, # turns
                                  bigtheta, # bigtheta
                                  density_variation, # density_variation
                                  p, q, #x and y squish constants (p and q)
                                  bsub, #b (theta coefficient) subtraction increment
                                  red_range, green_range, blue_range, # galaxy gas colors
                                  gas_alpha, #gas_color and gas_alpha
                                  center)

            if debug == 1:
                print(f"GALAXY NUMBER: {galaxy+1}\nMAX_RADIUS: {max_radius}\nTURNS: {turns}\nBIG_THETA: {bigtheta}\nDENSITY_VARIATION: {density_variation}\n"
                  f"XY SQUISH: {p}, {q}\nB_INCREMENT: {bsub}\n"
                  f"GAS_COLORS and GAS_ALPHA: ({red_range}, {green_range}, {blue_range}), {gas_alpha}\nAPPEARANCE: {GC}\nGAS CENTER: {center}\nGREED: {greed}\n")

            if greed:
                break




    Shooting_Star_rng = random.Random(Universe_Seed + 4) # pre determined seemingly random lists (RNG)
    while True:
        exit_check()
        shoot = Shooting_Star_rng.randint(1, 5000000)
        if shoot == 7:
            Shooting_Star(Shooting_Star_rng)
        



if __name__ == "__main__":
    # seed = 0
    # while seed != "":
    #     seed = input("Enter Universe Seed (Hit Enter For Random Seed): ")
    #     try:
    #         seed = int(seed)
    #         break
    #     except ValueError:
    #         continue

    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.NOFRAME)
    screen_info = pygame.display.Info()
    # screen = pygame.display.set_mode((screen_info.current_w - 20, screen_info.current_h - 20)) # windowed

    pygame.display.set_caption("Galaxy Generator")
    clock = pygame.time.Clock()
    clock.tick(60)
    screen.fill((0, 0, 0))

    # if seed == "":
    #     Universe_Generator(random.randint(0,1000000000000), 1)
    # else:
    #     Universe_Generator(seed, 1)

    Universe_Generator(random.randint(0, 1000000000000), 1)
    # Universe_Generator(0)
