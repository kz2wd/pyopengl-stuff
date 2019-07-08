# based on 1.3
# project : make each vertex moves independently, seem glitched

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import random

from copy import deepcopy


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

    return edges, vertices  # rajouter surface un jour ?


def modify_structure(vertices, v_moy):
    interval = 1  # taille intervalle

    vh = []  # valeur haute + ajouter dimension pr ch pt
    vb = []
    for i in range(len(vertices)):
        vh.append([interval/2, interval/2, interval/2])
        vb.append([0, 0, 0])
        for j in range(3):
            vh[i][j] += v_moy[i][j]
            vb[i][j] = vh[i][j] - interval

    for i in range(len(vertices)):
        for j in range(3):
            vertices[i][j] += round(random.uniform(vb[i][j], vh[i][j]), 5)

    # print("vh :" + str(vh))  # affichage pertinent ?
    # print("vb :" + str(vb))

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

    # glRotatef(0, 0, 0, 0)

    edges, vertices = create_structure()
    print("edges : " + str(edges))
    print("vertices : " + str(vertices))
    print("nombre de points : " + str(len(vertices)))

    var_moyenne = []
    for i in range(len(vertices)):
        var_moyenne.append([0, 0, 0])
    # print("var_moyenne : " + str(var_moyenne))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        display_structure(edges, vertices)
        # glRotatef(1, 1, 1, 1)
        pygame.display.flip()

        pygame.time.wait(10)

        old_vertices = deepcopy(vertices)
        vertices = modify_structure(vertices, var_moyenne)

        for i in range(len(vertices)):  # moyenne individuelle
            for j in range(3):
                var_moyenne[i][j] = old_vertices[i][j] - vertices[i][j]

        # print("variations : " + str(var_moyenne))


main()
