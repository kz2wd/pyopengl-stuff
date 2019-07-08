# based on 1.0
# project : generate, display and rotate around random generated structures

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import random


def create_structure():

    nb_pt = random.randrange(5, 10)

    vertices = []
    for i in range(nb_pt):
        vertices.append(((random.randrange(-20, 20)), (random.randrange(-20, 20)), (random.randrange(-20, 20))))

    u = 0
    for n in range(nb_pt):
        u = u + n + 1
    nb_bord = u

    edges = []
    for i in range(nb_bord):
        for j in range(nb_pt - (i + 1)):
            for k in range(j + 1):
                edges.append((j, k))

    return edges, vertices


def display_structure(edges, vertices):

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 110.0)

    glTranslatef(0.0, 0.0, -80)

    # glRotatef(0, 0, 0, 0)

    edges, vertices = create_structure()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        for i in range(10):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            display_structure(edges, vertices)
            glRotatef(1, 1, 1, 1)
            pygame.display.flip()
        edges, vertices = create_structure()

        pygame.time.wait(10)


main()
