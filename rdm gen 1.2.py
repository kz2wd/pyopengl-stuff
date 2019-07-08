# based on 1.1
# project : make the structure moves randomly

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import random


def create_structure():

    nb_pt = random.randrange(5, 20)

    vertices = []
    for i in range(nb_pt):
        vertices.append([random.randrange(-20, 20), random.randrange(-20, 20), random.randrange(-20, 20)])

    u = 0
    for n in range(nb_pt):
        u = u + n + 1
    nb_bord = u

    edges = []
    for i in range(nb_bord):
        for j in range(nb_pt - (i + 1)):
            for k in range(j + 1):
                edges.append([j, k])

    return edges, vertices


def modify_structure(vertices):

    for i in range(len(vertices)):
        for j in range(3):
            vertices[i][j] = vertices[i][j] + round(random.uniform(-0.05, 0.05), 5)

    return vertices


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

    gluPerspective(45, (display[0]/display[1]), 0.1, 200.0)

    glTranslatef(0.0, 0.0, -80)

    glRotatef(0, 0, 0, 0)

    edges, vertices = create_structure()
    print("edges : " + str(edges))
    print("vertices : " + str(vertices))
    print("nombre de points : " + str(len(vertices)))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        display_structure(edges, vertices)
        #glRotatef(1, 1, 1, 1)
        pygame.display.flip()

        pygame.time.wait(10)

        vertices = modify_structure(vertices)


main()
