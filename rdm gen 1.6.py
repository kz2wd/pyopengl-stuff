# based on 1.3
# project : generate circle => cylinder => complex structure

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import random
import math

from copy import deepcopy


def create_circle1(start=[0, 0, 0], r=2, p=3, num_pt=0):  # start = [x, y, z]

    # r = rayon
    plan = 1  # to use later
    # p = precision; number of pt per circle
    vertices = [start]

    for i in range(p):
        new_pt = [round((math.cos(2 * math.pi / p * i) * r), 4) + start[0],
                  round((math.sin(2 * math.pi / p * i) * r), 4) + start[1],
                  start[2]]
        vertices.append(new_pt)

    edges = []

    e = num_pt * p + num_pt  # ecart
    for i in range(1, p, 1):
        edges.append([i + e, i + 1 + e])
    edges.append([p + e, 1 + e])
    # print("start : " + str(start))

    return edges, vertices


def create_circle2(start=[0, 0, 0], r=[2, 2, 2], p=3, num_pt=0):  # start = [x, y, z]

    # r = rayon
    plan = 1  # to use later
    # p = precision; number of pt per circle
    vertices = [start]

    for i in range(p):
        new_pt = [round((math.cos(2 * math.pi / p * i) * r[i]), 4) + start[0],
                  round((math.sin(2 * math.pi / p * i) * r[i]), 4) + start[1],
                  start[2]]
        vertices.append(new_pt)

    edges = []

    e = num_pt * p + num_pt  # ecart
    for i in range(1, p, 1):
        edges.append([i + e, i + 1 + e])
    edges.append([p + e, 1 + e])
    # print("start : " + str(start))

    return edges, vertices


def create_cylinder1(circle_pos=[[0, 0, 0]], r=2, p=3):
    edges = []
    vertices = []
    for i in range(len(circle_pos)):
        edges_to_add, vertices_to_add = create_circle1(circle_pos[i], r, p, i)
        for j in edges_to_add:
            edges.append(j)
        for j in vertices_to_add:
            vertices.append(j)
    for i in range(len(circle_pos) - 1):  # to do after the circles are created
        for j in range(p):  # edges between circles
            edges.append([j + 1 + i * p + i, j + p + 2 + i + i * p])
        # print(edges)
    # print("len circle pos : " + str(len(circle_pos)))
    # print("vertcies : " + str(vertices))
    # print("edges : " + str(edges))
    return edges, vertices


def create_cylinder2(circle_pos=[[0, 0, 0]], r=[[3, 3, 3]], p=3):
    edges = []
    vertices = []
    for i in range(len(circle_pos)):
        edges_to_add, vertices_to_add = create_circle2(circle_pos[i], r[i], p, i)
        for j in edges_to_add:
            edges.append(j)
        for j in vertices_to_add:
            vertices.append(j)
    for i in range(len(circle_pos) - 1):  # to do after the circles are created
        for j in range(p):  # edges between circles
            edges.append([j + 1 + i * p + i, j + p + 2 + i + i * p])
        # print(edges)
    # print("len circle pos : " + str(len(circle_pos)))
    # print("vertcies : " + str(vertices))
    # print("edges : " + str(edges))
    return edges, vertices


def modify_structure(vertices, v_moy):
    interval = 0.1  # taille intervalle

    vh = [interval/2, interval/2, interval/2]  # valeur haute
    for i in range(3):
        vh[i] += v_moy[i]

    vb = [0, 0, 0]
    for i in range(3):    # valeur basse
        vb[i] = vh[i] - interval

    for i in range(len(vertices)):
        for j in range(3):
            vertices[i][j] += round(random.uniform(vb[j], vh[j]), 5)

    print("vh :" + str(vh))

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

    glTranslatef(0.0, 0.0, -40)

    # glRotatef(0, 0, 0, 0)

    cyl_pos = [[0, 0, 0], [0, 0, 5], [0, 0, 10], [0, 0, 15]]
    p = 8

    r = [[3, 4, 9, 4, 3, 2, 5, 10], [3, 4, 5, 6, 3, 4, 5, 6], [3, 7, 5, 6, 8, 4, 7, 6], [3, 4, 1, 6, 6, 4, 5, 6]]

    edges, vertices = create_cylinder2(cyl_pos, r, p)
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
        glRotatef(1, 1, 1, 1)
        pygame.display.flip()

        pygame.time.wait(10)


main()
