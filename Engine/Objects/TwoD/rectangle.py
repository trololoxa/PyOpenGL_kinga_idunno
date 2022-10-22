from Engine.Objects.basic.Object import Object
from OpenGL.GL import glBegin, glVertex2f, glEnd, glColor4f, GL_QUADS


class Rectangle(Object):
    """
        data structure:
        {
        'obj_type': [GL_QUADS, 4],
        'color': [1, 0, 0, 1],
        'center': [0, 0]
        'scale': [1, 1]
        }
        """

    def __init__(self, data):
        super().__init__(data=data, draw_func=self.draw_rectangle, process_data=False)

    def draw_rectangle(self, data):
        glBegin(GL_QUADS)

        glColor4f(data['color'][0], data['color'][1], data['color'][2], data['color'][3])

        glVertex2f(data['center'][0] + (data['scale'][0] / 2), data['center'][1] + (data['scale'][1] / 2))
        glVertex2f(data['center'][0] + (data['scale'][0] / 2), data['center'][1] - (data['scale'][1] / 2))
        glVertex2f(data['center'][0] - (data['scale'][0] / 2), data['center'][1] - (data['scale'][1] / 2))
        glVertex2f(data['center'][0] - (data['scale'][0] / 2), data['center'][1] + (data['scale'][1] / 2))

        glEnd()
