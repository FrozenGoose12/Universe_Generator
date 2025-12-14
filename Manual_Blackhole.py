# Copyright (c) 2025 FrozenGoose12
# Permission is granted to use and modify this file for personal
# and educational purposes only. Commercial use is strictly prohibited
# without written permission from the author.

import pygame, math, sys

pygame.init()
screen_info = pygame.display.Info()
screen = pygame.display.set_mode((screen_info.current_w-20, screen_info.current_h-20))
clock = pygame.time.Clock()

def exit_check():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

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
    # l4 = (100, 100, 255)

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
            theta += .01
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

    while True:
        exit_check()
        clock.tick(60)

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    BlackHoleGenerator(100, 100, (screen.get_width() // 2, screen.get_height() // 2))
    # BlackHoleGenerator(40, .5, (1400, 800))
