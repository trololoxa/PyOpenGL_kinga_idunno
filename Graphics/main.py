from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Graphics.Primitive import Primitive


class Main:
    def __init__(self):
        self.w, self.h = 500, 500
        self.name = 'name'
        self.primitives = []
        self.create_primitives([{'vertices': [[100, 100, 0], [200, 100, 0], [200, 200, 0], [100, 200, 0]],
                                 'colors': [[1, 1, 0, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]],
                                 'normals': [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
                                 'obj_type': 'quad'},
                                {'vertices': [[300, 300, 0], [400, 300, 0], [400, 400, 0], [300, 400, 0]],
                                 'colors': [[1, 1, 0, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]],
                                 'normals': [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
                                 'obj_type': 'triangle'}
                                ])

    def create_primitives(self, data):
        self.primitives += [Primitive(data=single_prim_data) for single_prim_data in data]
                            
    def iterate(self):
        glViewport(0, 0, 500, 500)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        self.iterate()
        glColor3f(1.0, 0.0, 3.0)
        for primitive in self.primitives:
            primitive.draw()
        glutSwapBuffers()

    def reshape(self):
        pass

    def mouse(self):
        pass

    def keyboard(self):
        pass

    def idle(self):
        pass

    def run(self):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(500, 500)
        glutInitWindowPosition(-5, 0)
        wind = glutCreateWindow(self.name.encode('utf-8'))
        glutDisplayFunc(self.display)
        glutReshapeFunc(self.reshape)
        glutMouseFunc(self.mouse)
        glutKeyboardFunc(self.keyboard)
        glutIdleFunc(self.idle)
        glutMainLoop()
