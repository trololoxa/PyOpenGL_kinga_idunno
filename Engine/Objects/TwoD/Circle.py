from math import pi, sin, cos
from OpenGL.GL import glBegin, GL_TRIANGLE_FAN, glVertex2f, glEnd, glColor4f, GL_LINE_LOOP
from Engine.Objects.basic.Object import Object


class Circle(Object):
    """
        data structure:
        {
        'obj_type': [GL_LINE_LOOP, num_lines],
        'num_lines': 200
        'color': [1, 0, 1, 1],
        'center': [0, 0]
        'radius': 1
        }
        """
    def __init__(self, data):
        super().__init__(data=data, draw_func=self.draw_circle,
                         type_list_change=['line_loop', data['num_lines']], process_data=False)

    def draw_circle(self, data):
        glBegin(GL_LINE_LOOP)
        glColor4f(data['color'][0], data['color'][1], data['color'][2], data['color'][3])
        for i in range(data['num_lines']):
            theta = 2.0 * pi * float(i) / float(data['num_lines'])
            x = data['radius'] * cos(theta)
            y = data['radius'] * sin(theta)
            glVertex2f(x + data['center'][0], y + data['center'][1])
        glEnd()


class FilledCircle(Object):
    def __init__(self, data):
        super().__init__(data=data, draw_func=self.draw_filled_circle,
                         type_list_change=['tri_fan', data['num_triangles']], process_data=False)

    def draw_filled_circle(self, data):
        """
        data structure:
        {
        'obj_type': [GL_TRIANGLE_FAN, num_triangles],
        'num_triangles': 200
        'color': [1, 0, 1, 1],
        'center': [0, 0]
        'radius': 1
        }
        """
        glBegin(GL_TRIANGLE_FAN)
        glColor4f(data['color'][0], data['color'][1], data['color'][2], data['color'][3])
        for i in range(data['num_triangles']):
            glVertex2f(
                (data['center'][0] + (data['radius'] * cos(i * pi * 2 / data['num_triangles']))),
                (data['center'][1] + (data['radius'] * sin(i * pi * 2 / data['num_triangles']))))
        glEnd()

"""
def drawFilledSun():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0, 0, -10)
    x, y = 0, 0
    radius = 0.30
    glColor3ub(255, 0, 0)
    twicePi = 2.0 * pi
    x = 0
    y = 0
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(20):
        glVertex2f ((x + (radius * cos(i * twicePi / 20))), (y + (radius * sin(i * twicePi / 20))))
    glEnd()


def DrawCircle(cx, cy, r, num_segments):
    glBegin(GL_LINE_LOOP)
    for ii in range(num_segments):
        theta = 2.0 * pi * float(ii) / float(num_segments)
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex2f(x + cx, y + cy)
    glEnd()"""