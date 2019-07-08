
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import random


def structure_3d():

    nb_pt = random.randrange(5, 20)

    verticies = []
    for i in range(nb_pt):
        verticies.append(((random.randrange(-20, 20)), (random.randrange(-20, 20)), (random.randrange(-20, 20))))

    u = 0
    for n in range(nb_pt):
        u = u + n + 1
    nb_bord = u

    edges = []
    for i in range(nb_bord):
        for j in range(nb_pt - (i + 1)):
            for k in range(j + 1):
                edges.append((j, k))


    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 100.0)

    glTranslatef(0.0, 0.0, -60)

    # glRotatef(0, 0, 0, 0)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        structure_3d()
        pygame.display.flip()

        pygame.time.wait(300)


main()
