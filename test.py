from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Graphics.Primitive import Primitive

w, h= 500, 500

primitives = []
primitives += [Primitive(data={'vertices': [[100, 100, 0], [200, 100, 0], [200, 200, 0], [100, 200, 0]],
                               'colors': [[1, 1, 0, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]],
                               'normals': [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
                               'obj_type': 'quad'}),
               Primitive(data={'vertices': [[300, 300, 0], [400, 300, 0], [400, 400, 0], [300, 400, 0]],
                               'colors': [[1, 1, 0, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]],
                               'normals': [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
                               'obj_type': 'triangle'})
               ]


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def show_screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    for primitive in primitives:
        primitive.draw()
    glutSwapBuffers()

def reshape():
    pass

def mouse():
    pass

def keyboard():
    pass

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(-5, 0)
wind = glutCreateWindow("OpenGL Coding Practice".encode('utf-8'))
glutDisplayFunc(show_screen)
#glutReshapeFunc(reshape)
#glutMouseFunc(mouse)
#glutKeyboardFunc(keyboard)
glutIdleFunc(show_screen)
glutMainLoop()
