# This is a sample Python script.
import swe2
import swe
import glfw
from OpenGL.GL.shaders import compileProgram, compileShader
from plane import meshPlane
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def get_swe(nx,nt,distance,g):
    swe2.shallow_water_1d_test(nx,nt,distance,g)
    file1 = open("sw1d_h.txt", "r")
    h_raw = file1.readlines()
    file1.close()
    H = []
    for i in h_raw:
        H.append(i.split())
    return H

def get_H(file="sw1d_h.txt"):
    file1 = open(file, "r")
    h_raw = file1.readlines()
    file1.close()
    H = []
    for i in h_raw:
        H.append(i.split())
    return H

def main():

    ANCHO=4
    LARGO=30
    DISTANCIA=0.5
    #swe.shallow_water_1d_test(LARGO)
    #get_swe(LARGO,500,DISTANCIA,5)
    Plane = meshPlane(get_H('4_30_05_99_2.txt'),ANCHO,LARGO,DISTANCIA) #30 largo
    #Plane = meshPlane(get_H(),ANCHO,LARGO,DISTANCIA) #20 largo

    pygame.init()
    display = (1200,800) #convertir a metodo el ancho alto
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(60, (display[0] / display[1]), 0, 50.0)
    glTranslatef(-0, -2.5, -6)
    glRotatef(1, 1, 1, 1)
    glRotatef(80, 0, 1, 0)
    glRotatef(1, 1, 1, 1)
    flag = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    glTranslatef(0.5, 0, 0)
                if event.key == pygame.K_o:
                    glTranslatef(-0.5, 0, 0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0, 0.5, 0)
                if event.key == pygame.K_UP:
                    glTranslatef(0, -0.5, 0)
                if event.key == pygame.K_LEFT:
                    glTranslatef(0, 0, 0.5)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0, 0, -0.5)
        if flag==1:
            Plane.next_step()
            flag=0
        else:
            flag=1
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Plane.updatePlane()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == '__main__':

    main()

