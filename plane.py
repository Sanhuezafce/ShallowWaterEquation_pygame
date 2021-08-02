from OpenGL.GL import *


class meshPlane:

    def __init__(self, init_cond, x=10, y=10, distance=1, ):
        self.__x = x #misma fuerza
        self.__y = y #iterar sobre los H[i]
        self.__vertices = []
        self.__edges = []
        self.__surfaces = []
        self.__colors = []
        self.__distance = distance
        self.initialize_stuff()
        self.__H = init_cond
        self.__current_h= 0
        self.apply_current_h()

    @property
    def current_h(self):
        return self.__current_h

    @current_h.setter
    def current_h(self, a):
        self.__current_h = a

    @property
    def H(self):
        return self.__H

    @H.setter
    def H(self, a):
        self.__H = a

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, a):
        self.__x = a

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, a):
        self.__y = a

    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, a):
        self.__distance = a

    @property
    def vertices(self):
        return self.__vertices

    @vertices.setter
    def vertices(self, a):
        self.__vertices = a

    @property
    def edges(self):
        return self.__edges

    @edges.setter
    def edges(self, a):
        self.__edges = a

    @property
    def surfaces(self):
        return self.__surfaces

    @surfaces.setter
    def surfaces(self, a):
        self.__surfaces = a

    @property
    def colors(self):
        return self.__colors

    @colors.setter
    def colors(self, a):
        self.__colors = a

    def next_step(self):
        if len(self.H[0])-1<=self.current_h+1:
            self.current_h=0
        else:
            self.current_h+=1
        self.apply_current_h()

    def apply_current_h(self):
        current_h = []
        for i in self.H:
            current_h.append(i[self.current_h])
        start_y = - ((self.y / 2) * self.distance)
        # vertex
        self.vertices=[]
        for j in range(self.y):
            start_x = -((self.x / 2) * self.distance)
            for i in range(self.x):
                self.vertices.append((start_x, float(current_h[j]), start_y))
                start_x += self.distance
            start_y += self.distance
        self.vertices = tuple(self.vertices)

    def initialize_stuff(self):
        start_y = -((self.y / 2) * self.distance)
        # vertex
        for j in range(self.y):
            start_x = -((self.x / 2) * self.distance)
            for i in range(self.x):
                self.vertices.append((start_x, 0, start_y))
                start_x += self.distance
            start_y += self.distance
        self.vertices = tuple(self.vertices)
        # edges
        for j in range(self.y):
            if j == self.y - 1:  # ultima col
                for i in range(self.x - 1):
                    self.edges.append((i + (j * self.x), i + (j * self.x) + 1))
                break
            for i in range(self.x - 1):
                self.edges.append((i + (j * self.x), i + (j * self.x) + 1))
            for i in range(self.x):

                if i == 0:
                    self.edges.append((j * self.x, ((j + 1) * self.x)))
                else:
                    self.edges.append((i + (j * self.x), (i - 1) + ((j + 1) * self.x)))
                    self.edges.append((i + (j * self.x), i + ((j + 1) * self.x)))
        self.edges = tuple(self.edges)
        # surfaces
        for j in range(self.y - 1):
            for i in range(self.x - 1):
                self.surfaces.append((i + (j * self.x), i + 1 + (j * self.x), i + self.x + (j * self.x)))
                self.surfaces.append((i + 1 + (j * self.x), i + self.x + (j * self.x), i + self.x + 1 + (j * self.x)))
        self.surfaces = tuple(self.surfaces)
        # colors
        for i in range(len(self.edges)):
            if i % 2 == 0:
                self.colors.append((0.3, 0.3, 1))
            else:
                self.colors.append((0.6, 1, 1))
        self.colors = tuple(self.colors)

        self.__x_force = [0] * len(self.vertices)
        self.__y_force = [0] * len(self.vertices)

    def updatePlane(self):
        glBegin(GL_TRIANGLES)
        for surface in self.surfaces:
            x = 0
            for vertex in surface:
                x += 1
                glColor3fv(self.colors[x])
                glVertex3fv(self.vertices[vertex])
        glEnd()

        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()
