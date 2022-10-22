from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Engine.Graphics.Scene import Scene
from types import SimpleNamespace


class Main:
    keys = {b'\x1b': 'esc'}
    values = SimpleNamespace(**{v: k for k, v in keys.items()})

    def __init__(self):
        self.w, self.h = 1024, 768
        self.name = 'idunno mb it is name'
        self.scene: Scene = Scene()

    def display(self):
        glClearColor(0, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        self.scene.render()
        glPopMatrix()
        glutSwapBuffers()

    def interactive_console(self):
        pass

    def reshape(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60.0, w / h, 0.1, 20000.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        glTranslatef(0, 0, -2)

    def mouse(self, button, state, x, y):
        pass

    def keyboard(self, key, x, y):
        print(key)
        match key:
            case self.values.esc:
                glutLeaveMainLoop()

    def idle(self):
        self.interactive_console()

    def run(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_DEPTH | GLUT_RGBA)
        glutInitWindowSize(self.w, self.h)
        glutInitWindowPosition(0, 0)
        glutCreateWindow(self.name.encode('utf-8'))

        glutDisplayFunc(self.display)
        glutReshapeFunc(self.reshape)
        glutMouseFunc(self.mouse)
        glutKeyboardFunc(self.keyboard)
        glutIdleFunc(self.idle)

        glClearColor(0, 0, 0, 0)
        glShadeModel(GL_SMOOTH)
        glClearDepth(1.0)
        glEnable(GL_DEPTH_TEST)

        glutMainLoop()
